from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/get_address', methods=['POST'])
def get_address():
  address = request.form['address']
  # Process or display the address here (without saving)
  return f"You entered: {address}"

if __name__ == '__main__':
  app.run(debug=True)
