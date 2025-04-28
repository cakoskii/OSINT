import sys
import asyncio  #asenkron programlama,aynı anda birden fazla işin ilerlemesini sağlar
import aiohttp  #kullanıcıya istek gönderirken kullanılır(bulmak için)
import ssl
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
                             QLineEdit, QLabel, QFileDialog, QGroupBox, QTextBrowser, QDesktopWidget, QProgressBar,
                             QComboBox, QMessageBox)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QTextCursor, QIcon, QPixmap


class DedektifUygulama(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dedektif")
        self.setWindowIcon(QIcon('icon.ico'))
        self.initUI()
        
    


