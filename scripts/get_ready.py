#!/usr/bin/env python
"""Robobonobo setup script.

Usage:
  ./get_ready.py [options]

Options:
  -h, --help        Show this help screen
  --version         Show the version.
"""

import os

gpios = [30, 31, 112, 113, 65, 27]
gpioBase = "/sys/class/gpio"


def setupGpio(pin):
  with open(os.path.join(gpioBase, "export"), mode="w+") as ex:
    ex.write(pin)
  pindir = "gpio" + pin
  with open(os.path.join(gpioBase, pindir, "direction"), mode="w+") as d:
    d.write("out")
  with open(os.path.join(gpioBase, pindir, "value"), mode="w+") as val:
    val.write("0")



def main():
  for gpio in gpios:
    setupGpio(str(gpio))

def __name__ == "__main__":
  from docopt import docopt
  args = docopt(__doc__, version="Robobonobo setup script v1")
  main()
