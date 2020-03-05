#!/usr/bin/python
import sys
from reader import barcode_reader
from lookup import UPC_lookup


if __name__ == '__main__':
    try:
        UPC_lookup("J41G78S1608A06JH")
    except KeyboardInterrupt:
        pass
