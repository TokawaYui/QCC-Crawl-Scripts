from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
import time
import selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 保持会话
sess = requests.session()

# 添加headers
afterLogin_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
}

# 登录操作
login = {'user': '18319752638', 'password': 'fgasdh123'}

driver = webdriver.Chrome(executable_path='D:\Chrome\chromedriver-win64\chromedriver.exe')  # 替换为实际路径


def login_qichacha():
    try:
        # 打开企查查登录页面
        driver.get("https://www.qcc.com")
        time.sleep(2)  # 等待页面加载完成

        # 定位到输入框
        username_input = driver.find_element(By.NAME, "username")
        password_input = driver.find_element(By.NAME, "password")

        # 输入账号密码
        username_input.send_keys("18319752638")
        password_input.send_keys("fgasdh123")

        # 等待用户手动完成验证码输入
        print("请手动输入验证码并完成登录操作")
        time.sleep(30)  # 等待用户手动输入验证码

        # 登录完成
        print("登录完成")
        return True
    except Exception as e:
        print(f"登录失败: {e}")
        return False


# 调用函数
if login_qichacha():
    # 登录后可以使用 Selenium 执行查询等操作
    driver.get("https://www.qcc.com/search?key=腾讯")
    time.sleep(5)
    print(driver.page_source)  # 获取当前页面内容
else:
    print("登录失败")


try:
    login_response = sess.post('https://www.qcc.com', data=login, headers=afterLogin_headers)
    if login_response.status_code == 200:
        print("Login successful")
    else:
        print("Login failed, status code:", login_response.status_code)
except Exception as e:
    print(f"Login exception: {e}")


def get_company_message(company):
    try:
        # 查询公司信息页面
        search = sess.get(f'https://www.qcc.com/search?key={company}', headers=afterLogin_headers, timeout=10)
        search.raise_for_status()
        search.encoding = 'utf-8'
        soup = BeautifulSoup(search.text, features="html.parser")
        href = soup.find_all('a', {'class': 'title'})[0].get('href')

        # 确保 URL 正确
        if href.startswith('/'):
            href = 'https://www.qcc.com' + href

        # 获取公司详细信息页面
        details = sess.get(href, headers=afterLogin_headers, timeout=10)
        details.raise_for_status()
        details.encoding = 'utf-8'
        details_soup = BeautifulSoup(details.text, features="html.parser")
        message = details_soup.text
        time.sleep(30)  # 延迟，避免被反爬机制检测
        return message
    except Exception as e:
        print(f"Error retrieving company information: {e}")
        return None


def message_to_df(message, company):
    list_companys = []
    Registration_status = []
    Date_of_Establishment = []
    registered_capital = []
    contributed_capital = []
    Approved_date = []
    Unified_social_credit_code = []
    Organization_Code = []
    companyNo = []
    Taxpayer_Identification_Number = []
    sub_Industry = []
    enterprise_type = []
    Business_Term = []
    Registration_Authority = []
    staff_size = []
    Number_of_participants = []
    sub_area = []
    company_adress = []
    Business_Scope = []

    list_companys.append(company)
    Registration_status.append(message.split('登记状态')[1].split('\n')[1].split('成立日期')[0].replace(' ', ''))
    Date_of_Establishment.append(message.split('成立日期')[1].split('\n')[1].replace(' ', ''))
    registered_capital.append(message.split('注册资本')[1].split('人民币')[0].replace(' ', ''))
    contributed_capital.append(message.split('实缴资本')[1].split('人民币')[0].replace(' ', ''))
    Approved_date.append(message.split('核准日期')[1].split('\n')[1].replace(' ', ''))
    try:
        credit = message.split('统一社会信用代码')[1].split('\n')[1].replace(' ', '')
        Unified_social_credit_code.append(credit)
    except:
        credit = message.split('统一社会信用代码')[3].split('\n')[1].replace(' ', '')
        Unified_social_credit_code.append(credit)
    Organization_Code.append(message.split('组织机构代码')[1].split('\n')[1].replace(' ', ''))
    companyNo.append(message.split('工商注册号')[1].split('\n')[1].replace(' ', ''))
    Taxpayer_Identification_Number.append(message.split('纳税人识别号')[1].split('\n')[1].replace(' ', ''))
    try:
        sub = message.split('所属行业')[1].split('\n')[1].replace(' ', '')
        sub_Industry.append(sub)
    except:
        sub = message.split('所属行业')[1].split('为')[1].split('，')[0]
        sub_Industry.append(sub)
    enterprise_type.append(message.split('企业类型')[1].split('\n')[1].replace(' ', ''))
    Business_Term.append(message.split('营业期限')[1].split('登记机关')[0].split('\n')[-1].replace(' ', ''))
    Registration_Authority.append(message.split('登记机关')[1].split('\n')[1].replace(' ', ''))
    staff_size.append(message.split('人员规模')[1].split('人')[0].split('\n')[-1].replace(' ', ''))
    Number_of_participants.append(message.split('参保人数')[1].split('所属地区')[0].replace(' ', '').split('\n')[2])
    sub_area.append(message.split('所属地区')[1].split('\n')[1].replace(' ', ''))
    try:
        adress = message.split('经营范围')[0].split('企业地址')[1].split('查看地图')[0].split('\n')[2].replace(' ', '')
        company_adress.append(adress)
    except:
        adress = message.split('经营范围')[1].split('企业地址')[1].split()[0]
        company_adress.append(adress)
    Business_Scope.append(message.split('经营范围')[1].split('\n')[1].replace(' ', ''))
    df = pd.DataFrame({'公司': company, \
                       '登记状态': Registration_status, \
                       '成立日期': Date_of_Establishment, \
                       '注册资本': registered_capital, \
                       '实缴资本': contributed_capital, \
                       '核准日期': Approved_date, \
                       '统一社会信用代码': Unified_social_credit_code, \
                       '组织机构代码': Organization_Code, \
                       '工商注册号': companyNo, \
                       '纳税人识别号': Taxpayer_Identification_Number, \
                       '所属行业': sub_Industry, \
                       '企业类型': enterprise_type, \
                       '营业期限': Business_Term, \
                       '登记机关': Registration_Authority, \
                       '人员规模': staff_size, \
                       '参保人数': Number_of_participants, \
                       '所属地区': sub_area, \
                       '企业地址': company_adress, \
                       '经营范围': Business_Scope})

    return df


# 测试公司列表
companys = ['深圳市腾讯计算机系统有限公司', '阿里巴巴（中国）有限公司']

for company in companys:
    print(f"Processing {company}")
    message = get_company_message(company)
    if message:
        df = message_to_df(message, company)
        if df is not None:
            if company == companys[0]:
                df.to_csv('E:/data/企业电力数据/Enterprises.csv', index=False, header=True)
            else:
                df.to_csv('E:/data/企业电力数据/Enterprises.csv', mode='a+', index=False, header=False)
            print("Data saved successfully.")
    else:
        print("No message retrieved.")
    time.sleep(30)  # 延迟以免触发反爬机制
