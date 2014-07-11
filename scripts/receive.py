#!/usr/bin/env python
"""Receieved commands on robobonobo...

"""

from serial import Serial
from time import time
import signal
import sys

SERIAL_PORT = "/dev/tty02"
FLATLINE_TIME = 2


class Bonobo():
    angle = 0
    distance = 0
    command_function_map = {
        'k': "kill_switch",
    }

    def __init__(self):
        self.register_signals()
        self.last_heartbeat = time()

    def handle_command(self, command):
        self.command_function_map[command]()

    def kill_switch(self):
        #TODO    kill the motor
        pass

    def rotate(self, angle):
        pass

    def go_forward(self, distance):
        pass

    def move(self, heading, distance):
        angle = heading - 360 if heading > 180 else heading
        self.rotate(angle)
        self.go_forward(distance)

    def check_heartbeat(self):
        if time() - self.last_heartbeat > FLATLINE_TIME:
            self.kill_switch()

    def run(self):
        with Serial(SERIAL_PORT, 57600, timeout=1) as xbee:
            while True:
                self.check_heartbeat(self.last_heartbeat)
                command = xbee.read(1)
                print "COMMAND: ", command
                self.handle_command(command)

    def signal_handler(self, sig, frame):
        self.kill_switch()
        sys.exit(0)

    def register_signals(self):
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGABRT, self.signal_handler)
        signal.signal(signal.SIGALRM, self.signal_handler)


if __name__ == '__main__':
    bonobo = Bonobo()
    bonobo.run()
