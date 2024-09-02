# scancode.io-reference-scans
A set of reference scans with ScanCode.io updated with each new release to track quality and performance progress over time.

Latest scans were created with ScanCode.io v21.8.2 (using ScanCode Toolkit v21.8.4). Earliest scans were created with ScanCode.io v21.6.10 (using ScanCode Toolkit v21.6.7).

## `docker` pipeline:
- input: Debian Linux `debian:buster-slim` for linux/amd64
  - docker://debian@sha256:0fe071e7b4811869579bef3f308096be22f672aa52f121b62c6c401f18abb97c
  - scan files: docker/v21.6.10/debian-buster* and docker/v21.8.2/debian-buster*

| Name | Pipeline Name | Creation Date | Number of Discovered Packages | Number of Missing Discovered Package Resources | Number of Modified Discovered Package Resources | Number of Application Packages | Number of Ignored Empty Files | Number of Ignored Uninteresting Files | Number of Ignored Whiteout Files | Number of Resources with No Licenses | Number of Scanned Resources | Number of System Packages | Number of Resources with Unknown Licenses |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| [debian-buster-slim-0fe071e7](https://github.com/aboutcode-org/scancode.io-reference-scans/blob/add-scan-stats-to-readme/docker/v21.8.2/debian-buster-slim-0fe071e7_results-2021-08-17-18-17-10.xlsx.tar.gz) | docker | 2021-08-03 | 84 | 38 | 0 | 0 | 0 | 537 | 0 | 373 | 42 | 2064 | 9 |
| [debian-buster-slim0d6ffa74](https://github.com/aboutcode-org/scancode.io-reference-scans/blob/add-scan-stats-to-readme/docker/v21.6.10/debian-buster-slim0d6ffa74_results-2021-07-20-22-35-15.xlsx.gz) | docker | 2021-07-20 | 84 | 38 | 0 | 0 | 0 | 537 | 0 | 373 | 40 | 2064 | 11 |


- input: CentOS Linux `elasticsearch:7.13.3` for linux/amd64
  - docker://elasticsearch@sha256:e54cc1adf707472e8d4b916227f536bd486198d83aaaf5a30459dd6b966cca03
  - https://hub.docker.com/layers/elasticsearch/library/elasticsearch/7.13.3/images/sha256-e54cc1adf707472e8d4b916227f536bd486198d83aaaf5a30459dd6b966cca03?context=explore
  - scan files: docker/v21.6.10/elasticsearch* and docker/v21.8.2/elasticsearch*

| Name | Pipeline Name | Creation Date | Number of Discovered Packages | Number of Missing Discovered Package Resources | Number of Modified Discovered Package Resources | Number of Application Packages | Number of Ignored Empty Files | Number of Ignored Uninteresting Files | Number of Ignored Whiteout Files | Number of Resources with No Licenses | Number of Scanned Resources | Number of System Packages | Number of Resources with Unknown Licenses |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| [elasticsearch-7.13.3-e54cc1ad-run-2](https://github.com/aboutcode-org/scancode.io-reference-scans/blob/add-scan-stats-to-readme/docker/v21.8.2/elasticsearch-7.13.3-e54cc1ad-run-2_results-2021-08-17-18-06-37.xlsx.tar.gz) | docker | 2021-08-03 | 247 | 243 | 235 | 258 | 1420 | 170 | 132 | 5249 | 730 | 11773 | 44 |
| [elasticsearch-7.13.3-e54cc1ad](https://github.com/aboutcode-org/scancode.io-reference-scans/blob/add-scan-stats-to-readme/docker/v21.6.10/elasticsearch-7.13.3-e54cc1ad_results-2021-07-20-22-20-20.xlsx.gz) | docker | 2021-07-20 | 247 | 243 | 235 | 258 | 1420 | 170 | 132 | 5251 | 730 | 11771 | 44 |


- input: Alpine Linux `nginx:1.20.1-alpine-perl` for linux/amd64
  - docker://nginx@sha256:e8984445b0175f26a07e78461dfb8dff90867ed8f7c3041b1fb3088fad942022
  - https://hub.docker.com/layers/nginx/library/nginx/1.20.1-alpine-perl/images/sha256-e8984445b0175f26a07e78461dfb8dff90867ed8f7c3041b1fb3088fad942022?context=explore
  - scan files: docker/v21.6.10/nginx* and docker/v21.8.2/nginx*

| Name | Pipeline Name | Creation Date | Number of Discovered Packages | Number of Missing Discovered Package Resources | Number of Modified Discovered Package Resources | Number of Application Packages | Number of Ignored Empty Files | Number of Ignored Uninteresting Files | Number of Ignored Whiteout Files | Number of Resources with No Licenses | Number of Scanned Resources | Number of System Packages | Number of Resources with Unknown Licenses |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| [nginx-e8984445-run-2](https://github.com/aboutcode-org/scancode.io-reference-scans/blob/add-scan-stats-to-readme/docker/v21.8.2/nginx-e8984445-run-2_results-2021-08-17-18-12-35.xlsx.tar.gz) | docker | 2021-08-03 | 44 | 30 | 1 | 0 | 0 | 23 | 21 | 5 | 1 | 2835 | 0 |
| [nginx-e8984445](https://github.com/aboutcode-org/scancode.io-reference-scans/blob/add-scan-stats-to-readme/docker/v21.6.10/nginx-1.20.1_results-2021-07-20-22-18-14.xlsx.gz) | docker | 2021-07-20 | 44 | 30 | 1 | 0 | 0 | 23 | 21 | 5 | 1 | 2835 | 0 |


- input: Windows `mongo:4.4.7-windowsservercore` for windows/amd64
  - docker://mongo@sha256:73dc6490e1159b56631bbcbd87e5cade415596dc75c26186860761cdb0ceab2a
  - https://hub.docker.com/layers/mongo/library/mongo/4.4.7-windowsservercore/images/sha256-73dc6490e1159b56631bbcbd87e5cade415596dc75c26186860761cdb0ceab2a?context=explore
  - scan files: docker/v21.6.10/windows-mongo* and docker/v21.8.2/windows-mongo*
  - Note: newer scancode.io scanpipe runs on `mongo:4.4.7-windowsservercore` will use the Windows-specific docker_windows pipeline

| Name | Pipeline Name | Creation Date | Number of Discovered Packages | Number of Missing Discovered Package Resources | Number of Modified Discovered Package Resources | Number of Application Packages | Number of Ignored Empty Files | Number of Ignored Uninteresting Files | Number of Ignored Whiteout Files | Number of Resources with No Licenses | Number of Scanned Resources | Number of System Packages | Number of Resources with Unknown Licenses |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| [mongo-4.4.7-windowsservercore-25673dc6490e-run-2](https://github.com/aboutcode-org/scancode.io-reference-scans/blob/add-scan-stats-to-readme/docker/v21.8.2/mongo-4.4.7-windowsservercore-25673dc6490e-run-2_results-2021-08-17-18-06-21.xlsx.tar.gz) | docker_windows | 2021-08-16 | 14869 | 1 | 0 | 14872 | 22349 | 22025 | 10141 | 3838 | 75 | 0 | 10 |
| [mongo-4.4.7-windowsservercore-25673dc6490e](https://github.com/aboutcode-org/scancode.io-reference-scans/blob/add-scan-stats-to-readme/docker/v21.6.10/mongo-4.4.7-windowsservercore-25673dc6490e_results-2021-07-20-23-18-32.xlsx.gz) | docker | 2021-07-20 | 7250 | 0 | 0 | 7258 | 41656 | 0 | 10141 | 56880 | 395 | 0 | 21 |


- input: Windows `python:windowsservercore-ltsc2016` for windows/amd64
  - docker://python@sha256:1ad782fdc694d2fd57227532267e5fb45be9f7b8c637365b1d05d789f1894b0c
  - https://hub.docker.com/layers/python/library/python/windowsservercore-ltsc2016/images/sha256-1ad782fdc694d2fd57227532267e5fb45be9f7b8c637365b1d05d789f1894b0c?context=explore
  - scan files: docker/v21.6.10/windows-python* and docker/v21.8.2/windows-python*
  - Note: newer scancode.io scanpipe runs on `python:windowsservercore-ltsc2016` will use the Windows-specific docker_windows pipeline

| Name | Pipeline Name | Creation Date | Number of Discovered Packages | Number of Missing Discovered Package Resources | Number of Modified Discovered Package Resources | Number of Application Packages | Number of Ignored Empty Files | Number of Ignored Uninteresting Files | Number of Ignored Whiteout Files | Number of Resources with No Licenses | Number of Scanned Resources | Number of System Packages | Number of Resources with Unknown Licenses |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| [windows-python-1ad782fd-run-3](https://github.com/aboutcode-org/scancode.io-reference-scans/blob/add-scan-stats-to-readme/docker/v21.8.2/windows-python-1ad782fd-run-3_results-2021-08-17-23-09-36.xlsx.tar.gz) | docker_windows | 2021-08-17 | 23025 | 2 | 0 | 28308 | 30572 | 28615 | 13533 | 9435 | 278 | 0 | 60 |
| [windows-python-1ad782fd-run-2](https://github.com/aboutcode-org/scancode.io-reference-scans/blob/add-scan-stats-to-readme/docker/v21.8.2/windows-python-1ad782fd-run-2_results-2021-08-17-18-26-01.xlsx.tar.gz) | docker | 2021-08-03 | 23267 | 0 | 0 | 28580 | 52776 | 0 | 13533 | 79914 | 958 | 0 | 83 |
| [windows-python-1ad782fd](https://github.com/aboutcode-org/scancode.io-reference-scans/blob/add-scan-stats-to-readme/docker/v21.6.10/windows-python-1ad782fd_results-2021-07-21-09-25-35.xlsx.gz) | docker | 2021-07-20 | 10958 | 0 | 0 | 16282 | 52776 | 0 | 13533 | 92171 | 993 | 0 | 89 |


- input: Distroless Linux `distrolessdev/base:nonroot` for linux/amd64
  - docker://distrolessdev/base@sha256:f2ff292d5f916630cd0c841e45ede1f2ccd7436e17ab22548873a455c562a413
  - https://hub.docker.com/layers/distrolessdev/base/nonroot/images/sha256-f2ff292d5f916630cd0c841e45ede1f2ccd7436e17ab22548873a455c562a413?context=explore
  - scan files: docker/v21.6.10/distrolessdev* and docker/v21.8.2/distrolessdev*

| Name | Pipeline Name | Creation Date | Number of Discovered Packages | Number of Missing Discovered Package Resources | Number of Modified Discovered Package Resources | Number of Application Packages | Number of Ignored Empty Files | Number of Ignored Uninteresting Files | Number of Ignored Whiteout Files | Number of Resources with No Licenses | Number of Scanned Resources | Number of System Packages | Number of Resources with Unknown Licenses |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| [distrolessdev-run-2](https://github.com/aboutcode-org/scancode.io-reference-scans/blob/add-scan-stats-to-readme/docker/v21.8.2/distrolessdev-run-2_results-2021-08-17-18-12-25.xlsx.tar.gz) | docker | 2021-08-03 | 6 | 0 | 0 | 0 | 0 | 22 | 0 | 1165 | 30 | 0 | 3 |
| [distrolessdev](https://github.com/aboutcode-org/scancode.io-reference-scans/blob/add-scan-stats-to-readme/docker/v21.6.10/distrolessdev_results-2021-07-21-09-16-51.xlsx.gz) | docker | 2021-07-20 | 0 | 0 | 0 | 0 | 0 | 22 | 0 | 1165 | 30 | 0 | 3 |


- input: Alpine Linux `alpine/httpie:latest` for linux/amd64
  - docker://alpine/httpie@sha256:de5b79b4b9e399334103e69865ce5a4203280a3b28fa82f336a4a4814233c3f3
  - https://hub.docker.com/layers/alpine/httpie/latest/images/sha256-de5b79b4b9e399334103e69865ce5a4203280a3b28fa82f336a4a4814233c3f3?context=explore
  - scan files: docker/v21.6.10/alpine-httpie* and docker/v21.8.2/alpine-httpie*

| Name | Pipeline Name | Creation Date | Number of Discovered Packages | Number of Missing Discovered Package Resources | Number of Modified Discovered Package Resources | Number of Application Packages | Number of Ignored Empty Files | Number of Ignored Uninteresting Files | Number of Ignored Whiteout Files | Number of Resources with No Licenses | Number of Scanned Resources | Number of System Packages | Number of Resources with Unknown Licenses |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| [alpine-httpie-de5b79b4-run-2](https://github.com/aboutcode-org/scancode.io-reference-scans/blob/add-scan-stats-to-readme/docker/v21.8.2/alpine-httpie-de5b79b4-run-2_results-2021-08-17-18-12-17.xlsx.tar.gz) | docker | 2021-08-03 | 55 | 20 | 3 | 12 | 13 | 15 | 3 | 199 | 505 | 4323 | 8 |
| [alpine-httpie-de5b79b4](https://github.com/aboutcode-org/scancode.io-reference-scans/blob/add-scan-stats-to-readme/docker/v21.6.10/alpine-httpie-de5b79b4_results-2021-07-20-23-15-15.xlsx.gz) | docker | 2021-07-20 | 55 | 20 | 3 | 12 | 13 | 15 | 3 | 200 | 505 | 4322 | 8 |


## `root_filesystem` pipeline:
- input: Debian linux image
  - https://cloud.debian.org/images/cloud/buster/20210621-680/debian-10-genericcloud-amd64-20210621-680.qcow2
  - scan files: rootfs/v21.6.10/debian-qcow* and rootfs/v21.8.2/debian-qcow*

| Name | Pipeline Name | Creation Date | Number of Discovered Packages | Number of Missing Discovered Package Resources | Number of Modified Discovered Package Resources | Number of Application Packages | Number of Ignored Empty Files | Number of Ignored Uninteresting Files | Number of Ignored Whiteout Files | Number of Resources with No Licenses | Number of Scanned Resources | Number of System Packages | Number of Resources with Unknown Licenses |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| [debian-qcow-run-2](https://github.com/aboutcode-org/scancode.io-reference-scans/blob/add-scan-stats-to-readme/rootfs/v21.8.2/debian-qcow-run-2_results-2021-08-17-18-07-18.xlsx.tar.gz) | root_filesystems | 2021-08-03 | 303 | 59 | 1 | 0 | 6 | 1996 | 0 | 2928 | 1353 | 12615 | 29 |
| [debian-qcow](https://github.com/aboutcode-org/scancode.io-reference-scans/blob/add-scan-stats-to-readme/rootfs/v21.6.10/debian-qcow_results-2021-07-21-09-16-29.xlsx.gz) | root_filesystems | 2021-07-20 | 303 | 59 | 1 | 0 | 6 | 1996 | 0 | 3069 | 1953 | 11862 | 41 |
