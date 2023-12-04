FROM semtech/mu-python-template:2.0.0-beta.1
LABEL maintainer="code@devloed.com"
ENV EYE_VERSION=8.7.5
LABEL reasoner="https://github.com/eyereasoner/eye/releases/tag/v${EYE_VERSION}"

RUN apt-get update && \
  apt-get install -y swi-prolog-nox curl && \
  curl -OL https://github.com/eyereasoner/eye/archive/refs/tags/v${EYE_VERSION}.zip && \
  unzip v${EYE_VERSION}.zip && \
  eye-${EYE_VERSION}/install.sh --prefix=/usr/local && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf v${EYE_VERSION}.zip eye-${EYE_VERSION}

RUN echo 'timeout = os.getenv("TIMEOUT", 300)' >> /gunicorn_conf.py
