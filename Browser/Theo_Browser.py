import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import*


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://www.google.com'))  #this is my url that will be used when u enter my browser
        self.setCentralWidget(self.browser)
        self.showMaximized()   #this part makes my browser  to be maximized
        
        #navbar
        navbar = QToolBar()
        self.addToolBar(navbar)
        #button for back
        back_btn = QAction('Back',self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)
        #forward button for my browser
        forward_btn = QAction('Forward',self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)
        #reload button for my browser
        reload_btn = QAction('Reload',self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)
        
        home_btn = QAction('Home',self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)
        
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar) 


    #this function is used for taking my browser to home
    
    def navigate_home(self):
        self.browser.setUrl(QUrl('http://www.google.com'))
    
    #this function is done so it can take any url inserted in my browser and serch it 
    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))
    
    
app = QApplication(sys.argv)
QApplication.setApplicationName('Theo_Browser')
window = MainWindow()
app.exec_()
