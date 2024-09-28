from flask import Flask, render_template, request, redirect, url_for
import main_noend
from multiprocessing import Process
from time import sleep
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/play', methods=['GET', 'POST'])
def play():
    if request.method == 'POST':
        D2 = request.form.get('direction')
        if D2 is not None:
            write_f('input.txt', D2)
            sleep(3)

    text = read_f('print.txt')
    return render_template('flip.html', text=text)


def background_worker():

    def input_m(m):
        write_f('print.txt', m + '\n')
        while True:
            sleep(3)
            if os.path.exists('input.txt'):
                inp = read_f('input.txt')
                os.remove('input.txt')
                print(f'-------{inp}-----')
                return inp

    if os.path.exists('input.txt'):
        os.remove('input.txt')
    if os.path.exists('print.txt'):
        os.remove('print.txt')

    main_noend.flip(lambda msg: write_f('print.txt', msg + '\n'), input_m)


def read_f(file):
    with open(file, 'r') as f:
        return f.read()


def write_f(file, txt):
    with open(file, 'a') as f:
        f.write(txt)


if __name__ == '__main__':
    process = Process(target=background_worker)
    process.start()
    app.run(debug=True)
