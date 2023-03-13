#Imports
import os
import pygame
#Initalization
os.system("cls")
pygame.init()
#Time
timeSleep = .005
clock = pygame.time.Clock()
elapsedTime = 0
timer = 0

currentSong = 0
mode = 0
trackName = ("Untitled Track")
timeFromStart = 0

#Song Options
def songOptions():
    os.system("cls")
    #Acquire Song Length
    global trackLength
    global timeFromStart
    global songSettings
    trackLength = pygame.mixer.Sound.get_length(track)
    
    if pygame.mixer.get_busy == True:
        print ("Now Playing \""+str(trackName)+str("\""))
    if pygame.mixer.get_busy == False:
        print ("Paused \""+str(trackName)+str("\""))
    
    print ("1.Pause")
    print ("2.Resume")
    #print ("3.Restart")
    #print ("4.Rewind 10s")
    #print ("5.Skip 10s")
    print ("3.Menu")
    print ("")

    songSettings = int(input())
    if songSettings == 1:
        pygame.mixer.get_busy = False
        pygame.mixer.pause()
        songOptions()
    elif songSettings == 2:
        pygame.mixer.get_busy = True
        pygame.mixer.unpause()
        songOptions()
    elif songSettings == 3:
        pygame.mixer.unpause()
        pygame.mixer.stop()
        startup()
    if songSettings != 6:
        songOptions()
    
#Song
def song():
    os.system("cls")
    global currentSong
    pygame.mixer.Sound.stop(track)
    pygame.mixer.Sound.play(track)
    currentSong = 0
    songOptions()

#Play Song
def play_song():
    os.system("cls")
    global trackName, track
    print ("What song would you like to play?")
    print ("1. Bee Gees Stayin Alive")
    print ("2. Bon Jovi: Livin on a prayer")
    print ("3. Daryl Hall & John Oates: Out of Touch")
    print ("4. Aerosmith: Dream On")
    currentSong = (int(input()))

    if currentSong == 1:
        track = pygame.mixer.Sound("bee gees.wav")
        trackName = ("Bee Gees: Stayin Alive")
        pygame.mixer.get_busy = True
        song()
    elif currentSong == 2:
        track = pygame.mixer.Sound("living on a prayer.wav")
        trackName = ("Bon Jovi: Livin on a Prayer")
        pygame.mixer.get_busy = True
        song()
    elif currentSong == 3:
        track = pygame.mixer.Sound("out of touch.wav")
        trackName = ("Daryl Hall & John Oates: Out of Touch")
        pygame.mixer.get_busy = True
        song()
    elif currentSong == 4:
        track = pygame.mixer.Sound("dream on.wav")
        trackName = ("Aerosmith: Dream On")
        pygame.mixer.get_busy = True
        song()

#Startup
def startup():
    os.system("cls")
    global mode
    print ("Hello")
    print ("Welcome to Jukebox!")
    print ("Please choose a mode:")
    print ("1. Play a song")
    #print ("2. Create a playlist")
    mode = (int(input("")))
    if mode == 1:
        play_song()

#Application Setup
while True:
    event = pygame.event.poll()
    keys = pygame.key.get_pressed()
    #Quit Application
    if event.type == pygame.QUIT:
        pygame.mixer.stop()

    #Timer
    delayTime = clock.tick()
    elapsedTime = elapsedTime + delayTime
    if elapsedTime > 1:
        timer += 1
        timeFromStart += 1
    
    #Application Startup
    if mode == 0:
        startup()
    
    
    
        

