#find ip from ipvoid.com
# by DMS
###########################
import requests 
from bs4 import BeautifulSoup as bs

def get_ipaddr(hostname):
    serviceurl = "https://www.ipvoid.com/find-website-ip/"
    payload = {
               'website':hostname,
               'websiteAddr':hostname,
              }
    html = requests.post(serviceurl, data=payload).content
    soup = bs(html,'html.parser')
    textarea = soup.find('textarea').text
    res = []
    for r in textarea.split('\n'):
        res.append(r.split(' ')[0])
    return res

def runQt():
    from PyQt6 import uic
    from PyQt6.QtWidgets import QMainWindow,QApplication,QLineEdit,QPlainTextEdit, QFrame,QLabel,QVBoxLayout
    import sys
    
    class UI(QMainWindow):
        def __init__(self):
            super(UI,self).__init__()
            #print('test here')
            uic.loadUi('ipvoid-find-ip.ui',self)
            
            self.get_children()
            
            self.show()
        
        def get_children(self):
            self.frame = self.findChild(QFrame,'frame2')
            self.layout = QVBoxLayout(self.frame)
            self.resultTE =self.findChild(QPlainTextEdit,'resultTE')
            self.hostnameLE = self.findChild(QLineEdit,'hostnameLE')
            self.hostnameLE.returnPressed.connect(self.on_pressed)
        
        def on_pressed(self):
            self.resultTE.setPlainText('')
            hostname = self.hostnameLE.text()
            res = get_ipaddr(hostname)
            print(res)
            for r in res:
                data = r+'\t'+hostname.strip()
                print(data)
                self.resultTE.appendPlainText(data)

    app = QApplication(sys.argv)
    UIWindow = UI()
    app.exec()
            
            
if __name__ == '__main__':
    #print(get_ipaddr('www.google.com'))
    runQt()