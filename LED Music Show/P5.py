import pygame
import time
#from neopixel import *
import datetime as d
import random as R
from tkinter import *
from timeit import default_timer as timer

global NoMusic, NoLight, Retro, Background_Color, AlarmGif, StopGif, Force
Background_Color = '#cb111f'
AlarmGif = False
StopGif = False
Force = False

def thedelay(fps):
    x = timer()
    while timer() - x < fps:
        pass
    return

class Song:
    def __init__(self,Song,AlbumArt = "1"):
        self.Song = Song
        self.AlbumArt = AlbumArt
    
    def updateArt (self, Art):
        self.AlbumArt = Art
        
    def getSong(self):
        return self.Song
        
    def getArt(self):
        return self.AlbumArt
        
def playSong(Song):
    pygame.mixer.music.load(Song)
    pygame.mixer.music.play()
    
def standard(strip,n, wait_ms=5):
    if strip != 0:
        color = Color(0,255,0)
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            if n == 2:
                color = Color(165,218,32)
                n = 0
        
            else:
                n = n + 1
                color = Color(0,255,0)

def colorWipe(strip):
    for i in range (strip.numPixels()):
        strip.setPixelColor(i,Color(0,0,0))
        strip.show()

def songPick(TrackList,ArtList):
    Track = []
    for i in TrackList:
        x=Song(i.rstrip())
        Track.append(x)
    j = 0
    for i in ArtList:
        y = Track[j]
        j = j + 1
        y.updateArt(i.rstrip())
    
    return Track
            
            
def FutabaJukeBox(F,G,x):
    TrackList = open(F,"r")
    ArtList = open(G,"r")
    Track = songPick(TrackList,ArtList)
    sn= R.randint(0,len(Track)-1)
    Song = Track[sn]
    playSong(Song.getSong())
    TrackList.close()
    titileSong = Song.getSong()[x:-4]
    titileSong = titileSong.replace("_"," ")
    return Song.getArt(), titileSong


def Stop():
    global StopGif, Force
    if Force == True:
        StopGif = False
        StopGif = False
    elif Force == False:
        StopGif = True
        Force = True

def pickFrame(i):
    delay = .041
    if i<=279:
            j=i
            if (j<10):
                fileName = "Pictures/Wake_Up/1/frame_00"+ str(j)+"_delay-0.05s.png"
            elif (100>j>=10):
                fileName = "Pictures/Wake_Up/1/frame_0"+ str(j)+"_delay-0.05s.png"
            elif (j>=100):
                fileName = "Pictures/Wake_Up/1/frame_"+ str(j)+"_delay-0.05s.png"
    elif 559>=i>=280:
            j=i-280
            if (j<10):
                fileName = "Pictures/Wake_Up/2/frame_00"+ str(j)+"_delay-0.05s.png"
            elif (100>j>=10):
                fileName = "Pictures/Wake_Up/2/frame_0"+ str(j)+"_delay-0.05s.png"
            elif (j>=100):
                fileName = "Pictures/Wake_Up/2/frame_"+ str(j)+"_delay-0.05s.png"
    elif 839>=i>=560:
            j=i-560
            if (j<10):
                fileName = "Pictures/Wake_Up/3/frame_00"+ str(j)+"_delay-0.05s.png"
            elif (100>j>=10):
                fileName = "Pictures/Wake_Up/3/frame_0"+ str(j)+"_delay-0.05s.png"
            elif (j>=100):
                fileName = "Pictures/Wake_Up/3/frame_"+ str(j)+"_delay-0.05s.png"
    elif 1118>=i>=840:
            j=i-840
            if (j<10):
                fileName = "Pictures/Wake_Up/4/frame_00"+ str(j)+"_delay-0.05s.png"
            elif (100>j>=10):
                fileName = "Pictures/Wake_Up/4/frame_0"+ str(j)+"_delay-0.05s.png"
            elif (j>=100):
                fileName = "Pictures/Wake_Up/4/frame_"+ str(j)+"_delay-0.05s.png"
    elif 1397>=i>=1119:
            j=i-1119
            if (j<10):
                fileName = "Pictures/Wake_Up/5/frame_00"+ str(j)+"_delay-0.05s.png"
            elif (100>j>=10):
                fileName = "Pictures/Wake_Up/5/frame_0"+ str(j)+"_delay-0.05s.png"
            elif (j>=100):
                fileName = "Pictures/Wake_Up/5/frame_"+ str(j)+"_delay-0.05s.png"
    elif 1676>=i>=1398:
            j=i-1398
            if (j<10):
                fileName = "Pictures/Wake_Up/6/frame_00"+ str(j)+"_delay-0.05s.png"
            elif (100>j>=10):
                fileName = "Pictures/Wake_Up/6/frame_0"+ str(j)+"_delay-0.05s.png"
            elif (j>=100):
                fileName = "Pictures/Wake_Up/6/frame_"+ str(j)+"_delay-0.05s.png"
    elif i>=1677:
            j=i-1677
            if (j<10):
                fileName = "Pictures/Wake_Up/7/frame_00"+ str(j)+"_delay-0.05s.png"
            elif (100>j>=10):
                fileName = "Pictures/Wake_Up/7/frame_0"+ str(j)+"_delay-0.05s.png"
            elif (j>=100):
                fileName = "Pictures/Wake_Up/7/frame_"+ str(j)+"_delay-0.05s.png"

    return fileName,delay
