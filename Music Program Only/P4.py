import pygame
import time
import datetime as d
import random as R
from tkinter import *
from timeit import default_timer as timer
global NoMusic, NoLight, Retro, Background_Color
Background_Color = '#ffe603'

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

def thedelay(fps):
    x = timer()
    while timer() - x < fps:
        pass
    return

def playSong(Song):
    pygame.mixer.music.load(Song)
    pygame.mixer.music.play()
    

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
            
            
def RiseJukeBox(F,G,x):
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

def pickFrameYK(i):
    delay = .041
    if i<=295:
            j=i
            if (j<10):
                fileName = "Pictures/MidnightChannels/Yukiko/1/frame_00"+ str(j)+"_delay-0.05s.png"
            elif (100>j>=10):
                fileName = "Pictures/MidnightChannels/Yukiko/1/frame_0"+ str(j)+"_delay-0.05s.png"
            elif (j>=100):
                fileName = "Pictures/MidnightChannels/Yukiko/1/frame_"+ str(j)+"_delay-0.05s.png"

    elif 557>=i>=296:
            j=i-296
            if (j<10):
                fileName = "Pictures/MidnightChannels/Yukiko/2/frame_00"+ str(j)+"_delay-0.05s.png"
            elif (100>j>=10):
                fileName = "Pictures/MidnightChannels/Yukiko/2/frame_0"+ str(j)+"_delay-0.05s.png"
            elif (j>=100):
                fileName = "Pictures/MidnightChannels/Yukiko/2/frame_"+ str(j)+"_delay-0.05s.png"

    elif i>=558:
            j=i-558
            if (j<10):
                fileName = "Pictures/MidnightChannels/Yukiko/3/frame_00"+ str(j)+"_delay-0.05s.png"
            elif (100>j>=10):
                fileName = "Pictures/MidnightChannels/Yukiko/3/frame_0"+ str(j)+"_delay-0.05s.png"
            elif (j>=100):
                fileName = "Pictures/MidnightChannels/Yukiko/3/frame_"+ str(j)+"_delay-0.05s.png"

    return fileName,delay

def pickFrameR(i):
    delay = .03
    if i<=239:
            j=i
            #frame_000_delay-0.04s
            if (j<10):
                fileName = "Pictures/MidnightChannels/Rise/1/frame_00"+ str(i)+"_delay-0.04s.png"
            elif (100>j>=10):
                fileName = "Pictures/MidnightChannels/Rise/1/frame_0"+ str(i)+"_delay-0.04s.png"
            elif (j>=100):
                fileName = "Pictures/MidnightChannels/Rise/1/frame_"+ str(i)+"_delay-0.04s.png"
    elif 485>=i>239:
            j=i-240
            if j == 0:
                delay = .03
            #frame_000_delay-0.04s
            if (j<10):
                fileName = "Pictures/MidnightChannels/Rise/2/frame_00"+ str(j)+"_delay-0.04s.png"
            elif (100>j>=10):
                fileName = "Pictures/MidnightChannels/Rise/2/frame_0"+ str(j)+"_delay-0.04s.png"
            elif (j>=100):
                fileName = "Pictures/MidnightChannels/Rise/2/frame_"+ str(j)+"_delay-0.04s.png"

    elif 700>=i>485:
            j=i-486
            if j == 0:
                delay = .03
            #frame_000_delay-0.04s
            if (j<10):
                fileName = "Pictures/MidnightChannels/Rise/3/frame_00"+ str(j)+"_delay-0.04s.gif"
            elif (100>j>=10):
                fileName = "Pictures/MidnightChannels/Rise/3/frame_0"+ str(j)+"_delay-0.04s.gif"
            elif (j>=100):
                fileName = "Pictures/MidnightChannels/Rise/3/frame_"+ str(j)+"_delay-0.04s.gif"

    elif i>700:
            j=i-701
            #frame_000_delay-0.04s
            if (j<10):
                fileName = "Pictures/MidnightChannels/Rise/4/frame_00"+ str(j)+"_delay-0.04s.png"
            elif (100>j>=10):
                fileName = "Pictures/MidnightChannels/Rise/4/frame_0"+ str(j)+"_delay-0.04s.png"
            elif (j>=100):
                fileName = "Pictures/MidnightChannels/Rise/4/frame_"+ str(j)+"_delay-0.04s.png"


    return fileName,delay
