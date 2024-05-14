from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Define a function to connect to the database
def connect_db():
  conn = sqlite3.connect('address_book.db')
  return conn

# Define a function to save address to database
def save_address(address):
  conn = connect_db()
  cursor = conn.cursor()
  cursor.execute("INSERT INTO addresses (address) VALUES (?)", (address,))
  conn.commit()
  conn.close()

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/save', methods=['POST'])
def save():
  address = request.form['address']
  save_address(address)
  return "Address saved successfully!"

if __name__ == '__main__':
  app.run(debug=True)
