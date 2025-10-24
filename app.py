from flask import Flask, render_template, request

app = Flask(__name__)

appointments = []

@app.route('/')
def home():
    return render_template('index.html', appointments=appointments)

@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        name = request.form['name']
        date = request.form['date']
        time = request.form['time']
        appointments.append({'name': name, 'date': date, 'time': time})
    return render_template('book.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
