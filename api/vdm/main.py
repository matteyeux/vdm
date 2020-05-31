#!/usr/bin/env python3

from vdm import __version__
from vdm import api
from vdm import errors

"""Main module for vdm api."""

def main():
    api.app.run(host='0.0.0.0', debug=True)


if __name__ == '__main__':
    main()
