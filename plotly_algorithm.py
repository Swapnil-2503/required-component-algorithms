import plotly.graph_objects as go

a=[] ## time of updating x axis
b=[]   ## updating  values
a.append (10)
b.append (20)
# Create a line graph
fig = go.Figure(data=go.Scatter(x=a, y=b))

# Update the layout
fig.update_layout(title='Line Graph', xaxis_title='X', yaxis_title='Y')


# Show the plot
fig.show()