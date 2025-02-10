"""
Author: Charlie
Date: 2025.02.08
"""
import os
import pandas as pd


# 读取 CSV 文件
csv_path = "E:/data/企业电力数据"
csv_name = "merged_data_647.csv"
csv_file = os.path.join(csv_path, csv_name)
df = pd.read_csv(csv_file, encoding="utf-8", on_bad_lines="skip", sep=",", quotechar='"')

# 确保 "企查分" 列是数值类型
df["企查分"] = pd.to_numeric(df["企查分"], errors="coerce")

# 使用 pd.cut() 进行分级
df["level"] = pd.cut(df["企查分"],
                     bins=[0, 400, 800, 1200, float("inf")],  # 分界点
                     labels=[1, 2, 3, 4],  # 对应的等级
                     right=False)  # 右边界不包含（即 0-399 为 1，400-799 为 2）

# 保存处理后的 CSV
df.to_csv(f"E:/data/企业电力数据/classified_{csv_name}", index=False)
