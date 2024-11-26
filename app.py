from flask import Flask, make_response, request, render_template, url_for, redirect

app = Flask(__name__)

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
        response = make_response(redirect(url_for('get_cookies')))
        if option == 'accept_all':
            response.set_cookie('usuario', 'Jonatan')
        return url_for('set_cookie', option=option)
    return render_template('consent.html')

if __name__ == '__main__':
    app.run()
