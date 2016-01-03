# python
记录自己的python语言学习历程

- mac上通过homebrew安装好wpython之后,执行程序竟然报错:` ImportError: No module named wx`...经过排查原来是wxpython没有注册环境变量,解决如下:
```
export PYTHONPATH=$PYTHONPATH:/usr/local/Cellar/wxpython/3.0.0.0/lib/python2.7/site-pac‌​kages/wx-3.0-osx_cocoa
```