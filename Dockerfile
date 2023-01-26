FROM altlinux/base:p10
MAINTAINER Vladistav V. Tantsev <vlad.tancev@gmail.com>

RUN apt-get update -q -y

ENV USER deploy
RUN useradd -ms /bin/bash $USER
#USER deploy
WORKDIR /home/$USER

RUN apt-get install python3 pip -y

COPY requirments.txt .
RUN pip install -r requirments.txt

RUN apt-get install libGL mate-calc libxcbutil-icccm libxcbutil-image libxcb-render-util libxkbcommon-x11 libxcbutil-keysyms fonts-ttf-dejavu -y

COPY app app
COPY res res
COPY startup.sh .

CMD /bin/bash startup.sh