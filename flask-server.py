from flask import Flask
import time

app = Flask(__name__)


@app.route("/")
def main():
    cur_time = str(time.time())
    a = int(time.time())**10
    return cur_time


if __name__ == '__main__':
    app.run()
