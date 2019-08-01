from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
     return render_template('index.html')

@app.route('/image')
def load():
    data = []
    for number in range(100):
        num = str(number) + '.jpg'
        data.append(num)
    return render_template('loadimage.html',data=data)

if __name__ == "__main__":
    app.run()
