
import pylab
from pylab import *
import cv2

def basic():
    import pylab as pl
    import numpy as np
    ###### basic figure show #######
    pl.figure(1)
    pl.plot([1,2,3])
    pl.figure(2)
    pl.plot([10,2,3])
    pl.show()
    ######## plot show numpy #####
    t = np.linspace(0, 10, 20)
    s = sin(t)
    pl.plot(t, s)
    pl.show()
    print 'hello'
    pl.clf()

    ######## plot show subplot #####
    t = np.linspace(0, 10, 20)
    s = (2*t)
    pl.figure() # return a figure , if nothing exist
    pl.plot(t, s)
    pl.plot(t, sin(s)) # add a subplot
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
    figure(frameon=False) 
    img = cv2.imread("../cp.jpg")
    imshow(img)
    #imshow(img, origin="lower") cant at this moment. , but the origin states the start point of the image.
    # one way
    #ginput(1,0.1) # draw the plot
    #raw_input() # waiting for u to hold the plot.
    # another
    #pylab.show()

def f_savefig()
    figure(frameon=False) 
    img = cv2.imread("../cp.jpg")
    imshow(img)
    # save
    #pylab.savefig("../fig.png")
    # save , and without margin
    pylab.savefig("../fig.png", bbox_inches='tight')
    #pylab.savefig("../fig.png", bbox_inches='tight', pad_inches=0) could not work
    #pylab.savefig("../fig.png", bbox_inches='tight', pad_inches=10) could not work and very slow

def imshow_extent():
    import matplotlib.pyplot as plt
    import numpy as np

    grid = np.random.random((10,10))

    fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, figsize=(6,10))

    ax1.imshow(grid, extent=[0,100,0,1])
    ax1.set_title('Default')

    ax2.imshow(grid, extent=[0,100,0,1], aspect='auto')
    ax2.set_title('Auto-scaled Aspect')

    ax3.imshow(grid, extent=[0,100,0,1], aspect=100)
    ax3.set_title('Manually Set Aspect')

    plt.tight_layout()
    plt.show()

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
#basic()
#imshow_extent()
#f_savefig()
