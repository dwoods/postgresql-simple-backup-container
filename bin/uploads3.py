#!/usr/bin/python

import sys
import getopt
import time
import tinys3
from datetime import timedelta

def main(argv):
  accessKey = ''
  secretKey = ''
  file = ''
  try:
    opts, args = getopt.getopt(argv,"ha:s:f:",["access_key=","secret_key=", "file="])
  except getopt.GetoptError:
    print 'uploads3.py -a <access_key> -s <secret_key> -f <file>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'uploads3.py -a <access_key> -s <secret_key> -f <file>'
      sys.exit()
    elif opt in ("-a", "--access_key"):
      accessKey = arg
    elif opt in ("-s", "--secret_key"):
      secretKey = arg
    elif opt in ("-f", "--file"):
      file = arg

  ## Creating a simple connection
  conn = tinys3.Connection(accessKey, secretKey)
  date = time.strftime("%Y%m%d%H%M")
  ## Uploading a single file
  f = open(file,'rb')
  t = timedelta(days=5)
  conn.upload(date + '-backup.sql.gz', f, bucket='bixgitlab', expires=t)

if __name__ == "__main__":
   main(sys.argv[1:])
