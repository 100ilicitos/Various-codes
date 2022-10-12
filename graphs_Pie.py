# Draw Pie Chart
# by Busyman.Inc

# pip install plotly

import plotly.express as plotly
import plotly.graph_objects as graph

plot = plotly.pie(labels=['D1','D2','D3'], values=[1,2,3])
plot.show()
