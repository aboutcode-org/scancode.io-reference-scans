# scancode.io-reference-scans
A set of reference scans with ScanCode.io updated with each new release to track quality and performance progress over time.

On 2021-07-20
------------------

Scans ScanCode.io v21.6.10 (using ScanCode Toolkit v21.6.7

## `docker` pipeline:
  - input: Debian Linux `debian:buster-slim` for linux/amd64
    - docker://debian@sha256:0fe071e7b4811869579bef3f308096be22f672aa52f121b62c6c401f18abb97c
    - scan files: docker/debian-buster*
  - input: CentOS Linux `elasticsearch:7.13.3` for linux/amd64
    - docker://elasticsearch@sha256:e54cc1adf707472e8d4b916227f536bd486198d83aaaf5a30459dd6b966cca03
    - https://hub.docker.com/layers/elasticsearch/library/elasticsearch/7.13.3/images/sha256-e54cc1adf707472e8d4b916227f536bd486198d83aaaf5a30459dd6b966cca03?context=explore 
    - scan files: docker/elasticsearch*
  - input: Alpine Linux `nginx:1.20.1-alpine-perl` for linux/amd64
    - docker://nginx@sha256:e8984445b0175f26a07e78461dfb8dff90867ed8f7c3041b1fb3088fad942022
    - https://hub.docker.com/layers/nginx/library/nginx/1.20.1-alpine-perl/images/sha256-e8984445b0175f26a07e78461dfb8dff90867ed8f7c3041b1fb3088fad942022?context=explore
    - scan files: docker/nginx*
  - input: Windows `mongo:4.4.7-windowsservercore` for windows/amd64
    - docker://mongo@sha256:73dc6490e1159b56631bbcbd87e5cade415596dc75c26186860761cdb0ceab2a
    - https://hub.docker.com/layers/mongo/library/mongo/4.4.7-windowsservercore/images/sha256-73dc6490e1159b56631bbcbd87e5cade415596dc75c26186860761cdb0ceab2a?context=explore
    - scan files: docker/windows-mongo*
  - input: Windows `python:windowsservercore-ltsc2016` for windows/amd64
    - docker://python@sha256:1ad782fdc694d2fd57227532267e5fb45be9f7b8c637365b1d05d789f1894b0c
    - https://hub.docker.com/layers/python/library/python/windowsservercore-ltsc2016/images/sha256-1ad782fdc694d2fd57227532267e5fb45be9f7b8c637365b1d05d789f1894b0c?context=explore
    - scan files: docker/windows-python*
  - input: Distroless Linux `distrolessdev/base:nonroot` for linux/amd64
    - docker://distrolessdev/base@sha256:f2ff292d5f916630cd0c841e45ede1f2ccd7436e17ab22548873a455c562a413
    - https://hub.docker.com/layers/distrolessdev/base/nonroot/images/sha256-f2ff292d5f916630cd0c841e45ede1f2ccd7436e17ab22548873a455c562a413?context=explore
    - scan files: docker/distrolessdev*
  - input: Alpine Linux `alpine/httpie:latest` for linux/amd64
    - docker://alpine/httpie@sha256:de5b79b4b9e399334103e69865ce5a4203280a3b28fa82f336a4a4814233c3f3
    - https://hub.docker.com/layers/alpine/httpie/latest/images/sha256-de5b79b4b9e399334103e69865ce5a4203280a3b28fa82f336a4a4814233c3f3?context=explore
    - scan files: docker/alpine-httpie*

## `root_filesystem` pipeline:
  - input: Debian linux image
    - https://cloud.debian.org/images/cloud/buster/20210621-680/debian-10-genericcloud-amd64-20210621-680.qcow2
    - scan files: rootfs/debian-qcow*
