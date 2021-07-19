## my_test_flask_app.py

import sentry_sdk
from flask import Flask
from flask import Flask, render_template
from raven.contrib.flask import Sentry
from sentry_sdk.integrations.flask import FlaskIntegration

# дополнительная секция для мониторинга производительности
sentry_sdk.init(
   dsn='http://1d82f51488b3488cbd767f3af6414791@localhost:9000/3',
   integrations=[FlaskIntegration()],


   traces_sample_rate=1.0
)
app = Flask(__name__)

# секция для отправки ошибок в Sentry
sentry = Sentry(app, dsn='http://1d82f51488b3488cbd767f3af6414791@localhost:9000/3')

@app.route('/')
def hello_error():

   0 / 1 #ZeroDivisionError to be sent to sentry
   return render_template("hello_world.html")

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port='4567')

