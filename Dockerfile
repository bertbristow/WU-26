FROM markadams/chromium-xvfb

RUN apt-get update && apt-get install -y \
    python python-pip curl unzip libgconf-2-4

RUN pip install pytest selenium==3.4.3

ENV CHROMEDRIVER_VERSION 2.29
ENV CHROMEDRIVER_SHA256 bb2cf08f2c213f061d6fbca9658fc44a367c1ba7e40b3ee1e3ae437be0f901c2

RUN curl -SLO "https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip" \
  && echo "$CHROMEDRIVER_SHA256  chromedriver_linux64.zip" | sha256sum -c - \
  && unzip "chromedriver_linux64.zip" -d /usr/local/bin \
  && rm "chromedriver_linux64.zip"
RUN apt-get install -y wget
#=========
# Firefox
#=========
ARG FIREFOX_VERSION=55.0.3
RUN wget --no-verbose -O /tmp/firefox-55.0.3.tar.bz2 https://download-installer.cdn.mozilla.net/pub/firefox/releases/55.0.3/linux-x86_64/en-US/firefox-55.0.3.tar.bz2 && \
    tar -C /opt -xjf /tmp/firefox-55.0.3.tar.bz2 && \
    mv /opt/firefox /opt/firefox-$FIREFOX_VERSION && \
    ln -fs /opt/firefox-$FIREFOX_VERSION/firefox /usr/bin/firefox

#============
# GeckoDriver
#============
ARG GECKODRIVER_VERSION=0.18.0
RUN wget --no-verbose -O /tmp/geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v$GECKODRIVER_VERSION/geckodriver-v$GECKODRIVER_VERSION-linux64.tar.gz && \
    rm -rf /opt/geckodriver && \
    tar -C /opt -zxf /tmp/geckodriver.tar.gz && \
    rm /tmp/geckodriver.tar.gz && \
    mv /opt/geckodriver /opt/geckodriver-$GECKODRIVER_VERSION && \
    chmod 755 /opt/geckodriver-$GECKODRIVER_VERSION && \
    ln -fs /opt/geckodriver-$GECKODRIVER_VERSION /usr/bin/geckodriver

RUN pip install pyvirtualdisplay

COPY . /src/app
RUN cd /src/app && \
    pip install -r requirements.txt

WORKDIR /src/app