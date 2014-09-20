#!/usr/bin/env python
# encoding: utf-8

import os
import readline
from flask import *
from api import app, db
from api.models import *

os.environ['PYTHONINSPECT'] = 'True'
