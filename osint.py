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


        self.username_input.setFont(QFont('Arial',11))
        self.username_input.returnPressed.connect(self.search_username)
        self.username_input.setStyleSheet("""
        background-color: #fff;
        border: 2px solid #ccc;
        padding: 10px;
        border-radius: 8px;
        color: #333;
        """)

        user_input_layout.addWidget(self.label)
        user_input_layout.addWidget(self.username_input)
        user_input_group.setLayout(user_input_layout)

        category_layout = QHBoxLayout()

        self.category_label = QLabel("Kategori Seçimi:")
        self.category_label.setFont(QFont('Arial',12,QFont.Bold))
        self.category_label.setStyleSheet("color: #333;")

        self.category_selector = QComboBox()
        self.category_selector.addItems([
            "Hepsi","Sosyal Medya", "Forumlar", "Video Platformları"
        ])
        self.category_selector.setFont(QFont('Arial',12))
        self.category_selector.setStyleSheet("""background-color: #fff;
        border: 2px solid #ccc;
        padding: 5px;
                                             border-radius: 8px;
        color: #333;
        """)
        category_layout.addWidget(self.category_label)
        category_layout.addWidget(self.category_selector)

        button_layout = QHBoxLayout()

        self.search_button = QPushButton("Ara")
        self.search_button.setFont(QFont('Arial',12))
        self.search_button.clicked.connect(self.search_username)
        self.search_button.setStyleSheet("""
        QPushButton{
        background-color: #4CAF50;
        color: white;
        padding: 10px;
        border-radius: 10px;
        font-weight: bold;
        border: none;
        }
        QPushButton:hover{
        background-color: #45a049;
        }
        """)
        #self.search_button.clicked.connect()

        self.save_button = QPushButton("Sonuçları Kaydet")
        self.save_button.setFont(QFont('Arial', 12))
        self.save_button.clicked.connect(self.save_results)
        self.save_button.setStyleSheet("""
        QPushButton{
        background-color: #008CBA;
        color: white;
        padding: 10px;
        border-radius: 10px;
        font-weight: bold;
        border: none;
        }
        QPushButton:hover{
        background-color: #007bb5;
        }
        """)
        button_layout.addWidget(self.search_button)
        button_layout.addWidget(self.save_button)