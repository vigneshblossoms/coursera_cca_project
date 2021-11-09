FROM python:3.7.3-stretch
WORKDIR /app
COPY . main.py /app/
RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]