from flask import Flask, make_response, request, render_template, url_for, redirect
# Las respuestas a las preguntas están en el readme.md
app = Flask(__name__)

@app.route('/set_cookie')
def set_cookie():
    response = make_response("Cookie creada")
    response.set_cookie('usuario', 'Jonatan', max_age=3600, httponly=True, secure=True)
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/')
def index():
    consent = request.cookies.get('cookies_consent')
    return render_template('consent.html', consent=consent)

@app.route('/privacy_policy')
def privacy_policy():
    return render_template('politica.html')

@app.route('/consent', methods=['GET', 'POST'])
def consent():
    if request.method == 'POST':
        option = request.form['option']
        response = make_response(redirect(url_for('set_cookie')))
        if option == 'accept_all':
            response.set_cookie('usuario', 'Jonatan')
            return redirect(url_for('set_cookie'))
        else:
            return redirect(url_for('reject'))
    return render_template('consent.html')

@app.route ('/reject')
def reject():
    return render_template('rechazo_cookies.html')


if __name__ == '__main__':
    app.run()
