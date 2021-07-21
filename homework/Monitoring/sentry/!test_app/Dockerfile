FROM python:3.9
WORKDIR /tmp
RUN pip install flask
RUN pip install raven
RUN pip install --upgrade 'sentry-sdk[flask]'
RUN pip install elastic-apm[flask] flask
COPY my_test_flask_app.py /tmp
COPY ./templates /tmp/templates
CMD ["python","my_test_flask_app.py"]