import numpy as np

from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool

album = ["10 Day", "Acid Rap", "Coloring Book"]
song = ["Track 1", "Track 2", "Track 3", "Track 4", "Track 5", "Track 6", "Track 7", "Track 8", "Track 9", "Track 10", "Track 11", "Track 12", "Track 13", "Track 14"]
label = ["Point 1", "Point 2", "Point 3", "Point 4", "Point 5", "Point 6", "Point 7", "Point 8", "Point 9", "Track 10", "Track 11", "Track 12", "Track 13", "Track 14"]
x = [4, 3, 5, 10, 11, 4, 2, 12]
y = [3, 2, 2, 2, 2, 2, 1, 1]
radii = [.1, .2, .1, 3.0, .1, .4, .2, 1.9]
colors = ['#206091', '#761F7F', '#85277E', '#A93A7C', '#B03E7B', '#B7427B', '#F8476B', '#FA9768']

TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,undo,redo,reset,tap,save,box_select"

p = figure(tools=TOOLS, title="Smoke", y_range=album, x_range=song, plot_width=1200)
p.xgrid.grid_line_color = None

p.scatter(x, y, radius=radii, fill_color=colors, line_color=None)

hover =p.select(dict(type=HoverTool))
hover.tooltips = OrderedDict([
    ("(xx,yy)", "(@x, @y)"),
    ("label", "@label"),
])

output_file("color_scatter.html", title="color_scatter.py example")

show(p)
