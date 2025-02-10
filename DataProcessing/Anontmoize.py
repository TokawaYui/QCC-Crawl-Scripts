"""
Author: Charlie
Date: 2025.01.30
"""
# import pandas as pd
#
# # 读取两个CSV文件
# map_file = "E:/data/企业电力数据/enterprise_mapping.csv"
# data_file = "E:/data/企业电力数据/output/normalized_classified_merged_data_647.csv"
# output_file = "E:/data/企业电力数据/output/anonymized_classified_merged_data_647.csv"
#
# # 步骤 1: 读取映射表，创建 {企业名: UID} 的字典
# map_df = pd.read_csv(map_file)
# name_to_uid = dict(zip(map_df["户名"], map_df["UID"]))
#
# # 步骤 2: 读取需要处理的CSV数据
# data_df = pd.read_csv(data_file)
#
# # 步骤 3: 替换公司名称列为 UID
# data_df["UID"] = data_df["企业名称"].map(name_to_uid)
#
# # 步骤 4: 处理未匹配到 UID 的情况
# unmatched_enterprises = data_df[data_df["UID"].isna()]["企业名称"].unique()  # 获取未匹配的企业名称（去重）
#
# # 输出未匹配的企业名称
# if len(unmatched_enterprises) > 0:
#     print("未匹配的企业名称如下：")
#     for name in unmatched_enterprises:
#         print(name)
# else:
#     print("所有企业名称都成功匹配！")
#
# # 步骤 5: 保存结果到新文件
# data_df.to_csv(output_file, index=False, encoding="utf-8-sig")
#
# print(f"处理完成！结果已保存到: {output_file}")


# import pandas as pd
#
# # 输入和输出文件路径
# input_file = "E:/data/企业电力数据/output/classified_merged_data_647.csv"
# output_file = "E:/data/企业电力数据/output/normalized_classified_merged_data_647.csv"
#
# # 读取 CSV 文件
# df = pd.read_csv(input_file)
#
# # 替换“企业名称”列中的中文括号
# df["企业名称"] = df["企业名称"].str.replace("（", "(", regex=False).str.replace("）", ")", regex=False)
#
# # 保存修改后的数据
# df.to_csv(output_file, index=False, encoding="utf-8-sig")
#
# print(f"处理完成！结果已保存到: {output_file}")


import pandas as pd

# 文件路径
mapping_file = "E:/data/企业电力数据/enterprise_uid_mapping.csv"
data_file = "E:/data/企业电力数据/output/normalized_classified_merged_data_647.csv"
output_file = "E:/data/企业电力数据/output/uid_merged_data.csv"

# 读取 CSV 文件
mapping_df = pd.read_csv(mapping_file)
data_df = pd.read_csv(data_file)

# 执行左连接
merged_df = mapping_df.merge(data_df, left_on="户名", right_on="企业名称", how="left")

# 删除没有匹配到“企业名称”的行（即 `NaN` 的行）
merged_df.dropna(subset=["企业名称"], inplace=True)

# 删除重复的“企业名称”列（因为已经有“户名”）
merged_df.drop(columns=["企业名称"], inplace=True)

# 保存结果
merged_df.to_csv(output_file, index=False, encoding="utf-8-sig")

print(f"处理完成！结果已保存到: {output_file}")
