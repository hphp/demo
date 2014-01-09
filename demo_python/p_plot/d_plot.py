# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

def plot_text(rt=False, plenty=1):
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

    ax.axis([0, 100, 0, 100])

    if rt == True:
        return fig

    plt.show()

def savefig():
    fig = plot_text(rt=True)
    fig.savefig("t.png")
    #plt.show()

#savefig()
plot_text(plenty=3)
