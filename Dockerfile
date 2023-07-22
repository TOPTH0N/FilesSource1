FROM TOPTH0N/FilesSource1:slim-buster

RUN git clone https://github.com/TOPTH0N/FilesSource1.git /root/zthon

WORKDIR /root/zthon

RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN npm i -g npm
RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/zthon/bin:$PATH"

CMD ["python3","-m","zthon"]
