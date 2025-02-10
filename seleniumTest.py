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
import random
import csv
from datetime import datetime
from htmlHandler import extract_company_info


def scrape_company_data(enterprises_list, output_dir, round_num, ch_dir, data_dir):
    # 错误日志
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    failed_companies_file = os.path.join(output_dir, f"failed_companies_{round_num}_{timestamp}.log")  # 带时间戳的文件名)
    # 输出csv
    enterprise_info_csv = os.path.join(output_dir, f'company_info_{round_num}.csv')

    # 设定表头
    fixed_info = {
        "UID": "",
        "户号": "",
        "企业名称": "",
        "统一社会信用代码": "",
        "企业规模": "",
        "企查分": "",
        "企业标签": "",
        "登记状态": "",
        "成立日期": "",
        "营业期限": "",
        "纳税人资质": "",
        "注册资本": "",
        "实缴资本": "",
        "企业类型": "",
        "人员规模": "",
        "参保人数": "",
        "国标行业": "",
        "经营范围": ""
    }

    # 检查文件是否存在，如果不存在则创建文件并写入表头
    file_exists = os.path.exists(enterprise_info_csv)
    with open(enterprise_info_csv, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fixed_info.keys())

        # 如果文件不存在，则写入表头
        if not file_exists:
            writer.writeheader()

    # TODO： 设置ChromeDriver路径
    # 设置 ChromeDriver 路径
    # chrome_driver_path = r'D:\Chrome\chromedriver-win64-133\chromedriver-win64\chromedriver.exe'  # 替换为你的 Chromedriver 路径
    chrome_driver_path = ch_dir
    # 创建 ChromeOptions 对象
    options = Options()
    # TODO： 设置谷歌用户数据路径
    # options.add_argument('--user-data-dir=C:/Users/86183/AppData/Local/Google/Chrome/User Data')  # 替换为你的 Chrome 配置路径
    options.add_argument('--user-data-dir={}'.format(data_dir))  # 你的 Chrome 配置路径
    options.add_argument('--profile-directory=Default')  # 如果你使用默认用户配置

    # 初始化 WebDriver
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    # 打开网页
    driver.get("https://www.qcc.com")
    time.sleep(10)  # 等待页面加载完成

    company_data_list = []  # 用于存储所有公司的数据

    for item in enterprises_list:
        # company_uid = item[0]
        company_name = item[1]
        # company_num = item[2]
        try:
            # driver.get("https://www.qcc.com")
            time.sleep(random.randint(30, 60))
            # 在搜索框内输入企业名字进行搜索
            search_box = driver.find_element(By.ID, "searchKey")
            search_box.clear()  # 清空搜索框
            search_box.send_keys(company_name)

            search_button = driver.find_element(By.XPATH, '//button[@type="button" and contains(@class, "btn-primary")]')
            search_button.click()

            time.sleep(random.randint(15, 20))  # 等待搜索结果加载

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

            # 打印目标页面标题
            print("目标页面标题:", driver.title)

            # 获取页面源代码
            time.sleep(random.randint(10, 15))
            page_source = driver.page_source
            # print(page_source)

            # 提取公司信息
            company_data = extract_company_info(item, page_source)
            # 将提取到的公司信息与表头格式化
            company_data_with_fixed_info = {key: company_data.get(key, "") for key in fixed_info.keys()}

            # TODO: 在这里就尝试csv的写入
            # 追加公司数据到 CSV 文件
            with open(enterprise_info_csv, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=fixed_info.keys())
                writer.writerow(company_data_with_fixed_info)

            # 添加到公司数据列表中
            company_data_list.append(company_data)

        # 记录处理成功的公司和处理失败的公司，方便补充数据
        except Exception as e:
            print(f"处理 {company_name} 时发生错误: {e}")
            # 错误处理,把出错的公司名字记录到一个log文件内
            with open(failed_companies_file, "a") as f:
                f.write(f"{company_name} - {str(e)}\n")

            driver.get("https://www.qcc.com")
            continue  # 如果某个公司出错，继续处理下一个

        # 回到首页
        driver.get("https://www.qcc.com")

    driver.quit()  # 退出 WebDriver

    # 返回所有公司数据
    return company_data_list


# # Test Code
# # 调用函数并传入企业名称数组
# test_enterprises = ['阿里巴巴']
# company_info = scrape_company_data(test_enterprises)
#
# # 打印所有提取到的公司数据
# for data in company_info:
#     for key, value in data.items():
#         print(f"{key}: {value}")





