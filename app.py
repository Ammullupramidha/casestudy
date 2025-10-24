from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        name = request.form.get('name')
        date = request.form.get('date')
        return f"Booking confirmed for {name} on {date}"
    return render_template('book.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
