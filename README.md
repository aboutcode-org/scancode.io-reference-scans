# scancode.io-reference-scans
A set of reference scans with ScanCode.io updated with each new release to track quality and performance progress over time.

Latest scans were created with ScanCode.io v21.8.2 (using ScanCode Toolkit v21.8.4). Earliest scans were created with ScanCode.io v21.6.10 (using ScanCode Toolkit v21.6.7).

## `docker` pipeline:
- input: Debian Linux `debian:buster-slim` for linux/amd64
  - docker://debian@sha256:0fe071e7b4811869579bef3f308096be22f672aa52f121b62c6c401f18abb97c
  - scan files: docker/debian-buster*

| Name | UUID | Creation Date | Number of Discovered Packages | Number of Missing Discovered Package Resources | Number of Modified Discovered Package Resources | Number of Application Packages | Number of Ignored Empty Files | Number of Ignored Uninteresting Files | Number of Ignored Whiteout Files | Number of Resources with No Licenses | Number of Scanned Resources | Number of System Packages | Number of Resources with Unknown Licenses |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| [debian-buster-slim-0fe071e7](http://staging.scancode.io/api/projects/4d768518-ccc0-4446-bfd0-a39b7b30ab27) | 4d768518-ccc0-4446-bfd0-a39b7b30ab27 | 2021-08-03T00:10:58.164888Z | 84 | 38 | 0 | 0 | 0 | 537 | 0 | 373 | 42 | 2064 | 9 |
| [debian-buster-slim0d6ffa74](http://staging.scancode.io/api/projects/ba778a4c-f4d8-4aba-823e-69c7559442db) | ba778a4c-f4d8-4aba-823e-69c7559442db | 2021-07-20T21:01:11.749035Z | 84 | 38 | 0 | 0 | 0 | 537 | 0 | 373 | 40 | 2064 | 11 |


- input: CentOS Linux `elasticsearch:7.13.3` for linux/amd64
  - docker://elasticsearch@sha256:e54cc1adf707472e8d4b916227f536bd486198d83aaaf5a30459dd6b966cca03
  - https://hub.docker.com/layers/elasticsearch/library/elasticsearch/7.13.3/images/sha256-e54cc1adf707472e8d4b916227f536bd486198d83aaaf5a30459dd6b966cca03?context=explore
  - scan files: docker/elasticsearch*

| Name | UUID | Creation Date | Number of Discovered Packages | Number of Missing Discovered Package Resources | Number of Modified Discovered Package Resources | Number of Application Packages | Number of Ignored Empty Files | Number of Ignored Uninteresting Files | Number of Ignored Whiteout Files | Number of Resources with No Licenses | Number of Scanned Resources | Number of System Packages | Number of Resources with Unknown Licenses |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| [elasticsearch-7.13.3-e54cc1ad-run-2](http://staging.scancode.io/api/projects/b26c3df4-c701-4b10-a950-b4ce89c5e714) | b26c3df4-c701-4b10-a950-b4ce89c5e714 | 2021-08-03T00:05:28.351063Z | 247 | 243 | 235 | 258 | 1420 | 170 | 132 | 5249 | 730 | 11773 | 44 |
| [elasticsearch-7.13.3-e54cc1ad](http://staging.scancode.io/api/projects/0b89a4e3-4afc-4c00-8f35-be741f201c8a) | 0b89a4e3-4afc-4c00-8f35-be741f201c8a | 2021-07-20T21:08:40.008417Z | 247 | 243 | 235 | 258 | 1420 | 170 | 132 | 5251 | 730 | 11771 | 44 |


- input: Alpine Linux `nginx:1.20.1-alpine-perl` for linux/amd64
  - docker://nginx@sha256:e8984445b0175f26a07e78461dfb8dff90867ed8f7c3041b1fb3088fad942022
  - https://hub.docker.com/layers/nginx/library/nginx/1.20.1-alpine-perl/images/sha256-e8984445b0175f26a07e78461dfb8dff90867ed8f7c3041b1fb3088fad942022?context=explore
  - scan files: docker/nginx*

| Name | UUID | Creation Date | Number of Discovered Packages | Number of Missing Discovered Package Resources | Number of Modified Discovered Package Resources | Number of Application Packages | Number of Ignored Empty Files | Number of Ignored Uninteresting Files | Number of Ignored Whiteout Files | Number of Resources with No Licenses | Number of Scanned Resources | Number of System Packages | Number of Resources with Unknown Licenses |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| [alpine-httpie-de5b79b4-run-2](http://staging.scancode.io/api/projects/727f7191-4087-41f4-9c70-b5cf5058433f) | 727f7191-4087-41f4-9c70-b5cf5058433f | 2021-08-03T00:18:01.306755Z | 55 | 20 | 3 | 12 | 13 | 15 | 3 | 199 | 505 | 4323 | 8 |
| [alpine-httpie-de5b79b4](http://staging.scancode.io/api/projects/634adeda-d453-48c4-ba4d-1e06e0e47b77) | 634adeda-d453-48c4-ba4d-1e06e0e47b77 | 2021-07-20T22:31:51.990930Z | 55 | 20 | 3 | 12 | 13 | 15 | 3 | 200 | 505 | 4322 | 8 |


- input: Windows `mongo:4.4.7-windowsservercore` for windows/amd64
  - docker://mongo@sha256:73dc6490e1159b56631bbcbd87e5cade415596dc75c26186860761cdb0ceab2a
  - https://hub.docker.com/layers/mongo/library/mongo/4.4.7-windowsservercore/images/sha256-73dc6490e1159b56631bbcbd87e5cade415596dc75c26186860761cdb0ceab2a?context=explore
  - scan files: docker/windows-mongo*

| Name | UUID | Creation Date | Number of Discovered Packages | Number of Missing Discovered Package Resources | Number of Modified Discovered Package Resources | Number of Application Packages | Number of Ignored Empty Files | Number of Ignored Uninteresting Files | Number of Ignored Whiteout Files | Number of Resources with No Licenses | Number of Scanned Resources | Number of System Packages | Number of Resources with Unknown Licenses |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| [mongo-4.4.7-windowsservercore-25673dc6490e](http://staging.scancode.io/api/projects/6d682971-ef06-4894-8705-34db5397c2ac) | 6d682971-ef06-4894-8705-34db5397c2ac | 2021-07-20T22:17:39.478859Z | 7250 | 0 | 0 | 7258 | 41656 | 0 | 10141 | 56880 | 395 | 0 | 21 |


- input: Windows `python:windowsservercore-ltsc2016` for windows/amd64
  - docker://python@sha256:1ad782fdc694d2fd57227532267e5fb45be9f7b8c637365b1d05d789f1894b0c
  - https://hub.docker.com/layers/python/library/python/windowsservercore-ltsc2016/images/sha256-1ad782fdc694d2fd57227532267e5fb45be9f7b8c637365b1d05d789f1894b0c?context=explore
  - scan files: docker/windows-python*

| Name | UUID | Creation Date | Number of Discovered Packages | Number of Missing Discovered Package Resources | Number of Modified Discovered Package Resources | Number of Application Packages | Number of Ignored Empty Files | Number of Ignored Uninteresting Files | Number of Ignored Whiteout Files | Number of Resources with No Licenses | Number of Scanned Resources | Number of System Packages | Number of Resources with Unknown Licenses |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| [windows-python-1ad782fd-run-2](http://staging.scancode.io/api/projects/a2939084-9d89-48a5-aedd-66a972264be0) | a2939084-9d89-48a5-aedd-66a972264be0 | 2021-08-03T00:21:32.816966Z | 23267 | 0 | 0 | 28580 | 52776 | 0 | 13533 | 79914 | 958 | 0 | 83 |
| [windows-python-1ad782fd](http://staging.scancode.io/api/projects/336543c7-74cb-4a31-9be2-0f2ae9aba6ab) | 336543c7-74cb-4a31-9be2-0f2ae9aba6ab | 2021-07-20T22:36:45.350924Z | 10958 | 0 | 0 | 16282 | 52776 | 0 | 13533 | 92171 | 993 | 0 | 89 |


- input: Distroless Linux `distrolessdev/base:nonroot` for linux/amd64
  - docker://distrolessdev/base@sha256:f2ff292d5f916630cd0c841e45ede1f2ccd7436e17ab22548873a455c562a413
  - https://hub.docker.com/layers/distrolessdev/base/nonroot/images/sha256-f2ff292d5f916630cd0c841e45ede1f2ccd7436e17ab22548873a455c562a413?context=explore
  - scan files: docker/distrolessdev*

| Name | UUID | Creation Date | Number of Discovered Packages | Number of Missing Discovered Package Resources | Number of Modified Discovered Package Resources | Number of Application Packages | Number of Ignored Empty Files | Number of Ignored Uninteresting Files | Number of Ignored Whiteout Files | Number of Resources with No Licenses | Number of Scanned Resources | Number of System Packages | Number of Resources with Unknown Licenses |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| [distrolessdev-run-2](http://staging.scancode.io/api/projects/7cbd5111-28e1-4294-8329-8df518d0e03e) | 7cbd5111-28e1-4294-8329-8df518d0e03e | 2021-08-03T00:17:31.813011Z | 6 | 0 | 0 | 0 | 0 | 22 | 0 | 1165 | 30 | 0 | 3 |
| [distrolessdev](http://staging.scancode.io/api/projects/a42d7598-a94c-4ca1-8bc8-38666aebb760) | a42d7598-a94c-4ca1-8bc8-38666aebb760 | 2021-07-20T22:38:28.381902Z | 0 | 0 | 0 | 0 | 0 | 22 | 0 | 1165 | 30 | 0 | 3 |


- input: Alpine Linux `alpine/httpie:latest` for linux/amd64
  - docker://alpine/httpie@sha256:de5b79b4b9e399334103e69865ce5a4203280a3b28fa82f336a4a4814233c3f3
  - https://hub.docker.com/layers/alpine/httpie/latest/images/sha256-de5b79b4b9e399334103e69865ce5a4203280a3b28fa82f336a4a4814233c3f3?context=explore
  - scan files: docker/alpine-httpie*

| Name | UUID | Creation Date | Number of Discovered Packages | Number of Missing Discovered Package Resources | Number of Modified Discovered Package Resources | Number of Application Packages | Number of Ignored Empty Files | Number of Ignored Uninteresting Files | Number of Ignored Whiteout Files | Number of Resources with No Licenses | Number of Scanned Resources | Number of System Packages | Number of Resources with Unknown Licenses |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| [alpine-httpie-de5b79b4-run-2](http://staging.scancode.io/api/projects/727f7191-4087-41f4-9c70-b5cf5058433f) | 727f7191-4087-41f4-9c70-b5cf5058433f | 2021-08-03T00:18:01.306755Z | 55 | 20 | 3 | 12 | 13 | 15 | 3 | 199 | 505 | 4323 | 8 |
| [alpine-httpie-de5b79b4](http://staging.scancode.io/api/projects/634adeda-d453-48c4-ba4d-1e06e0e47b77) | 634adeda-d453-48c4-ba4d-1e06e0e47b77 | 2021-07-20T22:31:51.990930Z | 55 | 20 | 3 | 12 | 13 | 15 | 3 | 200 | 505 | 4322 | 8 |


## `root_filesystem` pipeline:
- input: Debian linux image
  - https://cloud.debian.org/images/cloud/buster/20210621-680/debian-10-genericcloud-amd64-20210621-680.qcow2
  - scan files: rootfs/debian-qcow*

| Name | UUID | Creation Date | Number of Discovered Packages | Number of Missing Discovered Package Resources | Number of Modified Discovered Package Resources | Number of Application Packages | Number of Ignored Empty Files | Number of Ignored Uninteresting Files | Number of Ignored Whiteout Files | Number of Resources with No Licenses | Number of Scanned Resources | Number of System Packages | Number of Resources with Unknown Licenses |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| [debian-qcow-run-2](http://staging.scancode.io/api/projects/449f966c-52cd-4bb0-be07-4c47920809ae) | 449f966c-52cd-4bb0-be07-4c47920809ae | 2021-08-03T00:25:31.625829Z | 303 | 59 | 1 | 0 | 6 | 1996 | 0 | 2928 | 1353 | 12615 | 29 |
| [debian-qcow](http://staging.scancode.io/api/projects/bbb103fb-3b1b-42e2-bdc8-65f4e40eae9b) | bbb103fb-3b1b-42e2-bdc8-65f4e40eae9b | 2021-07-20T22:40:43.305403Z | 303 | 59 | 1 | 0 | 6 | 1996 | 0 | 3069 | 1953 | 11862 | 41 |
