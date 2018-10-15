import matplotlib.pyplot as plot

def graph(x, y):
    plot.plot(x,y)
    plot.axis([0,10,0,10])
    return plot.show()