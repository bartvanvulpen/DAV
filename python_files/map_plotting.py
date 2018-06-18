import pandas as pd
import numpy as np
import matplotlib as plt
import gmplot
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

import zipfile
import sys
from pandas import ExcelWriter
import re
from pandas import ExcelFile
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, GMapOptions
from bokeh.plotting import gmap



print("Starting reading data...")
data = pd.read_excel('datasets/MASTER_DATASET.xlsx')
print("Read data, now plotting map...")

lat = data['latitude']
lon = data['longitude']


# Create heatmap
heatmap, xedges, yedges = np.histogram2d(lat, lon, bins=(64,64))
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

# Plot heatmap
plt.clf()
plt.title('Pythonspot.com heatmap example')
plt.ylabel('y')
plt.xlabel('x')
plt.imshow(heatmap, extent=extent)
plt.show()
print("showing plot")
