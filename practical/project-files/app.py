from flask import Flask, render_template
from modules.pcinfo import pcinfo_blueprint

app = Flask(__name__)
app.register_blueprint(pcinfo_blueprint, url_prefix='/pcinfo')


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
