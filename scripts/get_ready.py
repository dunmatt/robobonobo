#!/usr/bin/env python
"""Robobonobo setup script.

Usage:
  ./get_ready.py [options]

Options:
  -h, --help        Show this help screen
  --version         Show the version.
"""

from docopt import docopt
from glob import glob
import os

GPIOS = [30, 31, 112, 113, 65, 27]
GPIO_BASE = "/sys/class/gpio"
SLOTS_GLOB = "/sys/devices/bone_capemgr.?/slots"


def write_gpio(filename, msg, pindir=""):
    with open(os.path.join(GPIO_BASE, pindir, filename), mode="w+") as ex:
        ex.write(msg)


def setup_gpio(pin):
    write_gpio("export", pin)
    pindir = "gpio" + pin
    write_gpio("direction", "out", pindir)
    write_gpio("value", "0", pindir)


def setup_dto():
    for match in glob(SLOTS_GLOB):
        with open(match, mode="w+") as slots:
            slots.write("robobonobo")


def main():
    for gpio in GPIOS:
        setup_gpio(str(gpio))
    setup_dto()


if __name__ == "__main__":
    args = docopt(__doc__, version="Robobonobo setup script v1")
    main()
