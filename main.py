from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
from twisted.internet.defer import inlineCallbacks


class Brainie(ApplicationSession):

    @inlineCallbacks
    def onJoin(self, details):
        print('WAMP WAMP! connected')

        # CHAT REPLY
        url = 'com.theb0ardside.onchat'

        def chatreply(msg):
            print('Yow! sensory input is working - received {0}'.format(msg))
            return 'hola\n'
        try:
            yield self.register(chatreply, url)
            print('"Reply" function registered as {0}'.format(url))
        except Exception as e:
            print('Something fucked up, mate: {0}'.format(e))

# def main():
#
#    # enter event loop, receive notifications of events
#    # philosohize on them
#    # try different combinations of things and relationships
#    thing1 = Thing()
#    thing2 = Thing()
#    ev = Event([thing1, thing2])
#    print ev.replay()
#    print ev.getThings()


if __name__ == '__main__':
    print 'Bzzzt.. I\'m alive!'
    runner = ApplicationRunner(url=u'ws://localhost:8080/ws', realm=u'thingie')
    runner.run(Brainie)
