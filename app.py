from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

driver = webdriver.Firefox()
url = "https://docs.google.com/presentation/d/1Ys9PpFA6xJmUlu2jbCazm7ueS9bcyl4sS6tDeZTKM1Y/present#slide=id.g114d98707c_0_6"
# ^ this is a slides presentation in presentation mode
driver.get(url)
slide_class = "punch-viewer-container"
page = driver.find_elements_by_class_name(slide_class)[0]

RIGHT = Keys.ARROW_RIGHT
LEFT = Keys.ARROW_LEFT

class SimpleEcho(WebSocket):

    def handleMessage(self):
    	if(self.data == "right"):
        	page.send_keys(RIGHT)
        elif(self.data == "left"):
        	page.send_keys(LEFT)
        self.sendMessage(self.data)

    def handleConnected(self):
        print self.address, 'connected'

    def handleClose(self):
        print self.address, 'closed'

server = SimpleWebSocketServer('', 8000, SimpleEcho)
server.serveforever()

#ngrok it then set up the web socket in the js