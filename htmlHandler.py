"""
Author: Charlie
Date: 2024.12.27
"""
from bs4 import BeautifulSoup
import lxml


# 提取企业信息
def extract_company_info(html_text):
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(html_text, "lxml")

    print("_______Enter extract company info_________")
    print(html_text)

    company_info = {}

    # 统一社会信用代码
    code_elem = soup.find("td", text="统一社会信用代码")
    if code_elem:
        company_info["统一社会信用代码"] = code_elem.find_next("span", class_="copy-value").text.strip()

    # 企业名称
    name_elem = soup.find("td", text="企业名称")
    if name_elem:
        company_info["企业名称"] = name_elem.find_next("span", class_="copy-value").text.strip()

    # 法定代表人
    legal_person_elem = soup.find("td", text="法定代表人")
    if legal_person_elem:
        legal_person = legal_person_elem.find_next("a")
        company_info["法定代表人"] = legal_person.text.strip() if legal_person else "未找到"

    # 成立日期
    date_elem = soup.find("td", text="成立日期")
    if date_elem:
        company_info["成立日期"] = date_elem.find_next("span", class_="copy-value").text.strip()

    # 注册资本
    capital_elem = soup.find("td", text="注册资本")
    if capital_elem:
        company_info["注册资本"] = capital_elem.find_next("td").text.strip()

    # 所属地区
    region_elem = soup.find("td", text="所属地区")
    if region_elem:
        company_info["所属地区"] = region_elem.find_next("span", class_="copy-value").text.strip()

    # 经营范围
    scope_elem = soup.find("td", text="经营范围")
    if scope_elem:
        company_info["经营范围"] = scope_elem.find_next("span", class_="copy-value").text.strip()

    return company_info
