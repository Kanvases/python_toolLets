# python_toolLets
一个持续更新的小工具库
## KeepLooking.py
通过监视程序运行后输出的结果文件是否存在，来判断某个程序是否运行完了。若检测到该文件，会从**微信文件传输助手**给你发一条提醒。
### 使用之前
```
numpy install wxpy
```
使用python运行脚本或者打包成exe。
```
$ python KeepLooking.py /path/to/result1.txt /path/to/result2.txt 60
```
表示每60秒检测一次`result1.txt`和`result2.txt`是否存在。每检测到一个程序，都会收到一条对应的消息。
默认每10秒检测一次。
运行后需要扫码登录微信。
