#!/usr/bin/python
import sys
from reader import barcode_reader
from runMenu import Run_Menu


if __name__ == '__main__':
    try:
        Run_Menu()
    except KeyboardInterrupt:
        pass
