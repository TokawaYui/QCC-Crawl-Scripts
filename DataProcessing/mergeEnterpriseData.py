"""
Author: Charlie
Date: 2025.02.08
"""
import pandas as pd
import glob
import os

# 指定包含 CSV 文件的文件夹路径
folder_path = "E:/data/企业电力数据/分片企业名单_20_output"  # 修改为你的路径
output_file = "E:/data/企业电力数据/merged_data_1000full.csv"  # 合并后的文件名

# 获取所有符合条件的 CSV 文件
csv_files = glob.glob(os.path.join(folder_path, "company_info_*.csv"))

# 初始化一个空的 DataFrame 用于存储合并数据
merged_df = pd.DataFrame()

# 逐个读取 CSV 并合并
for file in csv_files:
    df = pd.read_csv(file, encoding="utf-8", on_bad_lines="skip", sep=",", quotechar='"')  # 读取 CSV
    # df = df.dropna(subset=["企查分"])  # 去除 "企查分" 为空的行
    merged_df = pd.concat([merged_df, df], ignore_index=True)  # 合并数据

# 保存合并后的数据
merged_df.to_csv(output_file, index=False)

print(f"✅ 合并完成，共 {len(merged_df)} 行数据，已保存至 {output_file}。")
