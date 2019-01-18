#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import sys
import os
import time
from wxpy import Bot

if __name__ == "__main__":
  if(len(sys.argv)<2 or os.path.exists(sys.argv[1])):
    print('input a path to your final result(not exists now), or input file existed already.')
  else:
    dirFile=sys.argv[1]
    try:
      delay=int(sys.argv[2])
    except:
      delay=10
    bot = Bot(cache_path=True)
    print('Monitoring your program')
    #main loop
    while(not os.path.exists(dirFile)):
      time.sleep(delay)
    #got the final result
    bot.file_helper.send("你的程序运行完啦~")
