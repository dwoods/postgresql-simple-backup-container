FROM centos/postgresql-96-centos7

USER root

RUN yum -y install epel-release && yum update -y
RUN yum -y install python \
    python-devel \
    python-pip \
    mercurial \ 
    && yum clean all

# Install dev cron
RUN pip install devcron==0.4

# Install tinys3
RUN pip install tinys3

WORKDIR /opt/app-root/src

ADD ./bin ./bin
RUN chmod -R 777 /opt/app-root/src

USER 1001

ENV BACKUP_DATA_DIR=/tmp BACKUP_KEEP=2 BACKUP_MINUTE=* BACKUP_HOUR=*

CMD ./bin/run.sh
