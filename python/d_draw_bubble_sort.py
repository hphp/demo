
'''
Created on Jan 17, 2013

@author: Shannon
'''
import wx
import random


size = 30
xPos = 50
BarData = []
width = 900/(size*2)
gap = 900/(size*4)
delay = 100

class AnimationPanel(wx.Panel):
    
    def __init__(self,parent,ID=-1,pos=(0,0),size=(750,500)):
        wx.Panel.__init__(self,parent,ID,pos,size)
        self.SetBackgroundColour("BLACK")
        
        self.GenerateBarData(xPos)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
         
        self.font = wx.Font(8, wx.DEFAULT, wx.ITALIC, wx.NORMAL)
        
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)
                
  
    #generate the original bars's data (x,y,w,h)    
    def GenerateBarData(self,xPos):               
        for num in range(size):           
            xPos += (width + gap)
            height = random.randrange(5,300)
            barParameters=[xPos, 100, width, height]
            BarData.append(barParameters)                  
        self.RevertBarData()
          
    #revert the bars' yPos      
    def RevertBarData(self):
        maxH = self.maxHeight()
        for h in range(size):            
            moveH = maxH - BarData[h][3]
            yPos = BarData[h][1]
            yPos += moveH
            BarData[h][1] = yPos
  
    #return the hightest height in bars
    def maxHeight(self):
        Height = []
        #store all the bar height in Height[]
        for h in range(size):
            Height.append(BarData[h][3])
        #find out the heightest bar and return
        maxH = max(Height)
        return maxH
      
    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        self.paintBox(dc)
      
    def paintBox(self, dc):
        dc.SetBrush(wx.Brush("green"))
        dc.SetFont(self.font)
        dc.SetTextForeground("GREEN")
        for i in range(0,size):
            dc.DrawRectangle(*BarData[i])
            x = BarData[i][0]
            y = BarData[i][1] + BarData[i][3]
            h = str(BarData[i][3])
            dc.DrawText(h, x, y)
             
                
    #bubble sort
    def BubbleSort(self):
        for i in range(len(BarData), 1, -1):
            for j in range(i-1):
                if BarData[j][3] > BarData[j+1][3]:
                    BarData[j][1], BarData[j+1][1] = BarData[j+1][1], BarData[j][1]
                    BarData[j][3], BarData[j+1][3] = BarData[j+1][3], BarData[j][3]
                    yield
                     
    def OnTimer(self, event):
        if not hasattr(self, 'g'):
            self.g = self.BubbleSort()
        try:
            next(self.g)
            self.Refresh()
        except StopIteration:
            del self.g
            self.timer.Stop()
            wx.MessageBox('Done!')
        
