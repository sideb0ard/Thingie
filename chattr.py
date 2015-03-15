import SocketServer
import threading

import chan
from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner


listenaddr = '0.0.0.0'
listenport = 5050

c = chan.Chan()


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
        pass


class Chat(ApplicationSession):

    @inlineCallbacks
    def onJoin(self, details):
        print 'ON joinged!'

        while True:
            voice = c.get()
            reply = yield self.call('com.theb0ardside.onchat', voice)
            c.put(reply)
            print reply


def startWAMP():
    runner = ApplicationRunner(url=u'ws://localhost:8080/ws',
                               realm=u'thingie')
    runner.run(Chat)


class chatbot(SocketServer.BaseRequestHandler):

    def handle(self):

        print "Client connected with ", self.client_address
        data = 'init_placeholder'
        while len(data):
            data = self.request.recv(1024)
            c.put(data)
            self.request.send(c.get())
        print "Client exited"
        self.request.close()


def start_tcp():
    t = ThreadedTCPServer((listenaddr, listenport), chatbot)
    print 'Hit me up, bra .. {0}:{1}'.format(listenaddr, listenport)
    t.serve_forever()


def main_loop():

    # TCP chat
    th = threading.Thread(target=start_tcp)
    th.daemon = True
    th.start()

    # WAMP
    startWAMP()


if __name__ == '__main__':
    print 'ChatbotServer starting up'
    main_loop()
