import flask
from flask.views import MethodView
from index import Index
from reviews import Reviews
from enter import Enter

import gbmodel	#this sets the model

app = flask.Flask(__name__)

app.add_url_rule('/', 
		 view_func=Index.as_view('index'),
		 methods=["GET"])
app.add_url_rule('/reviews/',
		 view_func=Reviews.as_view('reviews'),
		 methods=["GET"])

app.add_url_rule('/enter/',
		 view_func=Enter.as_view('enter'),
		 methods=['GET', 'POST'])

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000, debug=True)
	
