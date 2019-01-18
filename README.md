# python_toolLets
一个持续更新的小工具库
## KeepLooking.py
通过监视程序运行后输出的结果文件是否存在，来判断某个程序是否运行完了。若检测到该文件，会从**微信文件传输助手**给你发一条提醒。
### 使用之前

```
numpy install wxpy
```
把`#!`部分改成自己的python3解释器，把`KeepLooking.py`加到PATH.
```
$ KeepLooking.py /path/to/your/final/result.txt 60
```
表示每60秒检测一次`result.txt`是否存在。默认为10。
运行后需要扫码登录微信。
