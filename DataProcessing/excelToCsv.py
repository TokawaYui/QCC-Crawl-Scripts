"""
Author: Charlie
Date: 2025.02.08
"""
import pandas as pd

# 读取 Excel 文件
excel_file = 'E:/data/企业电力数据/enterprise_mapping.xlsx'
df = pd.read_excel(excel_file)

# 保存为 CSV 文件
csv_file = 'E:/data/企业电力数据/enterprise_mapping.csv'
df.to_csv(csv_file, index=False)

# import pandas as pd
#
# # 输入和输出文件路径
# input_file = "E:/data/企业电力数据/enterprise_mapping.csv"
# output_file = "E:/data/企业电力数据/enterprise_uid_mapping.csv"
#
# # 读取 CSV 文件
# df = pd.read_csv(input_file)
#
# # 确保 UID 列存在，然后调整列顺序
# if "UID" in df.columns:
#     df = df[['UID'] + [col for col in df.columns if col != 'UID']]
#
# # 保存调整后的数据
# df.to_csv(output_file, index=False, encoding="utf-8-sig")
#
# print(f"处理完成！结果已保存到: {output_file}")

