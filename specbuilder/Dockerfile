FROM debian:latest
MAINTAINER Stefan Graunper <stefan.graupner@gmail.com>

RUN apt update -y
RUN apt upgrade -y

# recommended packages for pandoc + basic pdf export
RUN apt install --no-install-recommends -y \
  etoolbox \
  ghostscript \
  lmodern \
  graphviz \
  make \
  pandoc \
  pandoc-citeproc \
  texlive-fonts-recommended \
  texlive-generic-recommended \
  texlive-humanities \
  texlive-lang-german \
  texlive-latex-recommended \
  texlive-luatex \
  texlive-xetex

RUN apt install python3 imagemagick -y
