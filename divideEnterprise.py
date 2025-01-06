"""
Author: Charlie
Date: 2025.01.06
"""
import pandas as pd
import os
import openpyxl

"""
将1600家企业划分成100家一份的脚本
"""


def split_csv_file(input_file, output_dir, chunk_size=100):
    # 检查输出目录是否存在，不存在则创建
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 读取文件
    try:
        # 自动判断文件类型
        if input_file.endswith('.xlsx') or input_file.endswith('.xls'):
            df = pd.read_excel(input_file)
        elif input_file.endswith('.csv'):
            df = pd.read_csv(input_file)
        else:
            raise ValueError("输入文件格式不支持，请提供 CSV 或 Excel 文件")
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
        return

    # 划分数据并保存
    try:
        total_rows = len(df)
        file_count = 0
        for i in range(0, total_rows, chunk_size):
            chunk = df[i:i + chunk_size]
            output_file = os.path.join(output_dir, f"enterprise_{file_count + 1}.csv")
            chunk.to_csv(output_file, index=False, encoding='utf-8-sig')
            file_count += 1
        print(f"成功将文件划分为 {file_count} 份，保存于目录: {output_dir}")
    except Exception as e:
        print(f"划分文件时发生错误: {e}")


# 使用示例
input_file = "user_list.xlsx"  # 替换为你的输入文件名
output_dir = "E:\data\企业电力数据\分片企业名单"  # 替换为你的输出目录
split_csv_file(input_file, output_dir, chunk_size=100)
