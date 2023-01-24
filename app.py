from flask import Flask, render_template, request, flash

from topsis import topsis
from send_mail import send_mail

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/", methods=('GET', 'POST'))
def main():
    if request.method == "POST":

        file = request.files['file']
        weights = request.form['weights']
        impacts = request.form['impacts']
        email_id = request.form['email_id']

        file_name = 'data.csv'
        file.save(file_name)

        try:
            data = topsis(file_name, weights, impacts)
        except Exception as e:
            flash(e)
            return render_template('index.html')

        if email_id:
            send_mail(email_id, data.to_html())

        return render_template('output.html', table = data.to_html())

    return render_template('index.html')
