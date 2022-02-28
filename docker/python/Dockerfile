FROM  nvidia/cuda:11.4.0-cudnn8-devel-ubuntu20.04

ENV NOTO_DIR /usr/share/fonts/opentype/notosans

##ミラーを使うなどをする人が多いので入れてましたが、そこまで早くもならず無用だったので外しています。
# RUN sed -i.bak -r 's@http://(jp.)?archive.ubuntu.com/ubuntu/@http://ftp.jaist.ac.jp/pub/Linux/ubuntu/@g' /etc/apt/sources.list


## aptに時間がかなりかかるので、パッケージを絞っています。
RUN apt update \
    && apt install -y \
    wget \
    bzip2 \
    # ca-certificates \
    # libglib2.0-0 \
    # libxext6 \
    # libsm6 \
    # libxrender1 \
    git \
    # mercurial \
    # subversion \
    # zsh \
    # openssh-server \
    # gcc \
    # g++ \
    # libatlas-base-dev \
    # libboost-dev \
    # libboost-system-dev \
    # libboost-filesystem-dev \
    curl \
    # make \
    unzip \
    vim \
    # ffmpeg \
    mecab \
    libmecab-dev \
    mecab-ipadic-utf8 \
    file \
    xz-utils \
    sudo \
    python3 \
    python3-pip


RUN mkdir -p ${NOTO_DIR} &&\
  wget -q https://noto-website-2.storage.googleapis.com/pkgs/NotoSansCJKjp-hinted.zip -O noto.zip &&\
  unzip ./noto.zip -d ${NOTO_DIR}/ &&\
  chmod a+r ${NOTO_DIR}/NotoSans* &&\
  rm ./noto.zip

# remove cache files
RUN apt-get autoremove -y && apt-get clean && \
  rm -rf /usr/local/src/*

RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git \
    && cd mecab-ipadic-neologd \
    && bin/install-mecab-ipadic-neologd -n -y

COPY requirements.txt /tmp/

RUN pip install --no-cache-dir -U pip setuptools wheel \
    && pip install --no-cache-dir -r /tmp/requirements.txt

# nodejsの導入
RUN curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash - \
    && sudo apt-get install -y nodejs

# ## JupyterLabの拡張機能

# 変数や行列の中身を確認
RUN jupyter labextension install @lckr/jupyterlab_variableinspector@3.0.7

# 自動整形
RUN pip install autopep8 \
    && pip install jupyterlab_code_formatter \
    && jupyter labextension install @ryantam626/jupyterlab_code_formatter \
    && jupyter serverextension enable --py jupyterlab_code_formatter

# jupyter の config ファイルの作成
RUN mkdir /mlws && echo "c.NotebookApp.notebook_dir = '/mlws' \n" | tee -a ${HOME}/.jupyter/jupyter_notebook_config.py


RUN mkdir -p /usr/share/fonts/truetype/IPAexfont
RUN curl -L  "https://moji.or.jp/wp-content/ipafont/IPAexfont/IPAexfont00401.zip" > font.zip
RUN unzip font.zip
RUN cp IPAexfont00401/ipaexg.ttf /usr/share/fonts/truetype/IPAexfont/ipaexg.ttf
RUN echo "font.family : IPAexGothic" >>  /usr/local/lib/python3.8/dist-packages/matplotlib/mpl-data/matplotlibrc

EXPOSE 8888

CMD ["python3","-m","jupyter", "lab", "--ip=0.0.0.0", "--port=8888","--allow-root","--NotebookApp.token=''"]