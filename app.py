from flask import Flask, send_from_directory
from flask import Flask, render_template, request, redirect, url_for
from flask import Flask, send_from_directory
app = Flask(__name__)
app.secret_key = 'secret_key'
app = Flask(__name__, static_folder='static')

@app.route('/static/<path:filename>')
def custom_static(filename):
    return send_from_directory('static', filename, mimetype='application/octet-stream')  


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<page>.html')
def other_pages(page):
    try:
        return render_template(f'{page}.html')
    except Exception as e:
        return f"Error: {str(e)}", 404

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form['user_input']
    with open('data/input_data.txt', 'a') as f:
        f.write(user_input + '\n')
    return redirect(url_for('thanks'))

@app.route('/thanks')
def thanks():
    return send_from_directory('templates', 'thanks.html')




if __name__ == "__main__":
    app.run(debug=True)
