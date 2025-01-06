# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re


def extract_company_info(html_text):
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(html_text, "lxml")

    company_info = {}

    # 查找所有 class 为 "tb" 的 td 元素
    # td.get_text(strip=True)获得的是里面所有的文本内容
    td_elements = soup.find_all("td", class_="tb")
    # print(td_elements)
    # 一个td一个td的单独寻找
    for td in td_elements:
        if "统一社会信用代码" in td.get_text(strip=True):
            code_elem = td
            print("找到了统一社会信用代码")
            code_value = code_elem.find_next("span", class_="copy-value")
            if code_value:
                print("code_value：找到了统一社会信用代码")
                company_info["统一社会信用代码"] = code_value.text.strip()
                print(company_info["统一社会信用代码"])
            continue
        elif "企业名称" in td.get_text(strip=True):
            code_elem = td
            print("找到了企业名称")
            code_value = code_elem.find_next("span", class_="copy-value")
            if code_value:
                print("code_value：找到了企业名称")
                company_info["企业名称"] = code_value.text.strip()
                print(company_info["企业名称"])
            continue
        elif "登记状态" in td.get_text(strip=True):
            code_elem = td
            print("找到了登记状态")
            # 下一个标签是td
            code_value = code_elem.find_next("td")
            if code_value:
                print("code_value：找到了登记状态")
                company_info["登记状态"] = code_value.text.strip()
                print(company_info["登记状态"])
            continue
        elif "成立日期" in td.get_text(strip=True):
            code_elem = td
            print("找到了成立日期")
            code_value = code_elem.find_next("span", class_="copy-value")
            if code_value:
                print("code_value：找到了成立日期")
                company_info["成立日期"] = code_value.text.strip()
                print(company_info["成立日期"])
            continue
        elif "营业期限" in td.get_text(strip=True):
            code_elem = td
            print("找到了营业期限")
            # 这里下一个标签是td
            code_value = code_elem.find_next("td")
            # 做下数据处理
            # 正则表达式模式：匹配 yyyy-mm-dd 格式的日期
            pattern = r"\d{4}-\d{2}-\d{2}$"
            # 搜索目标日期（最后一个 yyyy-mm-dd 格式的日期）
            dates = re.findall(pattern, code_value.text.strip())
            if dates:
                target_date = dates[-1]
                print("提取的日期是：", target_date)
                company_info["营业期限"] = target_date
                print(company_info["营业期限"])
            continue
        elif "实缴资本" in td.get_text(strip=True):
            code_elem = td
            print("找到了实缴资本")
            # 这里下一个标签是td
            code_value = code_elem.find_next("td")
            if code_value:
                print("code_value：找到了实缴资本")
                company_info["实缴资本"] = code_value.text.strip()
                print(company_info["实缴资本"])
            continue
        elif "注册资本" in td.get_text(strip=True):
            # TODO： bugfix
            print("_________________bug fix_____________________")
            print(td.get_text(strip=True))
            code_elem = td
            print("找到了注册资本")
            # 这里下一个标签是td
            code_value = code_elem.find_next("td")
            if code_value:
                print("code_value：找到了注册资本")
                company_info["注册资本"] = code_value.text.strip()
                print(company_info["注册资本"])
            continue
        # elif "所属地区" in td.get_text(strip=True):
        #     code_elem = td
        #     print("找到了所属地区")
        #     code_value = code_elem.find_next("span", class_="copy-value")
        #     if code_value:
        #         print("code_value：找到了所属地区")
        #         company_info["所属地区"] = code_value.text.strip()
        #         print(company_info["所属地区"])
        #     continue
        elif "经营范围" in td.get_text(strip=True):
            code_elem = td
            print("找到了经营范围")
            code_value = code_elem.find_next("span", class_="copy-value")
            if code_value:
                print("code_value：找到了经营范围区")
                company_info["经营范围"] = code_value.text.strip()
                print(company_info["经营范围"])
            continue
        elif "纳税人资质" in td.get_text(strip=True):
            code_elem = td
            print("找到了纳税人资质")
            # 这里下一个标签是td
            code_value = code_elem.find_next("td")
            if code_value:
                print("code_value：纳税人资质")
                company_info["纳税人资质"] = code_value.text.strip()
                print(company_info["纳税人资质"])
            continue
        elif "企业类型" in td.get_text(strip=True):
            code_elem = td
            print("找到了企业类型")
            # 这里下一个标签是td
            code_value = code_elem.find_next("td")
            if code_value:
                print("code_value：企业类型")
                company_info["企业类型"] = code_value.text.strip()
                print(company_info["企业类型"])
            continue
        elif "人员规模" in td.get_text(strip=True):
            code_elem = td
            print("找到了人员规模")
            # 这里下一个标签是td
            code_value = code_elem.find_next("td")
            if code_value:
                print("code_value：人员规模")
                company_info["人员规模"] = code_value.text.strip()
                print(company_info["人员规模"])
            continue
        elif "国标行业" in td.get_text(strip=True):
            code_elem = td
            print("找到了国标行业")
            code_value = code_elem.find_next("span", class_="inline-block")
            if code_value:
                print("code_value：找到了国标行业")
                company_info["国标行业"] = code_value.text.strip()
                print(company_info["国标行业"])
            continue
        # 单行的情况 好像单双行都能生效
        elif "参保人数" in td.get_text(strip=True):
            code_elem = td
            print("找到了参保人数")
            code_value = code_elem.find_next("span")
            if code_value:
                print("code_value：找到了参保人数")
                company_info["参保人数"] = code_value.text.strip()
                print(company_info["参保人数"])

    # 法定代表人 其实也没用
    legal_person_elem = soup.find("td", string="法定代表人")
    if legal_person_elem:
        legal_person = legal_person_elem.find_next("a")
        if legal_person:
            company_info["法定代表人"] = legal_person.text.strip()

    # 参保人数 这个不好找，有的是双行，有的单行
    # 单行在<td class="tb">
    # elif "参保人数" in td.get_text(strip=True):
    #     code_elem = td
    #     print("找到了参保人数")
    #     code_value = code_elem.find_next("span")
    #     if code_value:
    #         print("code_value：找到了参保人数")
    #         company_info["参保人数"] = code_value.text.strip()
    #         print(company_info["参保人数"])

    # 返回固定格式的公司信息
    fixed_info = {
        "企业名称": company_info.get("企业名称", ""),
        "统一社会信用代码": company_info.get("统一社会信用代码", ""),
        "登记状态": company_info.get("登记状态", ""),
        "成立日期": company_info.get("成立日期", ""),
        "营业期限": company_info.get("营业期限", ""),
        "纳税人资质": company_info.get("纳税人资质", ""),
        "注册资本": company_info.get("注册资本", ""),
        "实缴资本": company_info.get("实缴资本", ""),
        "企业类型": company_info.get("企业类型", ""),
        "人员规模": company_info.get("人员规模", ""),
        "参保人数": company_info.get("参保人数", ""),
        "国标行业": company_info.get("国标行业", ""),
        "经营范围": company_info.get("经营范围", "")
    }

    return fixed_info


# 测试代码
# 提取并打印公司信息
with open("example2.html", "r", encoding="utf-8") as file:
    html_text = file.read()  # 读取文件内容
company_info = extract_company_info(html_text)
print(company_info)
