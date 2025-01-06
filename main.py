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
from seleniumTest import scrape_company_data

# TO CONFIRM 输入文件路径
input_dir = "E:\data\企业电力数据\分片企业名单"  # 替换为你的文件路径
input_file = os.path.join(input_dir, f"enterprise_1.csv")

df = pd.read_csv(input_file)

# 将 DataFrame 转换为一维数组
enterprises_list = df.values.tolist()
enterprises = [item[0] for item in enterprises_list]

# 输出数组
print(f"Now processing {input_file}")
print("企业名单数组: ")
print(enterprises)
print(len(enterprises))

company_data_list = scrape_company_data(enterprises)

# TODO: 写进csv内






