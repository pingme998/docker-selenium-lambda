FROM public.ecr.aws/lambda/python:3.8 as build
RUN mkdir -p /opt/bin/ && \
    mkdir -p /tmp/downloads && \
    yum install -y unzip && \
    curl -SL https://chromedriver.storage.googleapis.com/$(curl https://chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip > /tmp/downloads/chromedriver.zip && \
    unzip /tmp/downloads/chromedriver.zip -d /opt/bin/

FROM public.ecr.aws/lambda/python:3.8
RUN yum install -y shadow-utils && \
    mkdir -p /tmp/home && \
    /usr/sbin/useradd sbx_user1051 && \
    /usr/sbin/usermod -d /tmp/home sbx_user1051
COPY google-chrome.repo /etc/yum.repos.d/
RUN yum install -y --enablerepo=google-chrome google-chrome-stable
RUN chmod +x /usr/bin/google-chrome
RUN chown -R sbx_user1051 /tmp/home
RUN pip install selenium -t /var/task
RUN yum install -y xorg-x11-server-Xvfb && \
    pip install xvfbwrapper -t /var/task

USER sbx_user1051
# RUN chown -R sbx_user1051 /usr/bin/google-chrome
COPY --from=build /opt/bin/chromedriver /opt/bin/
# RUN chown -R sbx_user1051 /opt/bin/chromedriver
COPY test.py ./
CMD [ "test.handler" ]
