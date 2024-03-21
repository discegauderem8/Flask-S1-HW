from flask import Flask, request, redirect, make_response, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    response = make_response(redirect(url_for('welcome')))
    response.set_cookie('user_data', f'{name},{email}')
    return response


@app.route('/welcome')
def welcome():
    user_data = request.cookies.get('user_data')
    if user_data:
        name, _ = user_data.split(',')
        return render_template('welcome.html', name=name)
    else:
        return redirect(url_for('index'))


@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('index')))
    response.set_cookie('user_data', '', max_age=0)
    return response


if __name__ == '__main__':
    app.run(debug=True)
