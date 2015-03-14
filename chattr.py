from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
from autobahn.twisted.util import sleep

from things.dictionary import Event, Thing


class Chat(ApplicationSession):

    @inlineCallbacks
    def onJoin(self, details):
        print 'ON joinged!'

        # PUBLISH and CALL every second .. forever
        #
        while True:

            # PUBLISH an event
            #
            thing1 = {}
            thing2 = {}
            #event = {'things' : {thing1, thing2}}
            #thing2 = Thing()
            #ev = Event([thing1, thing2])

            try:
                yield self.publish('com.theb0ardside.onchat', thing1)
                print("published to 'onchat' with ev {}".format(thing1))
            except Exception as e:
                print('Something fucked up, mate: {0}'.format(e))

            yield sleep(1)

if __name__ == '__main__':
    print 'Chazbot starting up'
    runner = ApplicationRunner(url=u'ws://localhost:8080/ws', realm=u'thingie')
    runner.run(Chat)
