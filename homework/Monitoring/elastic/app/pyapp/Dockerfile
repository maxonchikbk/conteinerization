FROM python:3.9
RUN pip install elastic-apm[flask] flask
COPY main.py /tmp
WORKDIR /tmp
CMD ["python","main.py"]