def playOpen():
    global TMW, fileName,StopGif, other
    print(StopGif)
    if StopGif == True:
            print("This work")
            otherw.withdraw()
            return
    playSong("P5/Wake_Up.wav")
    i = 0
    while i < (1910):
        
        fileName, delay = pickFrame(i)
        Art = PhotoImage(file = fileName)
        TMW.configure(image = Art)
        otherw.update_idletasks()
        
        thedelay(delay)
        i = i +1 


def P5(NoMusic1,NoLight1, Retro1, LL, Alarm1):
    global StopGif, SongPlayer, window, AlbumArt, otherw, TMW, Force
    NoMusic = NoMusic1
    NoLight = NoLight1
    Retro  = Retro1
    Alarm = Alarm1
    strip = 0
    
    if NoMusic == False:
        window= Tk()
        otherw = Toplevel()
        otherw.withdraw()
        window.geometry('600x660')
        window.title("Music Player")
        window['background']= Background_Color
        TMW = Button(otherw, compound="top") 
        AlbumArt = PhotoImage(file = r"Pictures/AlbumArt/Default_Album_Art.png")
        SongPlayer = Button(window, image=AlbumArt , compound="top")
        SongPlayer.place(x = 0 , y =0 )   
        MusicLabel =  Label(window, text = "Temp Text",font=("Helvetica", 25),anchor=W, justify=LEFT)
        MusicLabel['background']= Background_Color
        MusicLabel.place(x = 0 , y =615)

    if NoLight == False:
        LED_COUNT      = 60
        LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
        LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
        LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
        LED_BRIGHTNESS = LL    # Set to 0 for darkest and 255 for brightest
        LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
        LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
        strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        strip.begin()

    pygame.mixer.init()

    F = "P5/P5Songs.txt"
    G = "P5/P5Art.txt"
    x = 3
    if  Retro:
        F = "P5/Retro/P5Songs.txt"
        G = "P5/Retro/P5Art.txt"
        x = 9
    try:
        n= 0
        

        while(True):
            dt = str(d.datetime.now())
            temp  = Alarm+":00"
            if temp == dt[11:19]:
                
                if Force == False:
                    otherw.deiconify()
                    otherw.title("Incoming Transmission")
                    StopGif = False
                           
                    TMW.grid(row=0, column=0)
                    window.withdraw()
                
                    otherw.geometry('600x300')
                    window.update_idletasks()
                    otherw.update_idletasks()
                    pygame.mixer.music.fadeout(500)
                    playOpen()
                    otherw.withdraw()
                    window.deiconify()
                    window.geometry('600x660')
                    window.update_idletasks()
                    
            if pygame.mixer.music.get_busy() == False and NoMusic == False:
                Art, SongPlaying = FutabaJukeBox(F,G,x)
                img = Art
                other =PhotoImage(file = img)
                SongPlayer.configure(image = other, command = Stop)
                MusicLabel.configure(text = SongPlaying)
                window.update_idletasks()
                
            
            if NoLight == False:
                
                if n >= 2:
                      n = 0
                standard(strip,n)
                n = n + 1
            
            if NoMusic == False:
                window.update()

    except KeyboardInterrupt:
        F.close()
        if NoLight == False:
            colorWipe(strip)
