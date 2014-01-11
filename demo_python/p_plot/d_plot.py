# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

def plot_arr():
    #
    print

def basic_plot_text(rt=False, plenty=1):
    fig = plt.figure()
    #fig.suptitle('bold figure suptitle', fontsize=14, fontweight='bold')

    ax = fig.add_subplot(111)
    #fig.subplots_adjust(top=0.85)
    #ax.set_title('axes title')

    #ax.set_xlabel('xlabel')
    #ax.set_ylabel('ylabel')

    print plenty
    for i in range(plenty):
        y = (i+1)*10
        x = 3
        ax.text(x, y, 'boxed italics text in data coords', style='italic',
            bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})

    ax.axis([0, 100, 0, (plenty+1)*10])

    if rt == True:
        return fig

    plt.show()

def plot_text(rt=False, plenty=1):
    w, h, dpi = (9, 12, 100)
    fig = plt.figure(figsize=(w, h), dpi=dpi)
    #fig.suptitle('bold figure suptitle', fontsize=14, fontweight='bold')

    ax = fig.add_subplot(111)
    #fig.subplots_adjust(top=0.85)
    #ax.set_title('axes title')

    #ax.set_xlabel('xlabel')
    #ax.set_ylabel('ylabel')

    print plenty
    total_height = h * dpi
    fontsize = total_height / (plenty+1)
    fontsize *= 1.1
    fontsize = int(fontsize)
    print fontsize
    for i in range(plenty):
        y = (i+1)*fontsize
        x = 3
        ax.text(x, y, 'boxed italics text in data coords', style='italic', fontsize=fontsize)

    ax.axis([0, 100, 0, (plenty+1)*fontsize])

    if rt == True:
        return fig

    plt.show()

def savefig():
    fig = basic_plot_text(rt=True)
    fig.savefig("t.png")
    #plt.show()

#savefig()
#basic_plot_text(plenty=120)
plot_text(plenty=120)
