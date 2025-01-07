"""
Author: Charlie
Date: 2024.12.27
"""
from bs4 import BeautifulSoup
import re
import lxml


# 提取企业信息
def extract_company_info(html_text):
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(html_text, "lxml")
    # TODO: 判断html是否完整

    company_info = {}
    company_tags = []

    """
    爬取企业标签
    """
    print("爬取企业标签")
    # 先锁定tags在的位置
    tag_parts = soup.find_all("div", class_="app-tags margin-type-default")
    if tag_parts:
        print("锁定tags")
        print(tag_parts[0])
    # 爬取tag标签的内容
    # 爬取蓝色标签class为ntag text-primary text-brand-blue
    blue_tag_elements = tag_parts[0].find_all("span", class_="ntag text-primary text-brand-blue")
    # print(blue_tag_elements)
    for tag in blue_tag_elements:
        company_tags.append(tag.get_text(strip=True))
        if "事业单位" in tag.get_text(strip=True):
            # 如果是事业单位
            print(tag.get_text(strip=True))
            print("该单位为事业单位，跳过")
            return False
        else:
            print(tag.get_text(strip=True))
            continue

    # ntag text-primary text-brand-blue click
    blue_click_tag_elements = tag_parts[0].find_all("span", class_="ntag text-primary text-brand-blue click")
    # print(blue_click_tag_elements)
    for tag in blue_click_tag_elements:
        company_tags.append(tag.get_text(strip=True))
        print(tag.get_text(strip=True))

    # 爬取红色标签 ntag text-primary text-red click
    red_tag_elements = tag_parts[0].find_all("span", class_="ntag text-primary text-red click")
    # print(red_tag_elements)
    for tag in red_tag_elements:
        company_tags.append(tag.get_text(strip=True))
        print(tag.get_text(strip=True))
        # TODO：标签单独列出？
        if "失信被执行人" in tag.get_text(strip=True):
            company_info["失信被执行人"] = 1
            print("该单位被列为失信被执行人")
        elif "限制高消费" in tag.get_text(strip=True):
            company_info["限制高消费"] = 1
            print("该单位被限制高消费")
        elif "被执行人" in tag.get_text(strip=True):
            company_info["被执行人"] = 1
            print("该单位被列为被执行人")

    company_info["企业标签"] = company_tags
    print(company_info["企业标签"])

    """
    爬取企业规模
    """
    scale_elements = soup.find_all("div", class_="rline scale")
    if scale_elements:
        print("找到了企业规模：")
        # print(scale_elements)
        scale = scale_elements[0].find_next("span", class_="val").text.strip()
        print(scale)
        company_info["企业规模"] = scale

    """
    爬取企业企查查得分
    """
    point_elements = soup.find_all("div", class_="company-score-tag")
    print("point_elements企查分")
    print(point_elements)
    for element in point_elements:
        print("找到了企查分：")
        point_text = element.find_next("span", class_="score-val").text.strip()
        point = re.findall(r'\d+\.\d+|\d+', point_text)
        print(point[0])
        company_info["企查分"] = point[0]

    """
    爬取企业主要信息
    """
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


    # 返回固定格式的公司信息
    fixed_info = {
        "企业名称": company_info.get("企业名称", ""),
        "统一社会信用代码": company_info.get("统一社会信用代码", ""),
        "企业规模": company_info.get("企业规模", ""),
        "企查分": company_info.get("企查分", ""),
        "企业标签": company_info.get("企业标签", ""),
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
