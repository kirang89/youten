#!/usr/bin/python
# encoding: utf-8

#
# Simple script to trigger creation of all the necessary
# databases and tables
#

from api import db

if __name__ == '__main__':
    db.create_all()