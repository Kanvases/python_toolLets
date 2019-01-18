import sys
import os
import time
from wxpy import Bot
import re

if __name__ == "__main__":
  # input format
  if(len(sys.argv)<2):
    print('input paramters:')
    print('1~N: path/to/your/not/existed/files.ext')
    print('N+1: delay seconed. 1~999. defalut as 10.')
  # collect all paths
  else:
    # if the last paramter is timer
    isnum=re.match('[1-9]{1,3}',sys.argv[-1])
    if isnum:
      dirFile=sys.argv[1:-1]
      delay=int(sys.argv[-1])
    else:
      dirFile=sys.argv[1:]
      delay=10
    
    # init wchat roboter
    bot = Bot(cache_path=True)
    print('Monitoring your programs:')
    for subPath in dirFile:
      print(subPath)
    bot.file_helper.send('开始监控程序啦~')

    #init 2 set of work
    unAchived=dirFile.copy()
    Achived=[]

    #main loop, while Achived not equal to all files.
    while(not len(Achived)==len(dirFile)):
      
    # detect each unachived file:
      for subPath in unAchived:

        if os.path.exists(subPath):
          bot.file_helper.send(subPath+" 运行完啦~")
          unAchived.remove(subPath)
          Achived.append(subPath)
        # delay.
        time.sleep(delay) 

    #got the all final result
    bot.file_helper.send("你的程序全部运行完啦~")
