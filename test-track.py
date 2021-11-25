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

        # Set loco address. For long address change "False" to "True"
        self.throttle = self.getThrottle(4, False)

        # Initial route to be set
        self.route = 1

        # set up sensor numbers
        # fwdSensor is reached when loco is running forward
        self.headshunt = sensors.provideSensor("CS1")
        self.branch1 = sensors.provideSensor("CS2")
        self.branch2 = sensors.provideSensor("CS3")
        self.branch3 = sensors.provideSensor("CS4")

        return

    def handle(self):

        self.setRoute()

        print "Set Loco Forward"
        self.throttle.setIsForward(True)

        self.waitMsec(1000)
        print "Set Speed"
        self.throttle.setSpeedSetting(0.7)

        print "Wait for Branch",self.route," Sensor"
        self.waitSensorActive(self.branch1)
        #self.waitMsec(10000)
        print "Set Speed Stop"
        self.throttle.setSpeedSetting(0)

        print "wait 5 seconds"
        self.waitMsec(5000)

        self.soundWhistle()

        print "Set Loco Reverse"
        self.throttle.setIsForward(False)
        self.waitMsec(1000)                 # wait 1 second for Xpressnet to catch up
        print "Set Speed"
        self.throttle.setSpeedSetting(0.7)

        print "Wait for Headshunt Sensor"
        self.waitSensorActive(self.headshunt)
        #self.waitMsec(10000)
        print "Set Speed Stop"
        self.throttle.setSpeedSetting(0)

        print "wait 5 seconds"
        self.waitMsec(5000)          # wait for 20 seconds

        self.soundWhistle()

        if(self.route == 3):
            self.route = 1
        else:
            self.route += 1

        return 1

    def setRoute(self):
        print "Setting route ", self.route

        if(self.route == 1) :
            turnouts.provideTurnout("CT1").setState(CLOSED)
            turnouts.provideTurnout("CT3").setState(CLOSED)
        elif(self.route == 2) :
            turnouts.provideTurnout("CT1").setState(THROWN)
            turnouts.provideTurnout("CT3").setState(CLOSED)
        elif(self.route == 3) :
            turnouts.provideTurnout("CT3").setState(THROWN)

    def soundWhistle(self):
        # Sound the whistle
        print "Sounding Whistle"
        self.throttle.setF3(True)     # turn on whistle
        self.waitMsec(1000)           # wait for 1 seconds
        self.throttle.setF3(False)    # turn off whistle
        self.waitMsec(1000)           # wait for 1 second


# end of class definition

# start one of these up
Test14().start()
