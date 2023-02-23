# https://www.youtube.com/watch?v=yBDHkveJUf4&t=11097s
print("Hello World")

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
  return "Hello Worldsss"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)