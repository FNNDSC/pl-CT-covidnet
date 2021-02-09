FROM alpine:latest as download
# these models aren't all that big, but we can keep the multi-stage build for good measure

WORKDIR /tmp
ADD https://fnndsc.childrens.harvard.edu/COVID-Net/models/20200716/COVID-Net-CT-1-L.tar.gz /tmp/models.tar.gz
RUN ["tar", "xf", "models.tar.gz"]

FROM docker.io/fnndsc/tensorflow:1.15.3

ENV DEBIAN_FRONTEND=noninteractive

# install python dependencies using apt
# for support on non-x86_64 architectures such as PowerPC
RUN apt-get update \
    && apt-get install -y python3-opencv python3-matplotlib \
    && rm -rf /var/lib/apt/lists/*

COPY --from=download /tmp/COVID-Net-CT-1-L/ /usr/local/lib/covidnet/COVID-Net-CT-1-L/

WORKDIR /usr/local/src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN pip install .

CMD ["ct_covidnet", "--help"]
