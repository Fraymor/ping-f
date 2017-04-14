from flask import Flask
import os

app = Flask(__name__)

def fib_func(n):
fib1 = 1
fib2 = 1
i = 2
while i <= n:
fib_sum = fib2 + fib1
fib1 = fib2
fib2 = fib_sum
i += 1
return fib_sum

@app.route('/ping', methods=['GET'])
def ping():
response = os.system("ping -w 1 google.com")
return '%d' % response

@app.route('/<n>', methods=['GET'])
def fib(n):
return '%d' % fib_func(n)

if __name__ == '__main__':
app.run(debug=True,host='0.0.0.0')