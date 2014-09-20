#!/usr/bin/python
# encoding: utf-8
#
# Simple script to trigger deletion of tables
#

from api import db

if __name__ == '__main__':
    db.drop_all()
