from alphadock.helper import *

import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        
        super(Ui, self).__init__() # Call the inherited classes __init__ method

        uic.loadUi('untitled.ui', self) # Load the .ui file
        
        UIFunctions.update_style_(self)
        UIFunctions.definitions_(self)
        UIFunctions.update_menus_(self)

        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)        
        self.pushButton_close.clicked.connect(lambda: self.close())
        self.pushButton_minimze.clicked.connect(lambda: self.showMinimized())
        self.dragPos = QtCore.QPoint()

        self.pushButton_1.clicked.connect(self.add_menu)
        self.pushButton_2.clicked.connect(self.clear_menu)
        self.a = 1

        self.show()
        

    def add_menu(self):
        self.menuhistory.addAction(str(self.a))
        self.a += 1

    def clear_menu(self):
        pass

    #https://stackoverflow.com/questions/63667232/how-to-move-window-when-dragging-frame-pyqt5
    def mousePressEvent(self, event): 
        self.dragPos = event.globalPos()
        
    def mouseMoveEvent(self, event):                                  
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()   

    
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()