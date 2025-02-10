"""
Author: Charlie
Date: 2025.02.08
"""
import pandas as pd

input_file = "E:/data/企业电力数据/anonymized_data/data_sum.csv"
output_file = "E:/data/企业电力数据/anonymized_data/data_sum_sorted.csv"

# **检查 CSV 列名，确保 UID 存在**
df_sample = pd.read_csv(input_file, nrows=5, sep=",")
print("CSV columns:", df_sample.columns.tolist())  # 显示列名，检查 UID 是否存在

# **设置正确的列名匹配**
if "UID" not in df_sample.columns:
    raise ValueError("Error: 'UID' column not found in CSV! Please check column names.")

# **按 UID 进行排序**
chunksize = 100000  # 100,000 行一次处理
df_sorted_chunks = []

for chunk in pd.read_csv(input_file, chunksize=chunksize, dtype={"UID": str}, sep=","):
    if "UID" not in chunk.columns:
        raise ValueError("❌ Error: 'UID' 列在当前块丢失，请检查 CSV 结构！")

    sorted_chunk = chunk.sort_values(by="UID")

    # 检查排序后 UID 是否仍然存在
    print("UID 前 5 行:", sorted_chunk["UID"].head().tolist())

    df_sorted_chunks.append(sorted_chunk)

# 合并所有块
df_sorted = pd.concat(df_sorted_chunks)

# 再次检查 UID
if "UID" not in df_sorted.columns:
    raise ValueError("❌ Error: 'UID' 在合并后丢失！")

# 保存结果
output_file = "E:/data/企业电力数据/anonymized_data/data_sum_sorted.csv"
df_sorted.to_csv(output_file, index=False)

print("✅ 排序完成，文件已保存！")

