from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
from twisted.internet.defer import inlineCallbacks

from things.dictionary import Event, Thing


class Brainie(ApplicationSession):

    @inlineCallbacks
    def onJoin(self, details):
        print('WAMP WAMP! connected')

        def omg(msg):
            print('Yow! sensory input is working - received {0}'.format(msg))

        try:
            yield self.subscribe(omg, 'com.theb0ardside.onchat')
            print('Subscribed to topic \'chat\'')
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
