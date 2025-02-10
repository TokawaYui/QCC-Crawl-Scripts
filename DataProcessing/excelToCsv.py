"""
Author: Charlie
Date: 2025.02.08
"""
import pandas as pd

# 读取 Excel 文件
excel_file = 'E:/data/企业电力数据/anonymized_data/sample.xlsx'
df = pd.read_excel(excel_file)

# 保存为 CSV 文件
csv_file = 'E:/data/企业电力数据/anonymized_data/data_sum_sorted.csv'
df.to_csv(csv_file, index=False)
