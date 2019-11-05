# FROM表示该镜像(image)继承自官方的 python 镜像(image)，
# 冒号表示标签，这里标签是3.6-alphine，即3.6-alphine版本的python
# alphine是Linux的一个发行版
FROM python:3.6-alphine

# 设置名为 PYTHONUNBUFFERED 的环境变量，并且设置值为1
ENV PYTHONUNBUFFERED 1

# 将当前目录下的文件（.dockerignore排除的文件外的所有文件）拷贝到到image下的/app目录
# 本项目中.表示的是mysite/compose/production/django的django这个目录
COPY . /app

# 将requirement.txt目录添加到/app目录
COPY ../../../requirements.txt /app

# 指定工作目录为/app, 此后，在基于此镜像启动的docker容器执行的命令都会以这个目录为当前工作目录
WORKDIR /app

# 在/app目录下，使用pip install 命令安装requirements.txt文件
# -i 指定pypi源为豆瓣
RUN pip3 install -r requirements.txt -i https://pypi.douban.com/simple

# 对外暴露端口
EXPOSE 80 8080 8000 5000


