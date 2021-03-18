import pygame
import time
#from neopixel import *
import random as R
from tkinter import *

global NoMusic, NoLight, Background_Color, window, AlbumArt
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


def standard(strip,Colors, wait_ms=.5):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Colors[i])
        strip.show()
        time.sleep(wait_ms/1000.0)
    RED = R.randint(0,255)
    G = R.randint(0,255)
    B = R.randint(0,255)
    Colors.insert(0,Color(RED,G,B))
    Colors.pop()

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
            
def JukeBox():
    global MusicLabel, SongPlayer, AlbumArt
    TrackList = open(r"DanceParty/Tracklist.txt","r")
    ArtList = open (r"DanceParty/Art.txt","r")
    Track = songPick(TrackList,ArtList)
    sn= R.randint(0,len(Track)-1)
    TheSong = Track[sn]
    pygame.mixer.music.load(TheSong.getSong())
    pygame.mixer.music.play()
    TrackList.close()
    TheFile = TheSong.getArt()
    AlbumArt = PhotoImage(file  = TheFile)
    SongPlayer.configure(image = AlbumArt)
    SongName = TheSong.getSong()[11:-4]
    SongName = SongName.replace("_"," ")
    if len(SongName) <=36:
        MusicLabel.configure(font=("Helvetica", 25))

    if len(SongName) >36:
       MusicLabel.configure(font=("Helvetica", 20))

    MusicLabel.configure (text = SongName)
    return

def getColors(pixels):
    Colors = []
    for i in range(pixels):
            RED = R.randint(0,255)
            G = R.randint(0,255)
            B = R.randint(0,255)
            Colors.append(Color(RED,G,B))
    return Colors
def GetBGC():
    global window, Background_Color, MusicLabel
    random_number = R.randint(1118481,16777215)
    hex_number = str(hex(random_number))
    Background_Color ='#'+ hex_number[2:]
    window['background']= Background_Color
    MusicLabel['background']= Background_Color
def DP (NoMusic1, NoLight1, LL):
    global NoMusic, NoLight, Background_Color, window, MusicLabel, SongPlayer
    NoMusic = NoMusic1
    NoLight  = NoLight1
    strip = 0
    
    if NoMusic == False:
        window= Tk()
        window.geometry('600x660')
        window.title("Music Player")
        AlbumArt = PhotoImage(file = r"Pictures/AlbumArt/Default_Album_Art.png")
        SongPlayer = Button(window, image=AlbumArt , compound="top")
        SongPlayer.place(x = 0 , y =0 )   
        MusicLabel =  Label(window, text = "Temp Text",font=("Helvetica", 25),anchor=W, justify=LEFT)
        MusicLabel.place(x = 0 , y =615)
        GetBGC()
        MusicLabel['background']= Background_Color
        
        
    if NoLight == False:
        
        LED_COUNT      = 60
        LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
        LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
        LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
        LED_BRIGHTNESS = LL     # Set to 0 for darkest and 255 for brightest
        LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
        LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
        strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        strip.begin()
        Colors = []
        getColors(strip.numPixels())

    pygame.mixer.init()
    try:
        while(1==1):
            if pygame.mixer.music.get_busy() == False and NoMusic == False:
                JukeBox()
                GetBGC()
                
            if NoLight == False:
                standard(strip,Colors)
            if NoMusic == False:
                window.update()
    except KeyboardInterrupt:
        if NoLight == False:
            colorWipe(strip)