class SidePanel(wx.Panel):
    def __init__(self, parent, aPanel, ID=-1,pos=(750,0),size=(250,500)): 
        wx.Panel.__init__(self,parent,ID,pos,size)
        self.SetBackgroundColour("GREY")
        self._aPanel = aPanel
        
        #---------------------------------------------        
        #create Button_Panel on Side_Panel
        self.Button_Panel = wx.Panel(self, -1,pos=(750,0),size=(250,150))
        
        #create ButtonSizer for button_panel
        ButtonSizer = wx.GridSizer(rows = 2, cols = 2)
        border = 3
        #create 4 buttons label, add them to Button_Panel
        #and binding them with corresponding event
        buttonLabel = (("Start", self.OnStart),
                       ("Step back", self.OnStepBack),
                       ("Pause", self.OnPause),
                       ("Step forward", self.OnStepForward))
        
        for eachLabel, eachHandle in buttonLabel:
            button = wx.Button(self.Button_Panel, -1, eachLabel)
            button.Bind(wx.EVT_BUTTON, eachHandle)
            ButtonSizer.Add(button, 0, wx.EXPAND|wx.ALL, border)
        self.Button_Panel.SetSizer(ButtonSizer)
        
        #---------------------------------------------

        #---------------------------------------------
        #Create ChoiceList_Panel for 2 choice dropdown list
        #Sort_List: provide choice of sorting algorithm
        #Graph_List: provide choice of graph algorithm
        self.ChoiceList_Panel = wx.Panel(self, -1, pos=(750,150),size=(250,150))
       
        SortList = ['Bubble Sort','Insertion Sort','Merge Sort',
                       'Quick Sort','Selection Sort','Shell Sort']
        GraphList = ['Breath-First Search', 'Depth-First Search',
                     'Dijkstra\'s Shortest Path', 'Prim\'s minimun spanning tree']
        #wx.Choice(parent,id,pos,size,choices,style,validator,name)
        SortChoice = wx.Choice(self.ChoiceList_Panel, -1,choices=SortList)
        GraphChoice = wx.Choice(self.ChoiceList_Panel, -1, choices=GraphList)
        al_tex = wx.StaticText(self.ChoiceList_Panel, -1, 'Select a sorting algorithm:')
        graph_tex = wx.StaticText(self.ChoiceList_Panel, -1, 'Or a graph algorithm:')
        ChoiceSizer = wx.BoxSizer(wx.VERTICAL)
        ChoiceSizer.Add(al_tex,1,wx.EXPAND|wx.ALL)
        ChoiceSizer.Add(SortChoice,1, wx.EXPAND|wx.ALL)
        ChoiceSizer.Add(graph_tex,1,wx.EXPAND|wx.ALL)
        ChoiceSizer.Add(GraphChoice,1,wx.EXPAND|wx.ALL)
        self.ChoiceList_Panel.SetSizer(ChoiceSizer)
        #---------------------------------------------

        #---------------------------------------------
        #create Size_Panel
        #Provide a set of size RadioBox
        self.Size_Panel = wx.Panel(self, -1, pos=(750,300),size=(250,100))
        SizeList = ['5','10','15','20','25','30','35','40','45','50']
        Size_RadioBox = wx.RadioBox(self.Size_Panel,-1,"Select size",wx.DefaultPosition,wx.DefaultSize,SizeList,5,wx.RA_SPECIFY_COLS)
        SizeSizer = wx.BoxSizer(wx.VERTICAL)
        SizeSizer.Add(Size_RadioBox,1, wx.EXPAND|wx.ALL)
        self.Size_Panel.SetSizer(SizeSizer)
        #---------------------------------------------

        #---------------------------------------------
        #create a Speed_Panel
        #Speed_Panel contains a slider used for control the speed of animation
        self.Speed_Panel = wx.Panel(self, -1, pos=(750,400),size=(250,100))
        Speed_Slider = wx.Slider(self.Speed_Panel, -1,25,1,50,wx.DefaultPosition,(250,-1),wx.SL_HORIZONTAL|wx.SL_AUTOTICKS|wx.SL_LABELS,name="Speed")
        Speed_Slider.SetTickFreq(5,1)
        Speed_tex = wx.StaticText(self.Speed_Panel, -1, "Change animation's speed")
        Speed_Sizer = wx.BoxSizer(wx.VERTICAL)
        Speed_Sizer.Add(Speed_tex,0,wx.EXPAND|wx.ALL)
        Speed_Sizer.Add(Speed_Slider,0,wx.EXPAND|wx.ALL)
        self.Speed_Panel.SetSizer(Speed_Sizer)
        #---------------------------------------------
        
        Side_PanelSizer = wx.BoxSizer(wx.VERTICAL)
        Side_PanelSizer.Add(self.Button_Panel,0,wx.EXPAND)
        Side_PanelSizer.Add(self.ChoiceList_Panel,0,wx.EXPAND)
        Side_PanelSizer.Add(self.Size_Panel,0,wx.EXPAND)
        Side_PanelSizer.Add(self.Speed_Panel,0,wx.EXPAND)
        self.SetSizer(Side_PanelSizer)
        
    def OnStart(self, event):
        self._aPanel.timer.Start(delay)
            
    def OnStepBack(self, event):
        pass

    def OnPause(self, event):
        self._aPanel.timer.Stop()

    def OnStepForward(self, event):
        pass
             
class MainFrame(wx.Frame):
    def __init__(self):
        
        wx.Frame.__init__(self, None, title="GUI",size=(1000,500))

        #---------------------------------------------       
        #create 2 panels
        #Animation_Panel---display the sorting animation
        #Side_panels---display the buttons, comboBox, slider
        self.Animation_Panel = AnimationPanel(self)
        self.Side_Panel = SidePanel(self, self.Animation_Panel)       

        #--------------------------------------------- 
        #arrange the two main panels in the main sizer for the MainFrame
        mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        mainSizer.Add(self.Animation_Panel, 2, wx.EXPAND)
        mainSizer.Add(self.Side_Panel, 1, wx.EXPAND)
        self.SetSizer(mainSizer)
        mainSizer.Fit(self)
        #---------------------------------------------
        
        
if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame()
    frame.Show()
    app.MainLoop()
