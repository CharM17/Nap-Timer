import os
import sys
import pygame
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import threading
from Nap import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    

    now_playing = 0
    nap_time = 0

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        Ui_MainWindow.__init__(self)
        self.initUI()
        self.setupUi(self)

    def initUI(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setMouseTracking(True)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            offset = event.globalPos() - self.drag_start_position
            self.move(self.x() + offset.x(), self.y() + offset.y())
            self.drag_start_position = event.globalPos()
    


    def close_window(self):
        sys.exit()

    def track_select(self, now_playing):
        if now_playing == 1:
            print("1")
        elif now_playing == 2:
            print("2")
        elif now_playing == 3:
            print("3")
        elif now_playing == 4:
            print("4")
    
    def set_time(self, value):
        self.nap_time = value * 60
    
    def button_control(self):
        sender = self.sender()
        buttons = [self.waveButton, self.fireplaceButton, self.frogButton, self.rainButton, self.noiseButton]
        for button in buttons:
            if button != sender:
                button.setChecked(False)

    def alarm(self):
        pygame.mixer.music.fadeout(60000)
        time.sleep(5)
        pygame.mixer.music.load("sounds/alarmsound.mp3")
        volume = .1
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play()
        while volume < 1:
            volume += .02
            time.sleep(1)
            pygame.mixer.music.set_volume(volume)
        buttons = [self.waveButton, self.fireplaceButton, self.frogButton, self.rainButton, self.noiseButton]
        for button in buttons:
            button.setChecked(False)
        time.sleep(60)
        pygame.mixer.music.fadeout(5000)
    
    def start_playing(self, now_playing):
        abspath = os.path.abspath(__file__)
        dname = os.path.dirname(abspath)
        os.chdir(dname)
        if now_playing == 1:
            song = "sounds/wavessound60.mp3"
        elif now_playing == 2:
            song = "sounds/firesound60.mp3"
        elif now_playing == 3:
            song = "sounds/frogsound60.mp3"
        elif now_playing == 4:
            song = "sounds/rainsound60.mp3"
        elif now_playing == 5:
            song = "sounds/brownnoise60.mp3"
        
        timer = threading.Timer(self.nap_time - 60 , window.alarm)
        timer.start()
        pygame.mixer.init()
        pygame.mixer.music.load(song)
        pygame.mixer.music.set_volume(.8)
        pygame.mixer.music.play()

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
