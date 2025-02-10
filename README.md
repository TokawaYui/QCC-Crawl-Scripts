
# QCC-Crawl-Scripts
This repository is used to design a crawl bot to do some data mining on the QCC website.

## 使用方法：

1. **环境要求**：
   - 使用浏览器为 **Chrome 最新版**
   - 下载相应版本的 **ChromeDriver**（下载地址：[https://googlechromelabs.github.io/chrome-for-testing/#stable](https://googlechromelabs.github.io/chrome-for-testing/#stable)）
   - 确保 Chrome 浏览器已登录企查查账号

2. **运行脚本**：
   - 在命令行中运行脚本，并传入以下四个参数：
     ```bash
     python main.py --input_dir "输入文件夹路径" -r 当前批次编号 --ch_dir "ChromeDriver 路径" --data_dir "谷歌用户数据路径"
     ```
   - 示例：
     ```bash
     python main.py --input_dir "E:\data\企业电力数据\分片企业名单_20_re" -r 3 --ch_dir "C:\path\to\chromedriver.exe" --data_dir "C:\path\to\googleuserdata"
     ```

   - **参数说明**：
     - `--input_dir`：输入文件夹路径，用于指定包含企业名单 CSV 文件的目录。
     - `-r`：当前批次编号（整数）。
     - `--ch_dir`：ChromeDriver 的完整路径。
     - `--data_dir`：谷歌浏览器用户数据的完整路径。

3. **注意事项**：
   - 启动脚本时请关闭 Chrome 浏览器，脚本会自动打开 Chrome 浏览器并跳转到企查查网页。处理完弹窗后可以最小化到后台运行。
   - 每次爬取大约花费半小时。

## 爬取内容说明

- **输出文件**：
  - 脚本会在输入文件夹下自动创建一个 `output` 文件夹，用于保存企业信息数据（`company_info_num.csv`）和错误日志。

- **错误日志示例**：
  ```bash
  复旦大学 - 'bool' object has no attribute 'get'
  上海市浦东新区环境监测站 - 'bool' object has no attribute 'get'
  ```
  这种错误一般为事业单位，由于没有企查分直接跳过，无影响，可以无视。

- **访问限制错误示例**：
  ```bash
  上海美庆企业发展有限公司 - Message:
  Stacktrace:
  GetHandleVerifier [0x00007FF7F01980D5+2992373]
  (No symbol) [0x00007FF7EFE2BFD0]
  (No symbol) [0x00007FF7EFCC590A]
  (No symbol) [0x00007FF7EFD1926E]
  (No symbol) [0x00007FF7EFD1955C]
  (No symbol) [0x00007FF7EFD627D7]
  (No symbol) [0x00007FF7EFD3F3AF]
  (No symbol) [0x00007FF7EFD5F584]
  (No symbol) [0x00007FF7EFD3F113]
  (No symbol) [0x00007FF7EFD0A918]
  (No symbol) [0x00007FF7EFD0BA81]
  GetHandleVerifier [0x00007FF7F01F6A2D+3379789]
  GetHandleVerifier [0x00007FF7F020C32D+3468109]
  GetHandleVerifier [0x00007FF7F0200043+3418211]
  GetHandleVerifier [0x00007FF7EFF8C78B+847787]
  (No symbol) [0x00007FF7EFE3757F]
  (No symbol) [0x00007FF7EFE32FC4]
  (No symbol) [0x00007FF7EFE3315D]
  (No symbol) [0x00007FF7EFE22979]
  BaseThreadInitThunk [0x00007FFBCBBEE8D7+23]
  RtlUserThreadStart [0x00007FFBCC3FFBCC+44]
  ```
​		**这种则说明企查查已经到达了访问限制，没办法获取到企业内容，说明要隔8-10小时后再进行下一批次的爬取，**

## 注意事项

- 企查查有访问次数上限，一次爬取量为 20，建议每次爬取间隔时间为 8-10 小时。
- 确保所有路径配置正确，并且脚本有权限访问这些路径。




​	
