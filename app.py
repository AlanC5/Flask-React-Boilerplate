from flask import Flask, render_template

app = Flask(__name__, static_folder = "static", template_folder = "static/dist")
app.config['SECRET_KEY'] = 'secret!'

@app.route('/')
def index():
    sensors =  { 
        'temperature': 80,
        'distance': 10
    }

    return render_template('index.html', sensors = sensors)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090, debug=True)
