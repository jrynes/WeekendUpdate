# Refer to the repo below for any updates to the base Dockerfile shown below:
# https://github.com/umihico/docker-selenium-lambda
FROM public.ecr.aws/lambda/python@sha256:e58821c4a48a784602cdbc8d0dee45211f7348c753b17f756595a3a7172ebd16 as build
RUN yum install -y unzip && \
    curl -Lo "/tmp/chromedriver.zip" "https://chromedriver.storage.googleapis.com/104.0.5112.79/chromedriver_linux64.zip" && \
    curl -Lo "/tmp/chrome-linux.zip" "https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Linux_x64%2F1012728%2Fchrome-linux.zip?alt=media" && \
    unzip /tmp/chromedriver.zip -d /opt/ && \
    unzip /tmp/chrome-linux.zip -d /opt/

FROM public.ecr.aws/lambda/python@sha256:e58821c4a48a784602cdbc8d0dee45211f7348c753b17f756595a3a7172ebd16
RUN yum install atk cups-libs gtk3 libXcomposite alsa-lib \
    libXcursor libXdamage libXext libXi libXrandr libXScrnSaver \
    libXtst pango at-spi2-atk libXt xorg-x11-server-Xvfb \
    xorg-x11-xauth dbus-glib dbus-glib-devel -y
RUN pip install selenium
COPY --from=build /opt/chrome-linux /opt/chrome
COPY --from=build /opt/chromedriver /opt/
COPY app.py ./
COPY config.py ./
#Create a bin folder in the Docker image
RUN mkdir bin
CMD [ "app.lambda_handler" ]