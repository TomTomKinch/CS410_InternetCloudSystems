from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

class Enter(MethodView):
	def get(movie):
		return render_template('enter.html')
	
	def post(movie):
		model = gbmodel.get_model()
		model.insert(request.form['title'], request.form['year'], 
			request.form['genre'], request.form['rating'], 
			request.form['name'], request.form['review'])
		return redirect(url_for('index'))
