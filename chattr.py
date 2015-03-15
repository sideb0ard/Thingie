import socket
import select

from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner


listenaddr = '0.0.0.0'
listenport = 5050


class Chat(ApplicationSession):

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((listenaddr, listenport))
    server.listen(5)

    print 'Hit me up, bra .. {0}:{1}'.format(listenaddr, listenport)

    @inlineCallbacks
    def onJoin(self, details):
        print 'ON joinged!'

        while True:
            try:
                client_socket, addr = self.server.accept()
                while True:
                    try:
                        client_socket.send('<CHATBOT:#> ')
                        # now wait..
                        msg = ''
                        ready = select.select([client_socket], [], [], 3)
                        if ready[0]:
                            msg += client_socket.recv(1024)
                        response = yield self.call('com.theb0ardside.onchat',
                                                   msg)
                        print 'Response: {0}'.format(response)
                        client_socket.send(response)
                    except socket.error:
                        client_socket.close()
            except Exception as e:
                print('Something fucked up, mate: {0}'.format(e))


if __name__ == '__main__':
    print 'ChatbotServer starting up'
    runner = ApplicationRunner(url=u'ws://localhost:8080/ws',
                               realm=u'thingie')
    runner.run(Chat)
