from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

class Reviews(MethodView):
	def get(movie):
		model = gbmodel.get_model()
		
		#entries = [dict(title=row[0], year=row[1], genre=row[2], 
			#rating=row[3], name=row[4], 
			#the_date=row[5], review=row[6])
			#for row in model.select()]
 
		entries = [dict(title='Toy Story', year='1995', genre='Animated',
			rating='5', name='me', the_date= '7/18/2018', review='Great Film'), 
			dict(title='Avengers', year='2012', genre='Action',
			rating='5', name='Tom', the_date= '7/17/2018', review='Solid Film')
			]
		return render_template('reviews.html', entries=entries)
