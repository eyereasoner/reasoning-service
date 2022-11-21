FROM semtech/mu-python-template:2.0.0-beta.1
LABEL maintainer="code@devloed.com"

ENV EYE_VERSION=22.1111.1734

RUN apt-get update && \
  apt-get install -y swi-prolog-nox curl && \
  curl -OL https://github.com/josd/eye/archive/refs/tags/v${EYE_VERSION}.zip && \
  unzip v${EYE_VERSION}.zip && \
  eye-${EYE_VERSION}/install.sh --prefix=/usr/local && \
  rm -rf v${EYE_VERSION}.zip eye-${EYE_VERSION}

