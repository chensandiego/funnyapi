from flask import Flask,jsonify
import random

from quotes import funny_quotes

app = Flask(__name__)


@app.route("/api/funny")
def serve_funny_quote():
	quotes = funny_quotes()
	nr_of_quotes = len(quotes)
	select_quote = quotes[random.randint(0,nr_of_quotes -1)]
	return jsonify(select_quote)

if __name__ == '__main__':
	app.run(debug=True)