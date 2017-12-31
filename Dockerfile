# Dockerfile to create a container able to build the OParl Specification
#
# MIT License
#
# Copyright (c) 2016, Stefan Graupner
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

FROM debian:latest
MAINTAINER Stefan Graupner <stefan.graupner@gmail.com>

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

RUN apt -y install python3 imagemagick zip tar bzip2

