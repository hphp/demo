
from pylab import *
import cv2

def basic():
    import pylab as pl
    import numpy as np
    t = np.linspace(0, 10, 20)
    s = sin(t)
    pl.plot(t, s)
    pl.show()
    print 'hello'
    pl.clf()
    t = np.linspace(0, 10, 20)
    s = (2*t)
    pl.figure()
    pl.plot(t, s)
    pl.show()

def subplot():
    import pylab as pl
    import numpy as np
    f = pl.figure()
    X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    #f.add_subplot(X, np.cos(X))
    #pl.show()

def ndarr():
    import pylab as pl
    import numpy as np

    X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    print X.shape, X
    C, S = np.cos(X), np.sin(X)

    pl.plot(X, C)
    pl.plot(X, S)

    pl.show()

def show_img_in_plot():
    img = cv2.imread("../cp.jpg")
    imshow(img)
    ginput(1,0.1) # draw the plot
    raw_input() # waiting for u to hold the plot.

def img_ratio():
    img = cv2.imread("../cp.jpg")
    imshow(img, aspect='equal')
    #gca().text(40,50,"helloworld")
    ginput(1,0.1) # draw the plot
    raw_input() # waiting for u to hold the plot.

def write_text_in_plot():
    img = cv2.imread("../cp.jpg")
    imshow(img)
    gca().text(40,50,"helloworld")
    ginput(1,0.1) # draw the plot
    raw_input() # waiting for u to hold the plot.

def write_text_in_figure():
    ##### HOW ???? ##########
    fig = figure()
    ax = fig.add_subplot()
    ax.text(40,50,"helloworld")
    ginput(1,0.1) # draw the plot
    raw_input() # waiting for u to hold the plot.
#show_img_in_plot()
#write_text_in_plot()
#img_ratio()
#write_text_in_figure()
#ndarr()
#subplot()
basic()
