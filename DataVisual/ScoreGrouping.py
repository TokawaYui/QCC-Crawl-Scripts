"""
Author: Charlie
Date: 2025.02.08
"""
import os.path

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

matplotlib.use("Agg")

# 读取 CSV 文件
csv_path = "E:/data/企业电力数据/output"
csv_name = "merged_data_647.csv"
csv_file = os.path.join(csv_path, csv_name)
df = pd.read_csv(csv_file, encoding="utf-8", on_bad_lines="skip", sep=",", quotechar='"')

# 确保 "企查分" 是数值类型
df["企查分"] = pd.to_numeric(df["企查分"], errors="coerce")

# 删除 "企查分" 为空的数据
df = df.dropna(subset=["企查分"])

# 计算每个分区间的企业数量
df["分数段"] = (df["企查分"] // 100) * 100  # 计算区间起点（如 0, 200, 400, ...）
score_distribution = df["分数段"].value_counts().sort_index()  # 统计数量并排序
print(score_distribution)

# 画图
plt.figure(figsize=(10, 6))
sns.barplot(x=score_distribution.index, y=score_distribution.values, palette="Blues_r")

# 添加标题和标签
plt.xlabel("Score", fontsize=12)
plt.ylabel("Num", fontsize=12)
plt.title(f"ScoreGrouping_{csv_name}", fontsize=14)
plt.xticks(rotation=45)  # 旋转 x 轴标签以便于阅读

# 显示数值标签
for i, v in enumerate(score_distribution.values):
    plt.text(i, v + 2, str(v), ha="center", fontsize=10)

# 保存图表
plt.savefig(f"{csv_name}企查分统计_100.png", dpi=300, bbox_inches="tight")