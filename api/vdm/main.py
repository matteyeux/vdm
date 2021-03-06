#!/usr/bin/env python3
import sys
import logging
from vdm import api

"""Main module for vdm api."""

def main():
    logging.basicConfig(filename='vdm_error.log',level=logging.DEBUG)
    if len(sys.argv) == 2 and sys.argv[1] == "-s":
        context = ('vdm_certs/fullchain.pem', 'vdm_certs/privkey.pem')
        api.app.run(host='0.0.0.0', ssl_context=context)
    else:
        api.app.run(host='0.0.0.0', debug=True)


if __name__ == '__main__':
    main()
