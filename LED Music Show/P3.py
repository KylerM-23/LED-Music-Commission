import pygame
import time
#from neopixel import *
import datetime as d
import random as R
from tkinter import *
from time import *

global Background_Color,Dark_Hour_Frames,TotalFrame ,FrameNum,window ,AlbumArt,MusicLabel, IsDarkHourGif, PlayerArt, fps ,DHT, currentSong
Background_Color = '#2495ff'   
DHT = "00:00:00"
Dark_Hour_Frames= []
TotalFrame = 190
FrameNum = 0
IsDarkHourGif = True
fps =.05

def createframes():
    global Dark_Hour_Frames
    for i in range (192):
        x = i
        if i <10:
            Dark_Hour_Frames.append(PhotoImage(file = "Pictures/Dark_Hour_Blue/frame_00"+str(x)+"_delay-0.05s.png"))

        elif 100>i >=10:
            Dark_Hour_Frames.append(PhotoImage(file = "Pictures/Dark_Hour_Blue/frame_0"+str(x)+"_delay-0.05s.png"))

        elif i >=100:
            Dark_Hour_Frames.append(PhotoImage(file = "Pictures/Dark_Hour_Blue/frame_"+str(x)+"_delay-0.05s.png"))

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
   
def standard(strip,n,NoMusic,NoLight, wait_ms=10):
    if strip != 0:
        #9,147,246
        color = Color(6,6,47)
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            if n == 1:
                color = Color(255,255,255)
                n = 0
        
            else:
                n = n + 1
                color = Color(6,6,47)        
               
def colorWipe(strip):
    for i in range (strip.numPixels()):
        strip.setPixelColor(i,Color(0,0,0))
        strip.show()

def delay(fps):
    x = time()
    #print(x)
    while time() - x < fps:
        pass
    return
def DarkHourGif():
    global FrameNum, TotalFrame, Dark_Hour_Frames, Album_Art, SongPlayer, IsDarkHour, window, IsDarkHourGif, PlayerArt, fps
    while(IsDarkHourGif == False):
        PlayerArt = Dark_Hour_Frames[FrameNum]
        SongPlayer.configure(image = PlayerArt)
        window.update_idletasks()
    
        if FrameNum == TotalFrame:
            FrameNum = 0
            IsDarkHourGif = True
            break

        else:
            FrameNum = FrameNum + 1
            delay(fps)
    return
    

def DarkHour(strip,dt,n,NoMusic,NoLight,wait_ms=1):
    global window,IsDarkHour, IsDarkHourGif, DHT
    #rgb(9,108,42)
    
    if NoMusic == False:

        if IsDarkHourGif == False and pygame.mixer.music.get_busy() == False:
            pygame.mixer.music.load("P3/Dark_Hour_Blue.wav")
            pygame.mixer.music.play()
            DarkHourGif()
            
           
    if NoLight == False:
        color = Color(0,0,0)
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            if n == 1:
                color = Color(0,0,0)
                n = 0
        
            else:
                n = n + 1
                color = Color(169,49,14)

def songPick(TrackList, ArtList):
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
                        
def FuukaJukeBox(F,G,x):
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

def P3(NoMusic1, NoLight1, Retro1, LL):
    global window, AlbumArt, IsDarkHourGif, MusicLabel, Background_Color, SongPlayer, fps, DHT
    
    strip = 0
    NoMusic = NoMusic1
    NoLight = NoLight1
    Retro = Retro1

    if NoMusic == False:
        window= Tk()
        createframes()
        window.geometry('600x660')
        window.title("Music Player")
        window['background']= '#2495ff'
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

    try:
        n= 0
        x = 3
        F = r"P3/P3Songs.txt"
        G = r"P3/P3Art.txt"
        
        if Retro:
            x = 9
            F = r"P3/Retro/P3Songs.txt" 
            G = r"P3/Retro/P3Art.txt" 
            
        while(True):
            dt = str(d.datetime.now())
            sleep(1)
            dt2 = dt[11:19]
            if dt2 == DHT:
                IsDarkHourGif = False
            if pygame.mixer.music.get_busy() == False and NoMusic == False:
                if IsDarkHourGif == False:
                    pass
                else:
                    Art, SongPlaying = FuukaJukeBox(F,G,x)

                    img = Art
                    if len(SongPlaying) <=36:
                        MusicLabel.configure(font=("Helvetica", 25))

                    if len(SongPlaying) >36:
                        MusicLabel.configure(font=("Helvetica", 20))
                    other =PhotoImage(file = img)
                    SongPlayer.configure(image = other)
                    MusicLabel.configure(text = SongPlaying)
                    window.update_idletasks()

            n = n + 1
                
            if n == 2:
                    n = 0
                
            
            if dt[11:13] != DHT[0:2]:
                Background_Color = '#2495ff'
                if NoMusic == False:
                    MusicLabel['background']= Background_Color
                
                    window['background'] = Background_Color
                standard(strip,n,NoMusic,NoLight)
            elif dt[11:13] == DHT[0:2]:
                if NoMusic == False:
                    Background_Color = '#086d32'
                    MusicLabel['background']= Background_Color
                    window['background'] = Background_Color
                
                if IsDarkHourGif == False and NoMusic == False:
                    pygame.mixer.music.fadeout(500)
                    DarkHR1 =(Dark_Hour_Frames[0])
                    SongPlayer.configure(image = DarkHR1)
                    MusicLabel.configure(text = "Dark Hour")
                    
                
                
                DarkHour(strip,dt2,n,NoMusic,NoLight)
            
            if NoMusic == False:
                window.update()
            

    except KeyboardInterrupt:
        if NoMusic == False:
            window.destroy()
        if NoLight == False:
            colorWipe(strip)
#37 charcaters max for a line