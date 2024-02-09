from flask import Flask, render_template
from modules.pcinfo import pcinfo_blueprint
from modules.networkinfo import networkinfo_blueprint

app = Flask(__name__)
app.register_blueprint(pcinfo_blueprint, url_prefix='/pcinfo')
app.register_blueprint(networkinfo_blueprint, url_prefix='/netinfo')


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
