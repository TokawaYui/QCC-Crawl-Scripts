"""
Author: Charlie
Date: 2025.02.08
"""
import pandas as pd
import os

# 输入和输出文件夹
input_folder = "E:/data/电力数据/electric_dataset/anonymized_data/data_by_industry"  # 你的CSV文件所在的文件夹
output_file = "E:/data/企业电力数据/anonymized_data/data_sum.csv"  # 处理后的CSV文件存放的文件夹

# 初始化一个空的列表用于存放数据块
data_frames = []

# 处理所有 CSV 文件
for filename in os.listdir(input_folder):
    if filename.endswith(".csv"):
        input_path = os.path.join(input_folder, filename)

        # 读取 CSV（使用 chunksize 适应大数据）
        chunk_iter = pd.read_csv(input_path, chunksize=10000)  # 分块读取，每次读取10000行
        for chunk in chunk_iter:
            # 计算后96列的和
            chunk["sum_power"] = chunk.iloc[:, 2:].sum(axis=1)
            data_frames.append(chunk)

        print(f"Processed: {filename}")

# 合并所有数据块并写入最终CSV
if data_frames:
    merged_df = pd.concat(data_frames, ignore_index=True)
    merged_df.to_csv(output_file, index=False)
    print(f"All files merged successfully into {output_file}")
else:
    print("No CSV files found or processed.")

