"""
Author: Charlie
Date: 2025.02.09
"""
import pandas as pd

# 文件路径
source_file = "E:/data/企业电力数据/output/uid_merged_data_827.csv"  # 包含 UID 和 level 的数据
other_file = "E:/data/企业电力数据/anonymized_data/data_sum_sorted.csv"  # 另一个需要左连接的数据
output_file = "E:/data/企业电力数据/output/final_merged_data_827.csv"

# 读取 CSV 文件
source_df = pd.read_csv(source_file, usecols=["UID", "level"])  # 只读取 UID 和 level 列
other_df = pd.read_csv(other_file)  # 读取另一个数据表

# 执行左连接
merged_df = other_df.merge(source_df, on="UID", how="left")  # 以 UID 进行左连接
merged_df.dropna(subset=["level"], inplace=True)

# 保存结果
merged_df.to_csv(output_file, index=False, encoding="utf-8-sig")

print(f"处理完成！结果已保存到: {output_file}")
