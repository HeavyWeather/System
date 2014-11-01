def delay(t):
  ''' delay whatever needs to happen next by time 't' in seconds, 
  usually until the wee hours when server load is lower. '''

  import time
  import os
  time.sleep(t)
  os.system('echo "Okay, here we go!"')
