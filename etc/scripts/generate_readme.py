from datetime import datetime
from os.path import abspath
from os.path import dirname
from os.path import join

import os

import jinja2
import requests


# Path of the source file we are in
CURRENT_FILE_PATH = abspath(__file__)
# CURRENT_FILE_PATH assumed to be in the `<project_root>/etc/scripts/` directory
PROJECT_ROOT_PATH = dirname(dirname(dirname(CURRENT_FILE_PATH)))
README_PATH = join(PROJECT_ROOT_PATH, "README.md")
TEMPLATE_PATH = join(PROJECT_ROOT_PATH, "etc", "scripts", "readme.template")


SCANCODE_IO_PROJECTS_ENDPOINT = "http://staging.scancode.io/api/projects/"
SCANCODE_IO_USER = os.environ.get("SCANCODE_IO_USER", "")
SCANCODE_IO_PASSWORD = os.environ.get("SCANCODE_IO_PASSWORD", "")
SCANCODE_IO_AUTH = (SCANCODE_IO_USER, SCANCODE_IO_PASSWORD)


DEBIAN_BUSTER_SLIM_PROJECT_UUIDS = (
    "4d768518-ccc0-4446-bfd0-a39b7b30ab27",
    "ba778a4c-f4d8-4aba-823e-69c7559442db",
)
ELASTICSEARCH_PROJECT_UUIDS = (
    "b26c3df4-c701-4b10-a950-b4ce89c5e714",
    "0b89a4e3-4afc-4c00-8f35-be741f201c8a",
)
ALPINE_PROJECT_UUIDS = (
    "727f7191-4087-41f4-9c70-b5cf5058433f",
    "634adeda-d453-48c4-ba4d-1e06e0e47b77",
)
NGINX_PROJECT_UUIDS = (
    "f865228e-f0d5-40e2-bb0d-298b35f3c706",
    "d6131a17-83af-4f52-82dd-575f75739c22",
)
WINDOWS_MONGO_PROJECT_UUIDS = (
    "e5b899b7-79d1-418c-9432-138990ff594a",
    "6d682971-ef06-4894-8705-34db5397c2ac",
)
WINDOWS_PYTHON_PROJECT_UUIDS = (
    "a2939084-9d89-48a5-aedd-66a972264be0",
    "336543c7-74cb-4a31-9be2-0f2ae9aba6ab",
)
DISTROLESS_PROJECT_UUIDS = (
    "7cbd5111-28e1-4294-8329-8df518d0e03e",
    "a42d7598-a94c-4ca1-8bc8-38666aebb760",
)
ALPINE_HTTPIE_PROJECT_UUIDS = (
    "727f7191-4087-41f4-9c70-b5cf5058433f",
    "634adeda-d453-48c4-ba4d-1e06e0e47b77"
)
DEBIAN_ROOTFS_PROJECT_UUIDS = (
    "449f966c-52cd-4bb0-be07-4c47920809ae",
    "bbb103fb-3b1b-42e2-bdc8-65f4e40eae9b",
)


