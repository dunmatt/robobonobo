#!/usr/bin/env python
"""Send sends commands to robobonobo... or anything else on a serial port for that matter.

Usage:
  ./send.py heartbeat
  ./send.py -c <command> [options]

Options:
  -c=<command>          Sets the command to send.
  -d=<delay>            Sets the duration before sending the command.  [default: 1]
  -h, --help            Show this help screen.
  -l=<lifetime>         Lifetime of the test, the total duration of the heartbeat.  [default: 300]
  -p=<port>             Serial port name  [default: /dev/tty.usbserial-AD02FLVJ]
  --version             Show the version.
"""

from serial import Serial
from time import sleep, time  # YAY! sleep time!

def sendCommand(command, port, delay, lifetime):
  startTime = time()
  sendTime = startTime + delay
  endTime = startTime + lifetime
  now = startTime
  with Serial(port, 57600, timeout=1) as xbee:
    # TODO: launch a thread to read from xbee and print whatever comes through
    xbee.close()
    xbee.open()
    while now < endTime:
      if command and sendTime < now:
        xbee.write(command)
        command = None  # ensures the command is only sent once
      xbee.write("1")  # send heartbeat
      sleep(.33)
      now = time()


if __name__ == '__main__':
  from docopt import docopt
  args = docopt(__doc__, version="Robobonobo command sender v1")
  # print(args)
  if args["heartbeat"]:
    sendCommand(None, args["-p"], float(args["-d"]), float(args["-l"]))
  else:
    sendCommand(args["-c"], args["-p"], float(args["-d"]), float(args["-l"]))
