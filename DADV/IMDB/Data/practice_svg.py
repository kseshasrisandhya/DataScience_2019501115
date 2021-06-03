import plotly.express as px
import plotly.graph_objects as go
lis = [23, 80, 92, 62, 98, 7, 9, 56, 19, 68]
x = [i for i in range(1, 11)]


fig = go.Figure([go.Bar(x=x, y=lis)])
fig.write_html("bar_graph_practice_question.html")
