from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib.cm
import numpy as np
import pandas as pd
from io import BytesIO
from PIL import Image


class CloudGenerate():
	def __init__(self):
		pass

	def make_cloud(self, terms, cm='twilight', w=800, h=800):
		try:
			# colormap ref: https://matplotlib.org/gallery/color/colormap_reference.html
			wc = WordCloud(width=w, height=h, colormap=cm)
			wc.generate(terms)
			# img = wc.to_image()
			img = wc.to_array()
			img = Image.fromarray(img)

			img_io = BytesIO()
			img.save(img_io, 'JPEG', quality=70)
			img_io.seek(0)
			return img_io

		except Exception as e:
			return 'error', str(e)

	def color_list(self):
		return matplotlib.cm.cmap_d.keys()