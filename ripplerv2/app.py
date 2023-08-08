from flask import Flask, render_template, request 
import random
import time 
from timeit import default_timer as timer

app = Flask(__name__,template_folder="templates")

start = 0 
end = 0 

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/anim.html')
def animation():
        global random_key
        random_key = random.randint(1,4)
        time.sleep(2)
        global start 
        start = timer()
        if random_key == 1:
            return render_template('anim1.html')
        if random_key == 2:
            return render_template('anim2.html')
        if random_key == 3:
            return render_template('anim3.html')
        if random_key == 4:
            return render_template('anim4.html')

@app.route('/results1.html')
def results1():
    end = timer()
    return render_template('results1.html', stop_time = round(end-start, 2), rkey = random_key)

@app.route('/results2.html')
def results2():
    end = timer()
    return render_template('results2.html', stop_time = round(end-start, 2), rkey = random_key)

@app.route('/results3.html')
def results3():
    end = timer()
    return render_template('results3.html', stop_time = round(end-start, 2), rkey = random_key)

@app.route('/results4.html')
def results4():
    end = timer()
    return render_template('results4.html', stop_time = round(end-start, 2), rkey = random_key)

@app.route('/anim1.html')
def animation1():
    global start 
    start = timer()
    return render_template('anim1.html')

@app.route('/anim2.html')
def animation2():
    global start 
    start = timer()
    return render_template('anim2.html')

@app.route('/anim3.html')
def animation3():
    global start 
    start = timer()
    return render_template('anim3.html')

@app.route('/anim4.html')
def animation4():
    global start 
    start = timer()
    return render_template('anim4.html')

if __name__ == "__main__":
    app.run(debug=True)