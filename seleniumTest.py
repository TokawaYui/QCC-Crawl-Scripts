from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import os
from htmlHandler import extract_company_info

# 设置 ChromeDriver 路径
chrome_driver_path = r'D:\Chrome\chromedriver-win64\chromedriver.exe'  # 替换为你的 Chromedriver 路径

# 创建 ChromeOptions 对象
options = Options()
options.add_argument('--user-data-dir=C:/Users/86183/AppData/Local/Google/Chrome/User Data')  # 替换为你的 Chrome 配置路径
options.add_argument('--profile-directory=Default')  # 如果你使用默认用户配置

# 初始化 WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# 已经提前在chrome上登录，然后获取用户信息，在这里打开网页就可以不用登录
driver.get("https://www.qcc.com")

time.sleep(10)

# TODO: 根据企业名单进入一个大循环
# 输入文件路径
input_dir = "E:\data\企业电力数据\分片企业名单"  # 替换为你的文件路径
input_file = os.path.join(input_dir, f"enterprise_1.csv")
# 读取 CSV 文件
df = pd.read_csv(input_file)

# 将 DataFrame 转换为数组（列表形式）
data_array = df.values.tolist()

# 输出数组
print("企业名单数组：")
print(data_array)


# 在搜索框内输入企业名字进行搜索
search_box = driver.find_element(By.ID, "searchKey")  # 替换为搜索框的 XPath
search_box.send_keys("阿里巴巴")  # 替换为实际公司名称

search_button = driver.find_element(By.XPATH, '//button[@type="button" and contains(@class, "btn-primary")]')  # 根据按钮的类型和类定位
search_button.click()

time.sleep(10)


# 进入搜索得到的第一个结果
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'title.copy-value'))
)
first_result = driver.find_element(By.CLASS_NAME, 'title.copy-value')

# 提取链接并跳转
first_result_link = first_result.get_attribute('href')
print(f"第一条结果链接: {first_result_link}")
driver.get(first_result_link)  # 打开链接

# 等待目标页面加载完成
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, 'body'))
)

# 打印目标页面标题或其他内容
print("目标页面标题:", driver.title)
# code here

# 把结果的html输出
time.sleep(10)
print(driver.page_source)

# TODO：目前已经进入了目标页面，该如何获取html信息呢
company_data = extract_company_info(driver.page_source)

# 打印提取到的信息
for key, value in company_data.items():
    print(f"{key}: {value}")

driver.quit()





