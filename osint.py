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
        
    def initUI(self):
        main_layout = QVBoxLayout()

        user_input_group = QGroupBox("Kullanıcı Adı Ara (Virgülle ayırarak birden fazla arayabilirisiniz.")
        user_input_group.setStyleSheet("""
        QGroupBox {
        border: 2px solid #8f8f91;
        border-radius: 10px;
        margin-top: 20px;
        padding: 10px;
        background-color: #f9f9f9;
        }
        QGroupBox::title {
        subcontrol-origin: margin;
        subcontrol-position: top center;
        padding: 0 10px;
        font-size: 14pt;
        font-weight: bold;
        color: #333;
        }
        """)
        user_input_layout = QVBoxLayout()
        self.label = QLabel("Kullanıcı Adı Girin:")
        self.label.setFont(QFont('Arial',12,QFont.Bold))
        self.label.setStyleSheet("color: #333;")

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText(
            "Kullanıcı adlarını virgülle ayırarak girin (örnek: kullanıcı1, kullanıcı2)"
        )


