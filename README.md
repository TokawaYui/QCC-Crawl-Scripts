# QCC-Crawl-Scripts
This repository is used to design a crawl bot to do some data mining on QCC website



**使用方法：**

​	使用浏览器为**Chrome最新版**，并且下载相应版本的**ChromeDriver**

​	**ChromeDriver**下载地址：https://googlechromelabs.github.io/chrome-for-testing/#stable

​	在Chrome打开企查查网页，并**完成登录后**，再执行本项目main函数即可。启动脚本时请关闭Chrome浏览器，main函数执行后会自动打开Chrome浏览器，并跳到企查查的网页，把不必要的遮挡弹窗关闭后，最小化到后台即可。

​	每次爬取大概花费半小时左右。



**爬取内容说明**：

​	代码会在output_dir输出企业信息数据，company_info_num.csv和错误日志。

​	错误日志内容：

​		1、

​		复旦大学 - 'bool' object has no attribute 'get'
​		上海市浦东新区环境监测站 - 'bool' object has no attribute 'get'

​		**这种一般为事业单位，由于没有企查分直接跳过，没有影响，可以无视。**

​		2、

​		上海美庆企业发展有限公司 - Message: 

​		Stacktrace:
​			GetHandleVerifier [0x00007FF7F01980D5+2992373]
​			(No symbol) [0x00007FF7EFE2BFD0]
​			(No symbol) [0x00007FF7EFCC590A]
​			(No symbol) [0x00007FF7EFD1926E]
​			(No symbol) [0x00007FF7EFD1955C]
​			(No symbol) [0x00007FF7EFD627D7]
​			(No symbol) [0x00007FF7EFD3F3AF]
​			(No symbol) [0x00007FF7EFD5F584]
​			(No symbol) [0x00007FF7EFD3F113]
​			(No symbol) [0x00007FF7EFD0A918]
​			(No symbol) [0x00007FF7EFD0BA81]
​			GetHandleVerifier [0x00007FF7F01F6A2D+3379789]
​			GetHandleVerifier [0x00007FF7F020C32D+3468109]
​			GetHandleVerifier [0x00007FF7F0200043+3418211]
​			GetHandleVerifier [0x00007FF7EFF8C78B+847787]
​			(No symbol) [0x00007FF7EFE3757F]
​			(No symbol) [0x00007FF7EFE32FC4]
​			(No symbol) [0x00007FF7EFE3315D]
​			(No symbol) [0x00007FF7EFE22979]
​			BaseThreadInitThunk [0x00007FFBCBBEE8D7+23]
​			RtlUserThreadStart [0x00007FFBCC3FFBCC+44]

​		**这种则说明企查查已经到达了访问限制，没办法获取到企业内容，说明要隔8-10小时后再进行下一批次的爬取，**



注意事项：

​	企查查有访问次数上限，一次爬取量为20，爬取间隔为8-10小时较好；

​	**main.py**中修改**input_dir**和**output_dir**，修改为存放企业分片名单的目录即可

​	**seleniumTest.py**中修改**chrome_driver_path**和**options.add_argument**

​	以我自己电脑为例：Chrome浏览器数据默认存放在`C:/Users/86183/AppData/Local/Google/Chrome/User Data`下

​	
