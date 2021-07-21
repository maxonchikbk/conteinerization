## my_test_flask_app.py

import sentry_sdk
from flask import Flask
from flask import Flask, render_template
from raven.contrib.flask import Sentry
from sentry_sdk.integrations.flask import FlaskIntegration
from elasticapm.contrib.flask import ElasticAPM

app = Flask(__name__)
app.config['ELASTIC_APM'] = {
          'SERVICE_NAME': 'ZeroApp',
          'SECRET_TOKEN': '',
          'SERVER_URL': 'http://host.docker.internal:8200'
}
apm = ElasticAPM(app)
# дополнительная секция для мониторинга производительности

sentry_sdk.init(
   dsn='http://e5d588985568478c9510406161004864@host.docker.internal:9000/2',
   integrations=[FlaskIntegration()],
   traces_sample_rate=1.0
)
# секция для отправки ошибок в Sentry
sentry = Sentry(app, dsn='http://e5d588985568478c9510406161004864@host.docker.internal:9000/2')

@app.route('/')
def hello_error():

   1 / 0 #ZeroDivisionError to be sent to sentry
   return render_template("hello_world.html")

if __name__ == '__main__':
   app.run(host='0.0.0.0', port='4567')

