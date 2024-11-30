from flask import Flask

app = Flask(__name__)  # Creates a Flask application instance.

@app.route('/')  # Defines a route for the root URL ('/').
def hello_world():  # Function that handles requests to the root URL.
    return 'Hello, World!'  # Returns a response.

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)