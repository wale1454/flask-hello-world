import os


from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    
    my_variable_value = os.getenv('TEST_APIKEY', 'default_value')

    
    return my_variable_value
