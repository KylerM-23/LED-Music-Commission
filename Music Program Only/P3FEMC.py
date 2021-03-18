import pygame
import time
import datetime as d
import random as R
from tkinter import *
from time import *

global Background_Color,Dark_Hour_Frames,TotalFrame ,FrameNum,window ,AlbumArt,MusicLabel, IsDarkHourGif, PlayerArt, fps ,DHT, currentSong
Background_Color = '#ff638e'   
DHT = "00:00:00"
Dark_Hour_Frames= []
TotalFrame = 176
FrameNum = 0
IsDarkHourGif = True
fps =.05

def createframes():
    global Dark_Hour_Frames
    for i in range (TotalFrame+1):
        x = i
        if i <10:
            Dark_Hour_Frames.append(PhotoImage(file = "Pictures/Dark_Hour_Pink/frame_00"+str(x)+"_delay-0.05s.png"))

        elif 100>i >=10:
            Dark_Hour_Frames.append(PhotoImage(file = "Pictures/Dark_Hour_Pink/frame_0"+str(x)+"_delay-0.05s.png"))

        elif i >=100:
            Dark_Hour_Frames.append(PhotoImage(file = "Pictures/Dark_Hour_Pink/frame_"+str(x)+"_delay-0.05s.png"))

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
   


def delay(fps):
    x = time()
    while time() - x < fps:
        pass
    return
def DarkHourGif():
    global FrameNum, TotalFrame, Dark_Hour_Frames, Album_Art, SongPlayer, IsDarkHour, window, IsDarkHourGif, PlayerArt, fps
    while(IsDarkHourGif == False):
        PlayerArt = Dark_Hour_Frames[FrameNum]
        SongPlayer.configure(image = PlayerArt)
        window.update_idletasks()
    
        if FrameNum >= TotalFrame:
            FrameNum = 0
            IsDarkHourGif = True
            return

        else:
            FrameNum = FrameNum + 1
            delay(fps)
    return
    

def DarkHour(strip,dt,n,NoMusic,NoLight,wait_ms=1):
    global window,IsDarkHour, IsDarkHourGif, DHT
    
    if NoMusic == False:

        if IsDarkHourGif == False and pygame.mixer.music.get_busy() == False:
            pygame.mixer.music.load("P3/Dark_Hour_Blue.wav")
            pygame.mixer.music.play()
            DarkHourGif()
            
      

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
                        
def FuukaJukeBox(x):
    global Retro
    File1 = open(r"P3/P3Songs.txt")
    File2 = open(r"P3/P3PSongs.txt")
    File3 = open(r"P3/P3Art.txt")
    File4 = open(r"P3/P3PArt.txt")
        

    if Retro:
        File1 = open(r"P3/Retro/P3Songs.txt")
        File2 = open(r"P3/Retro/P3PSongs.txt")
        File3 = open(r"P3/Retro/P3Art.txt")
        File4 = open(r"P3/Retro/P3PArt.txt")

    Track1 = songPick(File1,File3)
    Track2 = songPick(File2,File4)
    Track = Track1 + Track2
    sn= R.randint(0,len(Track)-1)
    SongPlay = Track[sn]
    playSong(SongPlay.getSong())
    titileSong = SongPlay.getSong()[x:-4]
    titileSong = titileSong.replace("_"," ")
    return SongPlay.getArt(), titileSong

def P3FEMC(NoMusic1, NoLight1, Retro1, LL):
    global window, AlbumArt, IsDarkHourGif, MusicLabel, Background_Color, SongPlayer, fps, DHT, Retro
    
    strip = 0
    NoMusic = NoMusic1
    NoLight = NoLight1
    Retro = Retro1

    if NoMusic == False:
        window= Tk()
        createframes()
        window.geometry('600x660')
        window.title("Music Player")
        window['background']= '#ff638e'
        AlbumArt = PhotoImage(file = r"Pictures/AlbumArt/Default_Album_Art.png")
        SongPlayer = Button(window, image=AlbumArt , compound="top")
        SongPlayer.place(x = 0 , y =0 )   
        MusicLabel =  Label(window, text = "Temp Text",font=("Helvetica", 25),anchor=W, justify=LEFT)
        MusicLabel['background']= Background_Color
        MusicLabel.place(x = 0 , y =615)

    pygame.mixer.init()

    try:
        n= 0
        x = 3
        if Retro:
            x = 9
            
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
                    Art, SongPlaying = FuukaJukeBox(x)

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
                Background_Color = '#ff638e'
                if NoMusic == False:
                    MusicLabel['background']= Background_Color
                
                    window['background'] = Background_Color
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

