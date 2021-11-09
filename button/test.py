#!/usr/bin/python

import time
import sys

forever = 1;

while forever:
  for i in range(10):
    print i,
    sys.stdout.flush()
    time.sleep(0.1)
