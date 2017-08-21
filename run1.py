from flask import (Flask,
                   render_template,
                   request,
                   session,
                   escape,
                   url_for,
                   redirect
                   )

from Settings_app import key

app = Flask(__name__)
app.secret_key = key


@app.route('/', methods=['GET', 'POST'])
def signin():
    return render_template('signin.html')


@app.route('/operator', methods=['GET', 'POST'])
def operator():
    return render_template('operator.html')\

@app.route('/engineer', methods=['GET', 'POST'])
def engineer():
    return render_template('engineer.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    return render_template('admin.html')



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True)