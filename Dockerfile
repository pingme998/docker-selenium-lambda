FROM public.ecr.aws/lambda/python:3.8
RUN pip install selenium -t /var/task && \
    yum install -y shadow-utils gzip tar wget && \
    /usr/sbin/useradd sbx_user1051 && \
    wget https://github.com/indigo-dc/udocker/releases/download/devel3_1.2.7/udocker-1.2.7.tar.gz && \
    tar zxvf udocker-1.2.7.tar.gz
ENV PATH /var/task/udocker:$PATH
USER sbx_user1051
RUN udocker install && \
    udocker pull selenium/standalone-chrome
COPY test.py ./
CMD [ "test.handler" ]
