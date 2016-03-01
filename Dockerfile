FROM python:3.4.3

RUN apt-get update && \
    apt-get install -y lilypond imagemagick texlive

WORKDIR /abjad

COPY . /abjad

CMD ["bash"]