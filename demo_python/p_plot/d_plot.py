# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

def figsize():
    w, h, dpi = (9, 12, 10)
    fig = plt.figure(figsize=(w, h), dpi=dpi)
    plt.show()

def subplot():
    plt.figure()
    plt.subplot(222)
    plt.plot([1,2,3])
    plt.subplot(224)
    plt.plot([4,5,6])
    plt.subplot(221)
    plt.plot([11,21,31])
    plt.show()

    plt.figure()
    plt.subplot(121)
    plt.plot([3,5,8])
    plt.show()

    plt.figure()
    plt.subplot(111)
    plt.plot([3,5,8])
    plt.show()

def plot_text_center():
    w, h = 2, 1
    fontsize = 50
    fig = plt.figure(figsize=(w, h), dpi = fontsize)
    sp = plt.subplot(111)
    sp.text(w/2., h/2., "goodboy", ha='center', va='center', fontsize=fontsize)
    sp.axis([0,w,0,h])
    plt.show()

def plot_without_ax():
    fig = plt.figure()
    sp = plt.subplot(111)
    sp.text(0, 0, "goodboy")
    plt.axis("off")
    plt.show()

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
#plot_text(plenty=120)
#plot_without_ax()
#subplot()
#figsize()
plot_text_center()
