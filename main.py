from flask import Flask, request, render_template
import json
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    full_response = json.dumps(request.form.to_dict())
    token = request.form.get('Token', 'No token found!')
    return render_template('main.html', all=full_response, token=token)