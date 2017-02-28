#! /Python34
#! -*- coding: utf-8 -*-

"""
https://www.reddit.com/r/beginnerprojects/comments/4n9hne/project_idea_alarm_clock/
Paul Bosonetto
2/22/2017

Alarm Clock, accessed through a PyQt5 Gui, that displays a random Youtube video
(chosen from links in a text file), upon a user specified time.

THIS IS THE GUI FILE.

"""
import sys, random
from PyQt5.QtWidgets import (QMainWindow, QWidget, QApplication, QPushButton,
    QFrame, QHBoxLayout, QVBoxLayout, QSplitter, QStyleFactory, QTableWidget,
    QHeaderView, QGridLayout, QFileDialog)
from PyQt5.QtCore import Qt


class LinkPopup(QWidget):
    def __init__(self):
        super().__init__()

        self.initPopup()

    def initPopup(self):

        browseBtn = QPushButton(self)
        #table or list with links
        #need a label to show 'links list' location

        self.setGeometry(400,400,400,300)
        self.setWindowTitle('Link List')
        self.show()


class NewAlarmPopup(QWidget):
    def __init__(self):
        super().__init__()

        self.initPopup()

    def initPopup(self):
        self.setGeometry(300,300,400,300)
        self.setWindowTitle('Add new alarm')
        self.show()

class MainUI(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()



    #TODO put all the GUI stuff in another file and import it?
    #set up GUI
    def initUI(self):

        mainWidget = QWidget()
        self.setCentralWidget(mainWidget)

        self.button1 = QPushButton('Add New Alarm')
        self.button1.clicked.connect(self.openNewAlarmWindow)
        self.button2 = QPushButton('Update Links File')
        #self.button2.clicked.connect(YoutubeAlarmClock.getLinksFile)

        self.table1 = QTableWidget(mainWidget)
        #setRowCount number of columns for number of entries for that day
        self.table1.setRowCount(8)
        self.table1.setColumnCount(1)
        vLabels = ['Monday','', 'Tuesday', 'Wednesday','Thursday','Friday','Saturday',
                  'Sunday']
        hLabels = ['Alarms']
        self.table1.setVerticalHeaderLabels(vLabels)
        self.table1.setHorizontalHeaderLabels(hLabels)

        #make horizontal label fill panel
        headerH = self.table1.horizontalHeader()
        headerH.setSectionResizeMode(QHeaderView.Stretch)

        headerV = self.table1.verticalHeader()
        headerV.setSectionResizeMode(QHeaderView.Stretch)

        self.table2 = QTableWidget(mainWidget)
        #setRowCount number of columns for number of entries for that day
        self.table2.setRowCount(8)
        self.table2.setColumnCount(1)
        self.hLabels2 = ['Video Link File: ']
        self.table2.setHorizontalHeaderLabels(self.hLabels2)

        headerH2 = self.table2.horizontalHeader()
        headerH2.setSectionResizeMode(QHeaderView.Stretch)

        headerV2 = self.table2.verticalHeader()
        headerV2.setSectionResizeMode(QHeaderView.Stretch)

        widge1 =  QWidget()
        vbox = QVBoxLayout(mainWidget)
        vbox.addWidget(self.button1)
        vbox.addWidget(self.button2)
        widge1.setLayout(vbox)

        hbox = QHBoxLayout(mainWidget)
        hbox.addWidget(self.table1)
        hbox.addWidget(widge1)
        hbox.addWidget(self.table2)


        self.setGeometry(300,300,800,600)
        self.setFixedSize(800,600)
        self.setWindowTitle('Youtube Alarm Clock')
        self.show()


    def openNewAlarmWindow(self):
        self.popup = NewAlarmPopup()
        self.show()







if __name__ == '__main__':
    app = QApplication(sys.argv)
    mui = MainUI()
    sys.exit(app.exec_())
