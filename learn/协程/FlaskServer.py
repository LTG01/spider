from flask import Flask ,render_template
import time
#实例华一个app
app = Flask(__name__)

@app.route('/ltg00')
def index_1():
    time.sleep(1)
    return render_template('test.html')

@app.route('/ltg01')
def index_2():
    time.sleep(1)
    return render_template('test.html')


@app.route('/ltg02')
def index_3():
    time.sleep(1)
    return render_template('test.html')


if __name__ == '__main__':

    app.run(debug=True)
    pass