def pickFrameK(i):
    delay = .04
    if i<=270:
            j=i
            #frame_000_delay-0.04s
            if (j<10):
                fileName = "Pictures/MidnightChannels/Kanji/1/frame_00"+ str(i)+"_delay-0.05s.png"
            elif (100>j>=10):
                fileName = "Pictures/MidnightChannels/Kanji/1/frame_0"+ str(i)+"_delay-0.05s.png"
            elif (j>=100):
                fileName = "Pictures/MidnightChannels/Kanji/1/frame_"+ str(i)+"_delay-0.05s.png"
    elif 521>=i>270:
            j=i-271
            #frame_000_delay-0.04s
            if (j<10):
                fileName = "Pictures/MidnightChannels/Kanji/2/frame_00"+ str(j)+"_delay-0.05s.png"
            elif (100>j>=10):
                fileName = "Pictures/MidnightChannels/Kanji/2/frame_0"+ str(j)+"_delay-0.05s.png"
            elif (j>=100):
                fileName = "Pictures/MidnightChannels/Kanji/2/frame_"+ str(j)+"_delay-0.05s.png"

    elif i>521:
            j=i-522
            #frame_000_delay-0.04s
            if (j<10):
                fileName = "Pictures/MidnightChannels/Kanji/3/frame_00"+ str(j)+"_delay-0.05s.png"
            elif (100>j>=10):
                fileName = "Pictures/MidnightChannels/Kanji/3/frame_0"+ str(j)+"_delay-0.05s.png"
            elif (j>=100):
                fileName = "Pictures/MidnightChannels/Kanji/3/frame_"+ str(j)+"_delay-0.05s.png"
    return fileName,delay
def pickFrameN(i):
    delay = .041
    if i<=282:
            j=i
            if (j<10):
                fileName = "Pictures/MidnightChannels/Naoto/1/frame_00"+ str(j)+"_delay-0.05s.png"
            elif (100>j>=10):
                fileName = "Pictures/MidnightChannels/Naoto/1/frame_0"+ str(j)+"_delay-0.05s.png"
            elif (j>=100):
                fileName = "Pictures/MidnightChannels/Naoto/1/frame_"+ str(j)+"_delay-0.05s.png"
    elif 576>=i>282:
            j=i-282
            if (j<10):
                fileName = "Pictures/MidnightChannels/Naoto/2/frame_00"+ str(j)+"_delay-0.05s.png"
            elif (100>j>=10):
                fileName = "Pictures/MidnightChannels/Naoto/2/frame_0"+ str(j)+"_delay-0.05s.png"
            elif (j>=100):
                fileName = "Pictures/MidnightChannels/Naoto/2/frame_"+ str(j)+"_delay-0.05s.png"

    elif i>576:
            j=i-576
            if (j<10):
                fileName = "Pictures/MidnightChannels/Naoto/3/frame_00"+ str(j)+"_delay-0.05s.png"
            elif (100>j>=10):
                fileName = "Pictures/MidnightChannels/Naoto/3/frame_0"+ str(j)+"_delay-0.05s.png"
            elif (j>=100):
                fileName = "Pictures/MidnightChannels/Naoto/3/frame_"+ str(j)+"_delay-0.05s.png"




    return fileName,delay
def playYukikoMC():
    global SongPlayer, AlbumArt, fileName, window
    playSong("P4/Yukiko.wav")
    i = 0
    while i < (677):
        fileName, delay = pickFrameYK(i)
        AlbumArt = PhotoImage(file = fileName)
        SongPlayer.configure(image = AlbumArt)
        window.update_idletasks()
        
        thedelay(delay)
        i = i +1 

