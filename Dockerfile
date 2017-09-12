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
RUN wget https://ftp.mozilla.org/pub/mozilla.org/firefox/releases/40.0.3/linux-x86_64/en-US/firefox-40.0.3.tar.bz2
RUN tar -xjvf firefox-40.0.3.tar.bz2
RUN mv firefox /opt/firefox
RUN ln -sf /opt/firefox/firefox /usr/bin/firefox
RUN pip install pyvirtualdisplay

COPY . /src/app
RUN cd /src/app && \
    pip install -r requirements.txt

WORKDIR /src/app
