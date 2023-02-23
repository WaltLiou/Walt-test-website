# https://www.youtube.com/watch?v=yBDHkveJUf4&t=11097s
print("Hello World")

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
  return render_template('home.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

# htmldog.com   <=HTML語法
# excalidraw.com  <=白板
# unsplash.com    <=找圖片
# lorem text generator  <=文本生成器