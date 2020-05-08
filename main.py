from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    token = request.form.get('Token', 'No token found!')
    return render_template('main.html', all=request.form, token=token)