def playKanjiMC():
    global SongPlayer, AlbumArt, fileName, window
    playSong("P4/Kanji.wav")
    i = 1
    while i < (763):
        fileName, delay = pickFrameK(i)
        AlbumArt = PhotoImage(file = fileName)
        SongPlayer.configure(image = AlbumArt)
        window.update_idletasks()
        
        thedelay(delay)
        i = i +1 

def playRiseMC():
    global SongPlayer, AlbumArt, fileName, window
    playSong("P4/Rise.wav")
    i = 1
    while i < (878):
        fileName, delay = pickFrameR(i)
        AlbumArt = PhotoImage(file = fileName)
        SongPlayer.configure(image = AlbumArt)
        window.update_idletasks()
        
        thedelay(delay)
        i = i +1 

def playNaotoMC():
    global SongPlayer, AlbumArt, fileName, window
    playSong("P4/Naoto.wav")
    i = 1
    while i < (874):
        fileName, delay = pickFrameN(i)
        AlbumArt = PhotoImage(file = fileName)
        SongPlayer.configure(image = AlbumArt)
        window.update_idletasks()
        
        thedelay(delay)
        i = i +1 

def OpeningMC():
    x= R.randint(0,4)
    x=0
    if x==0:
        playYukikoMC()
    elif x==1:
        playKanjiMC()
    elif x==2:
        playRiseMC()
    elif x==3:
        playNaotoMC()

def MidnightChannel(strip):
    global MCGIF
    if NoLight == False:
        colorWipe(strip)
    if MCGIF == False:
        OpeningMC()
        MCGIF == True
    
def P4(NoMusic1, NoLight1, Retro1, LL):
    global NoMusic, NoLight, Retro, window, AlbumArt, IsDarkHour, MusicLabel, Background_Color, SongPlayer, fps,MCGIF
    
    NoMusic = NoMusic1
    NoLight = NoLight1
    Retro = Retro1
    strip =0
    if NoMusic == False:
        window= Tk()
        window.geometry('600x660')
        window.title("Music Player")
        window['background']= Background_Color
        AlbumArt = PhotoImage(file = r"Pictures/AlbumArt/Default_Album_Art.png")
        SongPlayer = Button(window, image=AlbumArt , compound="top")
        SongPlayer.place(x = 0 , y =0 )   
        MusicLabel =  Label(window, text = "Temp Text",font=("Helvetica", 25),anchor=W, justify=LEFT)
        MusicLabel['background']= Background_Color
        MusicLabel.place(x = 0 , y =615)
   

    print ('Press Ctrl-C to quit.')
    pygame.mixer.init()

    try:
        n= 0
        x = 3
        F = r"P4/P4Songs.txt"
        G = r"P4/P4Art.txt"
        
        if Retro:
            x = 9
            F = r"P4/Retro/P4Songs.txt" 
            G = r"P4/Retro/P4Art.txt" 
        
        while(True):

            weather = 'Rain'
            if pygame.mixer.music.get_busy() == False and NoMusic != True:
                Art, SongPlaying = RiseJukeBox(F,G,x)
                img = Art
                other =PhotoImage(file = img)
                SongPlayer.configure(image = other)
                if len(SongPlaying) <=36:
                        MusicLabel.configure(font=("Helvetica", 25))

                if len(SongPlaying) >36:
                        MusicLabel.configure(font=("Helvetica", 20))
                MusicLabel.configure(text = SongPlaying)
                window.update_idletasks()
            
            dt = str(d.datetime.now())
            

            if dt[11:19] == "00:00:00" and weather == 'Rain':
               window.geometry('600x340')
               MCGIF =False
               pygame.mixer.music.fadeout(500)
               MidnightChannel(strip)
               window.geometry('600x660')

         
             
            if NoMusic == False:
                window.update()
    except KeyboardInterrupt:
        return
