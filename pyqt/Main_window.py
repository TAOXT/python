import sys
#从转换的.py文件内调用类
from lable_test import Ui_MainWindow
from PyQt5 import QtWidgets

class myWin(QtWidgets.QWidget, Ui_MainWindow):
    global mstr
    def __init__(self):

        super(myWin, self).__init__()
        self.setupUi(self)
        self.pushButton_5.clicked.connect(self.changeText)

        self.pushButton_6.clicked.connect(self.addText)
        self.pushButton_7.clicked.connect(self.clear)

        self.radioButton.clicked.connect(self.OnlyRead)
        self.radioButton_2.clicked.connect(self.ReadAndWrite)

        # self.dial.valueChanged().connect(self.PrintValue)
        # self.lcdNumber.
        # self.lcdNumber



#实现按下按钮改变文字内容和颜色
    def changeText(self):
        self.label.setText("xxxx")
        self.label.setStyleSheet("color:blue")

#实现输出单行文本框的内容
    def PrintValue(self):
        print (self.lineEdit.text())

    # 实现从单行文本框中获取内容
    def getText(self):
        global mstr
        mstr=self.lineEdit.text()
    #  实现从单行文本中获得的内容在添加到多行文本框
    def setText(self):
        global mstr
        self.textBrowser.append(mstr)
        self.lineEdit.setText("")
        print(self.textBrowser.toPlainText())

    def addText(self):
        self.getText()
        self.setText()


    # 实现清空多行文本框
    def clear(self):
        self.textBrowser.clear()


    #实现当选择这个单选按钮的时候实现文本框为只读模式
    def OnlyRead(self):
        self.textBrowser_2.setReadOnly(True);

    #设置属性为读写模式
    def ReadAndWrite(self):
        self.textBrowser_2.setReadOnly(False)
    #
    def PrintValue(self):
        print(self.dial.value())





if __name__=="__main__":

    app=QtWidgets.QApplication(sys.argv)
    Widget=myWin()
    Widget.show()
    Widget.PrintValue()
  #  Widget.changeColor()
    sys.exit(app.exec_())