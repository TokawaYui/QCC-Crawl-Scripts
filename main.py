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
import argparse
import os
import pandas as pd

def main():
    # 创建参数解析器
    parser = argparse.ArgumentParser(description='QCC Scape Crawl Parameters')
    
    # 添加参数
    parser.add_argument('--input_dir', type=str, required=True, help='输入文件夹路径')
    parser.add_argument('-r', type=int, required=True, help='当前批次编号')
    parser.add_argument('--ch_dir', type=str, required=True, help='ChromeDriver 路径')
    parser.add_argument('--data_dir', type=str, required=True, help='谷歌用户数据路径')
    
    # 解析参数
    args = parser.parse_args()
    
    print("QCC Scape Crawl Starting......")
    
    # 获取输入文件
    input_file = os.path.join(args.input_dir, f"enterprise_{args.r}.csv")
    output_dir = os.path.join(args.input_dir, 'output')
    
    print(f"Now processing {input_file}")
    
    df = pd.read_csv(input_file)
    
    # 将 DataFrame 转换为一维数组
    enterprises_list = df.values.tolist()
    enterprises = [item[0] for item in enterprises_list]
    
    # 输出数组
    print("Enterprises: ")
    print(enterprises_list)
    print(len(enterprises_list))
    
    print("Start Scraping the data")
    company_data_list = scrape_company_data(enterprises_list, output_dir, args.r, args.ch_dir, args.data_dir)
    
    print(company_data_list)

if __name__ == "__main__":
    main()







