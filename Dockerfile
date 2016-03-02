FROM python:3.4.3

ENV LILYPOND_VERSION 2.19.37

RUN apt-get update \
    && apt-get install -y \
        build-essential \
        graphviz \
        imagemagick \
        texlive \
        wget

RUN cd / \
    && wget http://download.linuxaudio.org/lilypond/binaries/linux-64/lilypond-$LILYPOND_VERSION-1.linux-64.sh \
    && chmod +x lilypond-$LILYPOND_VERSION-1.linux-64.sh \
    && ./lilypond-$LILYPOND_VERSION-1.linux-64.sh --batch \
    && rm lilypond-$LILYPOND_VERSION-1.linux-64.sh \
    && lilypond -v

WORKDIR /abjad

COPY . /abjad

CMD ["bash"]
