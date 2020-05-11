from flask import render_template
from flask.views import MethodView

import gbmodel

class Index(MethodView):
	def get(movie):
		return render_template('index.html')

	def get(movie):
		model = gbmodel.get_model()
		entries = [dict(title=row[0], year=row[1], genre=row[2], 
			rating=row[3], name=row[4], 
			the_date=row[5], review=row[6])
			for row in model.select()]
		return render_template('index.html', entries=entries)
	
