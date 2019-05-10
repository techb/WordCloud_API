from flask import Flask, send_file
from flask_restful import Resource, Api, reqparse
import json, os

# import and create our cloud generator
import CloudGenerate as CG
cg = CG.CloudGenerate()

app = Flask(__name__)
# treat a trailing slash as the same url, else /color works and /color/ 404's
# see: https://stackoverflow.com/questions/33241050/trailing-slash-triggers-404-in-flask-path-rule/33285603
app.url_map.strict_slashes = False

api = Api(app)
parser = reqparse.RequestParser()


class Colors(Resource):
	def __init__(self):
		pass

	def get(self, color_search=None):
		colors = cg.color_list()
		color_list = {'colors': []}
		for c in colors:
			# search for the color if user specified
			if color_search:
				if color_search.lower() in c.lower():
					color_list['colors'].append(c)

			else:
				color_list['colors'].append(c)

		if color_list['colors']:
			return color_list, 200
		else:
			return {
				'No Matching Colors': 'Color List Can Be Found: https://matplotlib.org/gallery/color/colormap_reference.html'
			}, 204 # No content


class MuhCloud(Resource):
	def __init__(self):
		pass

	def post(self):
		parser.add_argument('terms', location='json')
		parser.add_argument('color', location='json')
		args = parser.parse_args()

		img = cg.make_cloud(args['terms'], cm=args['color'])

		# Checking type for errors. In the try block, return a tuple.
		# If an error happend: ('error', <The Error Message>)
		if type(img) is tuple:
			return {img[0]: img[1]}
		else:
			return send_file(img, mimetype='image/jpeg')

# Add the endpoints
api.add_resource(Colors, '/colors', '/colors/<string:color_search>')
api.add_resource(MuhCloud, '/cloud')

# start in debug mode so we have live reloading on code changes
# port 10798 == ord('k') + ord('b')
app.run(port=10798, debug=True)