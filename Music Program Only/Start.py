from P5 import *
from P4 import *

from P3FEMC import *
from DanceParty import *

from tkinter import *
from P3 import *
global NoMusic, home,NoLight,Retro , AlarmStr, LightLevel, LightText, AlarmH , AlarmM , AHPic, AMPic, gifOn,TimeFrame, framecount, Rframecount
global RTotalFrames, Music, frame, Rframe, frametotal, Alarm_Hr, Alarm_Min, HomeOn
NoMusic = False
Retro = False
NoLight = True
AlarmStr = "08:00"
LightText=  "max"
LightLevel =255
AlarmH= 8
AlarmM= 0
HomeOn = True
gifOn = True
home= Tk()
Rframecount = 0
RTotalFrames = 170
TimeFrame = LabelFrame(home)
MBI = PhotoImage(file = "Pictures/YukariGif/0.gif")
framecount = 0
frame = []
Rframe = []
frametotal  = 196

def closewindow():
    global AlarmStr, HomeOn
    HomeOn =False
    if AlarmH <10:
        AlarmStr = "0"+str(AlarmH)+":"
    
    elif AlarmH >=10:
        AlarmStr =str(AlarmH)+ ":"

    if AlarmM == 0:
        AlarmStr = AlarmStr +"00"

    else:
        AlarmStr = AlarmStr + str(AlarmM)

def P3Click():
    home.destroy()
    closewindow()
    P3(NoMusic,NoLight,Retro,LightLevel)
    
def P4Click():
    global NoMusic, home, NoLight, Retro, LightLevel
    home.destroy()
    closewindow()
    P4(NoMusic,NoLight,Retro,LightLevel)
    
def P5Click():
    home.destroy()
    closewindow()
    P5(NoMusic,NoLight,Retro,LightLevel,AlarmStr)
    
def P3FEMCClick():
    home.destroy()
    closewindow()
    P3FEMC(NoMusic,NoLight,Retro,LightLevel)

def DPClick():
    home.destroy()
    closewindow()
    DP(NoMusic, NoLight, LightLevel)
    
def MusicClick():
    global NoMusic, framecount
    if NoMusic == False:
        NoMusic = True
    
    else:
        NoMusic = False
        framecount = 0
        

        
def RetroClick():
    global Retro, Rframecount
    if Retro == False:
        Retro = True
    
    else:
        Retro = False
        Rframecount = 0

def GetFrames():
    for i in range(frametotal):
        text = "Pictures/YukariGif/" +str(i)+ ".gif"
        frame.append(PhotoImage(file = text))

    for i in range(RTotalFrames):
        if (i+2)<10:
            text = "Pictures/Buttons/RetroGif/frame_00" +str(i+2)+ "_delay-0.04s.gif"
        elif (i+2)>=10 and (i+2) <100:
            text = "Pictures/Buttons/RetroGif/frame_0" +str(i+2)+ "_delay-0.04s.gif"
        elif (i+2)>=100:
            text = "Pictures/Buttons/RetroGif/frame_" +str(i+2)+ "_delay-0.04s.gif"
        Rframe.append(PhotoImage(file = text))

def updateframe():
    global Music, framecount, home,MBI, frametotal, HomeOn
    if NoMusic == False:
        Music.configure(image = frame[framecount])
        framecount = framecount + 1
        if framecount == frametotal:
            framecount = 0
    elif NoMusic == True:
        MBI = PhotoImage(file = r"Pictures/Buttons/NoMusic.png")
        Music.configure(image = MBI)
    if HomeOn == True:
        home.after(100, updateframe)

def Retroframe():
    global Retro, Rframecount, home,RBI, RTotalFrames, SRetro, Rframe, HomeOn
    if Retro == True:
        SRetro.configure(image = Rframe[Rframecount])
        Rframecount = Rframecount + 1
        if Rframecount == RTotalFrames:
            Rframecount = 0
    elif Retro == False:
        RBI = PhotoImage(file = r"Pictures/Buttons/RetroButton.png")
        SRetro.configure(image = RBI)
    if HomeOn == True:
        home.after(40, Retroframe)


def HourClick():
    global AlarmH
    global Alarm_Hr
    AlarmH = AlarmH + 1
    if AlarmH == 24:
        AlarmH = 0
    global AMPF
    AHPF = "Pictures/Time_Stamps/Hour/"+str(AlarmH)+".png"
    global AHPic
    AHPic = PhotoImage(file = AHPF)
    Alarm_Hr.configure(image = AHPic)

def MinClick():
    global AlarmM, Alarm_Min, AMPF, AMPic
    AlarmM = AlarmM + 15
    if AlarmM == 60:
        AlarmM = 0
    AMPF = "Pictures/Time_Stamps/Min/"+str(AlarmM)+".png"
    AMPic = PhotoImage(file = AMPF)
    Alarm_Min.configure(image = AMPic)
    
def main():
    global AMPF, AMPIC, AHPF, AHPIC, Alarm_Hr, Alarm_Min,SRetro,Light, home ,TimeFrame, Music
    Music = Button(home, image = PhotoImage("Pictures/Buttons/Blankbutton.png"),  compound="top",command = MusicClick)
    GetFrames()
    AMPF = "Pictures/Time_Stamps/Min/0.png"
    AMPic = PhotoImage(file = AMPF) 
    AHPF = "Pictures/Time_Stamps/Hour/8.png"
    AHPic = PhotoImage(file = AHPF) 
    Alarm_Hr = Button(TimeFrame,image = AHPic, compound="top", command = HourClick)
    Alarm_Min = Button(TimeFrame,image = AMPic, compound="top", command = MinClick)
    home.title("Control Board")

    home.geometry('1225x630')
    P3BI = PhotoImage(file = r"Pictures/Buttons/P3Button.png")
    P3Button = Button(home, image=P3BI,command = P3Click)
    P3Button.grid(column=0, row=1)
    
    P3FBI = PhotoImage(file = r"Pictures/Buttons/P3FEMCButton.png")
    P3FEMCButton = Button(home, image=P3FBI , compound="top",command = P3FEMCClick)
    P3FEMCButton.grid(column=1, row=1)
    
    P4BI = PhotoImage(file = r"Pictures/Buttons/P4Button.png") 
    P4Button = Button(home, image=P4BI, compound="top", command = P4Click)
    P4Button.grid(column=2, row=1)
    
    P5BI = PhotoImage(file = r"Pictures/Buttons/P5Button.png")
    P5Button = Button(home, image=P5BI , compound="top", command = P5Click)
    P5Button.grid(column=0, row=2)
    
    DPBI = PhotoImage(file = r"Pictures/Buttons/DPButton.png")
    DPButton = Button(home, image = DPBI , compound="top", command = DPClick)
    DPButton.grid(column=1, row=2)
    
    RBI = PhotoImage(file = r"Pictures/Buttons/RetroButton.png")
    SRetro = Button(home,image = RBI,  compound="top", command = RetroClick)


    TimeFrame.grid(row=2, column=2)
    Alarm_Hr.pack(side = LEFT)
    Alarm_Min.pack(side = RIGHT)

    Music.grid(column=0, row=3)
    SRetro.grid(column=1, row=3)
    if NoMusic == False:
        home.after(100, updateframe)
    if Retro == False:
        home.after(40, Retroframe)
    home.mainloop()
main()
