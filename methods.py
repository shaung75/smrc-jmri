# This is an example script for a JMRI "Automat" in Python
# It is based on the AutomatonExample.
#
# It listens to two sensors, running a locomotive back and
# forth between them by changing its direction when a sensor
# detects the engine.
#
# Author:  Howard Watkins, January 2007.
# Part of the JMRI distribution

import jarray
import jmri

class Test14(jmri.jmrit.automat.AbstractAutomaton) :

    def init(self):
        # init() is called exactly once at the beginning to do
        print "Inside init(self)"

        self.route = 1

        return

    def handle(self):
        # handle() is called repeatedly until it returns false.
        #print "Inside handle(self)"

        self.setRoute()

        return 1

    def setRoute(self):
        print self.route

        if(self.route == 3):
            self.route = 1
        else:
            self.route += 1


# end of class definition

# start one of these up
Test14().start()
