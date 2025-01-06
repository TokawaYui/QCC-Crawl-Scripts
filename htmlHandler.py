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
        company_info["法定代表人"] = legal_person_elem.find_next("a").text.strip()

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

# 将你的HTML内容赋值给html_content变量
html_content = """<div class="cominfo-normal"><table class="ntable"><tr><td width="13%" class="tb">统一社会信用代码 <i class="app-glossary-info glossary-info aicon qccdicon icon-icon_zhushi"></i></td> <td width="21%" style="padding-right: 0px;"><span class="app-copy-box copy-hover-item"><span class="copy-value">91330100716105852F</span><span class="app-copy copy-button-item"><div class="base_copy"><!----> <span class="m-l-4">复制</span></div></span></span></td> <td width="13%" class="tb">企业名称 <i class="app-glossary-info glossary-info aicon qccdicon icon-icon_zhushi"></i></td> <td colspan="3"><span class="app-copy-box copy-hover-item"><span class="copy-value">阿里巴巴（中国）网络技术有限公司</span><span class="app-copy copy-button-item"><div class="base_copy"><!----> <span class="m-l-4">复制</span></div></span></span> <div class="text-gray clearfix original-name-part"><div class="ntag text-gray original-tag">曾用名<span class="m-l-space">2</span></div> <div class="original-name-list"><div><span class="app-copy-box copy-hover-item"><span class="copy-value">阿里巴巴（杭州）网络技术发展有限公司</span><span>（- 至 
              2000-07）</span><a class="inline-block"><span class="text-dk">…</span>展开</a><span class="app-copy copy-button-item"><div class="base_copy hover-show"><!----> <span class="m-l-4">复制</span></div></span></span></div></div></div></td></tr> <tr><td width="13%" rowspan="2" class="tb">法定代表人
        <i class="app-glossary-info glossary-info aicon qccdicon icon-icon_zhushi"></i> <!----> <!----></td> <td rowspan="2" class="base-opertd"><div><div class="td-coy"><span class="headimg"><img src="https://image.qcc.com/person/pc51965038cd7af518be306491e4bd23.jpg?x-oss-process=style/person_200" class="img-logo app-auto-logo" style="width: 40px; height: 40px;"></span> <span class="cont"><span class="upside-line"><span><span><a href="https://www.qcc.com/pl/pc51965038cd7af518be306491e4bd23.html" target="_blank">蒋芳</a></span> <a class="ntag-v2"><i class="war-icon aicon qccdicon icon-icon_guanlianqiye"></i> <span class="text-dark">关联企业</span> <span class="count">18</span></a> <!----></span> <!----></span> <!----> <!----> </span> <!----> </div></div> <!----></td> <td width="13%" rowspan="1" class="tb">登记状态 <i class="app-glossary-info glossary-info aicon qccdicon icon-icon_zhushi"></i></td> <td width="20%" rowspan="1">存续<!----></td> <td width="13%" rowspan="1" class="tb">成立日期</td> <td width="20%" rowspan="1"><span class="app-copy-box copy-hover-item"><span class="copy-value"> 1999-09-09</span><span class="app-copy copy-button-item"><div class="base_copy"><!----> <span class="m-l-4">复制</span></div></span></span></td></tr> <tr><td class="tb"><span>注册资本</span> <i class="app-glossary-info glossary-info aicon qccdicon icon-icon_zhushi"></i></td> <td>599594.14455万美元</td> <td class="tb">实缴资本 <i class="app-glossary-info glossary-info aicon qccdicon icon-icon_zhushi"></i></td> <td>
          316403.90188万美元
        </td> <!----></tr> <tr><td class="tb">组织机构代码 <i class="app-glossary-info glossary-info aicon qccdicon icon-icon_zhushi"></i></td> <td><span class="app-copy-box copy-hover-item"><span class="copy-value">71610585-2</span><span class="app-copy copy-button-item"><div class="base_copy"><!----> <span class="m-l-4">复制</span></div></span></span></td> <td class="tb">工商注册号 <i class="app-glossary-info glossary-info aicon qccdicon icon-icon_zhushi"></i></td> <td><span class="app-copy-box copy-hover-item"><span class="copy-value">330100400015575</span><span class="app-copy copy-button-item"><div class="base_copy"><!----> <span class="m-l-4">复制</span></div></span></span></td> <td class="tb">纳税人识别号 <i class="app-glossary-info glossary-info aicon qccdicon icon-icon_zhushi"></i></td> <td style="padding-right: 0px;"><span class="app-copy-box copy-hover-item"><span class="copy-value">91330100716105852F</span><span class="app-copy copy-button-item"><div class="base_copy"><!----> <span class="m-l-4">复制</span></div></span></span></td></tr> <tr><td class="tb">企业类型
        </td> <td>有限责任公司（港澳台投资、非独资）</td> <td class="tb">营业期限 <i class="app-glossary-info glossary-info aicon qccdicon icon-icon_zhushi"></i></td> <td>
        1999-09-09
        至
        
          2040-09-08
        </td> <td class="tb">纳税人资质 <i class="app-glossary-info glossary-info aicon qccdicon icon-icon_zhushi"></i></td> <td>增值税一般纳税人</td></tr> <tr><td class="tb">人员规模
        </td> <td>4000-4999人</td> <td class="tb double-tb"><div>参保人数</div> <div>分支机构参保人数</div></td> <td class="double-tb"><div><span>4827</span><a class="m-l-r-10">(2023年报)</a> <a><div class="trend-wrapper ntag-v2 ntag-v2-primary"><i class="qushi aicon qccdicon icon-icon_qushi"></i></div></a></div> <div><span>479</span><span class="m-l-r-10 text-gray">(2023年报)</span> <a><div class="trend-wrapper ntag-v2 ntag-v2-primary"><i class="qushi aicon qccdicon icon-icon_qushi"></i></div></a></div></td> <td class="tb">核准日期 <i class="app-glossary-info glossary-info aicon qccdicon icon-icon_zhushi"></i><div style="position: absolute; top: 0px; left: 0px; width: 100%;"><div><div class="qccd-popover undefined qccd-popover-placement-bottom" style="left: 725px; top: 1220px; transform-origin: 50% -4px; display: none;"><div role="tooltip" class="qccd-popover-inner qccd-popover-content" style="max-width: none;"><div><div class="qccd-popover-inner-content"><div class="glossary-content"><div class="line"><!----> <div class="glossary-text">一般指企业最近一次的法定变更登记申请被核准的日期。</div></div> <!----></div></div></div></div></div></div></div></td> <td><span class="app-data-mask"> <span class="vip-mask"></span></span></td></tr> <tr><td class="tb">所属地区</td> <td><span class="app-copy-box copy-hover-item"><span class="copy-value">浙江省杭州市滨江区</span><span class="app-copy copy-button-item"><div class="base_copy hover-show"><!----> <span class="m-l-4">复制</span></div></span></span></td> <td class="tb">登记机关 <i class="app-glossary-info glossary-info aicon qccdicon icon-icon_zhushi"></i></td> <td colspan="1"><span class="app-copy-box copy-hover-item"><span class="copy-value">杭州市高新区（滨江）市场监督管理局</span><span class="app-copy copy-button-item"><div class="base_copy hover-show"><!----> <span class="m-l-4">复制</span></div></span></span></td> <td class="tb">进出口企业代码 <i class="app-glossary-info glossary-info aicon qccdicon icon-icon_zhushi"></i></td> <td><span class="app-copy-box copy-hover-item"><span class="copy-value">3300716105852</span><span class="app-copy copy-button-item"><div class="base_copy"><!----> <span class="m-l-4">复制</span></div></span></span></td></tr> <tr><td class="tb">国标行业 <i class="app-glossary-info glossary-info aicon qccdicon icon-icon_zhushi"></i></td> <td><div class="gb-content"><div class="gb-wrapper"><span>应用软件开发<span class="inline-block"><span class="g-color-999">（I6513）</span><i class="arrow arrow-title aicon qccdicon icon-icon_jiantou8"></i></span></span></div></div></td> <td class="tb">英文名
        </td> <td colspan="3"><span class="app-copy-box copy-hover-item"><span><span class="copy-value">Alibaba (China) Technology Co., Ltd.</span> <!----></span><span class="app-copy copy-button-item"><div class="base_copy hover-show"><!----> <span class="m-l-4">复制</span></div></span></span></td></tr> <tr><td class="tb"><span>注册地址 </span> <i class="app-glossary-info glossary-info aicon qccdicon icon-icon_zhushi"></i></td> <td colspan="5"><span class="app-copy-box copy-hover-item"><span><a class="text-dk copy-value">浙江省杭州市滨江区网商路699号</a><a href="/map?keyNo=c70a55cb048c8e4db7bca357a2c113e0" rel="nofollow" target="_blank" class="m-l-sm">附近企业</a><!----></span><span class="app-copy copy-button-item"><div class="base_copy"><!----> <span class="m-l-4">复制</span></div></span></span></td></tr> <!----> <tr><td class="tb">经营范围 <i class="app-glossary-info glossary-info aicon qccdicon icon-icon_zhushi"></i></td> <td colspan="5" class="break-word"><span class="app-copy-box copy-hover-item"><span class="copy-value">一般项目：软件开发；软件销售；技术服务、技术开发、技术咨询、技术交流、技术转让、技术推广；网络设备销售；计算机软硬件及辅助设备零售；计算机软硬件及辅助设备批发；非居住房地产租赁；停车场服务；翻译服务；物业管理；业务培训（不含教育培训、职业技能培训等需取得许可的培训）（除依法须经批准的项目外，凭营业执照依法自主开展经营活动）。</span><span class="app-copy copy-button-item"><div class="base_copy"><!----> <span class="m-l-4">复制</span></div></span></span></td></tr></table> <!----> <!----> <div tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true" data-backdrop="true" class="app-nmodal modal fade"><div class="modal-dialog nmodal" style="width: 600px; margin-top: 50px;"><div class="modal-content"><div class="modal-header"><a type="button" data-dismiss="modal" class="nclose"><i class="close-btn aicon qccdicon icon-icon_guanbixx"></i></a> <div class="right"> <div class="watermark"></div></div> <h4 class="modal-title"><div>法定代表人<span class="text-primary">1</span></div> <!----> <!----> <!----> <!----></h4></div> <div class="cross-line"></div> <div class="modal-body scroll-content" style="padding: 15px;"> <div class="app-ntable"> <table class="ntable hide-info"><!----> <tr><!----> <th class="tx">序号</th> <th class="">姓名<!----> <!----></th></tr> <tr><!----> <td class="tx">
            
          </td> <td class="left"><div class="td-coy"><span class="headimg"><img src="https://image.qcc.com/person/pc51965038cd7af518be306491e4bd23.jpg?x-oss-process=style/person_200" class="img-logo app-auto-logo" style="width: 40px; height: 40px;"></span> <span class="cont"><span class="upside-line"><span><span><a href="https://www.qcc.com/pl/pc51965038cd7af518be306491e4bd23.html" target="_blank">蒋芳</a></span> <a class="ntag-v2"><i class="war-icon aicon qccdicon icon-icon_guanlianqiye"></i> <span class="text-dark">关联企业</span> <span class="count">18</span></a> <!----></span> <!----></span> <!----> <!----> </span> <!----> </div></td></tr> </table>  <nav class="text-right"> <ul class="pagination" style="display: none;"><!----> <!----> <!----> <li class="active"><a href="javascript:void(0)">
      
      <!----></a></li> <!----> <!----> <!----></ul></nav></div></div> <!----> <!----></div></div></div></div>"""  # 省略部分HTML
company_data = extract_company_info(html_content)

# 打印提取到的信息
for key, value in company_data.items():
    print(f"{key}: {value}")