class ProjectStats:
    def __init__(
        self,
        name,
        uuid,
        pipeline_name,
        created_date,
        dp_total,
        dp_missing_resources,
        dp_modified_resources,
        cr_application_package,
        cr_ignored_empty_files,
        cr_ignored_uninteresting_files,
        cr_ignored_whiteout_files,
        cr_no_licenses,
        cr_scanned,
        cr_system_package,
        cr_unknown_license,
    ):
        self.name = name
        self.uuid = uuid
        self.pipeline_name = pipeline_name
        self.created_date = created_date
        self.dp_total = dp_total
        self.dp_missing_resources = dp_missing_resources
        self.dp_modified_resources = dp_modified_resources
        self.cr_application_package = cr_application_package
        self.cr_ignored_empty_files = cr_ignored_empty_files
        self.cr_ignored_uninteresting_files = cr_ignored_uninteresting_files
        self.cr_ignored_whiteout_files = cr_ignored_whiteout_files
        self.cr_no_licenses = cr_no_licenses
        self.cr_scanned = cr_scanned
        self.cr_system_package = cr_system_package
        self.cr_unknown_license = cr_unknown_license

    @classmethod
    def from_uuid(cls, uuid):
        """
        Return a ProjectStats object whose fields are populated by the stats of
        a project with a UUID of `uuid` on a scancode.io instance.
        """
        project_page = SCANCODE_IO_PROJECTS_ENDPOINT + uuid
        response = requests.get(project_page, auth=SCANCODE_IO_AUTH)
        if not response:
            return
        json_response = response.json()
        name = json_response.get("name", "")
        created_date = json_response.get("created_date", "")
        if created_date:
            created_date = datetime.strptime(created_date, "%Y-%m-%dT%H:%M:%S.%fZ")
            created_date = created_date.strftime("%Y-%m-%d")
        runs = json_response.get("runs", [])
        if runs:
            pipeline_name = runs[0].get("pipeline_name", "")
        codebase_resources_summary = json_response.get("codebase_resources_summary", {})
        discovered_package_summary = json_response.get("discovered_package_summary", {})
        return cls(
            name=name,
            uuid=uuid,
            pipeline_name=pipeline_name,
            created_date=created_date,
            dp_total=discovered_package_summary.get("total", 0),
            dp_missing_resources=discovered_package_summary.get("with_missing_resources", 0),
            dp_modified_resources=discovered_package_summary.get("with_modified_resources", 0),
            cr_application_package=codebase_resources_summary.get("application-package",0),
            cr_ignored_empty_files=codebase_resources_summary.get("ignored-empty-file", 0),
            cr_ignored_uninteresting_files=codebase_resources_summary.get("ignored-not-interesting", 0),
            cr_ignored_whiteout_files=codebase_resources_summary.get("ignored-whiteout", 0),
            cr_no_licenses=codebase_resources_summary.get("no-licenses", 0),
            cr_scanned=codebase_resources_summary.get("scanned", 0),
            cr_system_package=codebase_resources_summary.get("system-package", 0),
            cr_unknown_license=codebase_resources_summary.get("unknown-license", 0)
        )


def collect_project_stats(project_uuid_group):
    """
    Given a list of UUIDs `project_uuid_group`, return a list of ProjectStats
    objects that were instantiated with the UUIDs in `project_uuid_group`
    """
    # Collect project stats by project UUID
    project_stats = []
    for project_uuid in project_uuid_group:
        p = ProjectStats.from_uuid(project_uuid)
        if not p:
            continue
        project_stats.append(p)
    return project_stats


def generate_readme(template=TEMPLATE_PATH):
    with open(template) as f:
        template = f.read()
    template = jinja2.Template(template)
    rendered = template.render(
        debian_buster_slim_project_stats=collect_project_stats(DEBIAN_BUSTER_SLIM_PROJECT_UUIDS),
        elasticsearch_project_stats=collect_project_stats(ELASTICSEARCH_PROJECT_UUIDS),
        alpine_project_stats=collect_project_stats(ALPINE_PROJECT_UUIDS),
        mongo_project_stats=collect_project_stats(WINDOWS_MONGO_PROJECT_UUIDS),
        windows_python_project_stats=collect_project_stats(WINDOWS_PYTHON_PROJECT_UUIDS),
        distroless_project_stats=collect_project_stats(DISTROLESS_PROJECT_UUIDS),
        alpine_httpie_project_stats=collect_project_stats(ALPINE_HTTPIE_PROJECT_UUIDS),
        debian_rootfs_project_stats=collect_project_stats(DEBIAN_ROOTFS_PROJECT_UUIDS)
    )
    with open(README_PATH, "w") as f:
        f.write(rendered)


if __name__ == "__main__":
    generate_readme()
