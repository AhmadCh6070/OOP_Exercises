#Task 1
from flask import Flask, jsonify
import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='Allahtallah1'
)


app = Flask(__name__)

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def check_airport(code):


@app.route('/prime_number/<int:num>')
def check_prime(num):
    prime_status = is_prime(num)
    response = {"Number": num,"isPrime": prime_status}

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

#Task 2



