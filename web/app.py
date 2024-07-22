from flask import Flask, render_template
import requests
import json

app = Flask(__name__, static_folder='static', template_folder='templates')


# To display the response of our spider on the web, we need to make a request to scrapyrt
@app.route('/')
def index():
    response = requests.get(
        url="http://127.0.0.1:9080/crawl.json?start_requests=true&spider_name=bestsellers"
    ).json()
    items = response.get('items')
    return render_template('index.html', games=items)


# When you go to the /show endpoint, this function will get executed, and it will
# look into the templates folder to find 'index.html'
# @app.route('/show')
# def show_template():
#     return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)  # debug = true so no need to restart flask if there are changes in the webpage
