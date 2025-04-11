import pandas as pd
import matplotlib.pyplot as plt
import os

def creat_frame():
    """
    创建一个包含学生信息的DataFrame并保存为CSV文件（适配新数据）。
    """
    data = {
        '姓名': ['张三', '李四', '王五', '赵六', '陈七'],
        '年龄': [25.0, 30.0, None, 22.0, 28.0],  # 年龄列缺失王五的数据
        '成绩': [85.5, 90.0, 78.5, 88.0, 92.0],
        '城市': ['北京', '上海', '广州', '深圳', '上海']  # 列名调整为“城市”
    }
    df = pd.DataFrame(data)
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/data.csv', index=False, encoding='utf-8')

def load_data():
    """任务1: 读取数据文件"""
    return pd.read_csv('data/data.csv')

def show_basic_info(data):
    """任务2: 显示数据基本信息"""
    print("=== 数据前5行 ===")
    print(data.head())
    print("\n=== 数据信息 ===")
    print(data.info())
    print("\n=== 统计描述 ===")
    print(data.describe(include='all'))

def handle_missing_values(data):
    """任务3: 处理缺失值"""
    # 年龄列用均值填充，成绩列无缺失值（但保留逻辑）
    data['年龄'].fillna(data['年龄'].mean(), inplace=True)
    return data

def analyze_statistics(data):
    """任务4: 统计分析数值列"""
    numeric_cols = data.select_dtypes(include=['number'])
    stats = numeric_cols.agg(['mean', 'std', 'min', 'max', 'median'])
    print("\n=== 数值列统计分析 ===")
    print(stats)

def visualize_data(data, column_name='成绩'):
    """任务6: 数据可视化"""
    plt.figure(figsize=(8, 4))
    plt.hist(data[column_name], bins=5, edgecolor='black')
    plt.title(f'{column_name}分布直方图')
    plt.xlabel(column_name)
    plt.ylabel('频数')
    plt.grid(axis='y', alpha=0.5)
    plt.show()

def save_processed_data(data):
    """任务7: 保存处理后的数据"""
    data.to_csv('processed_data.csv', index=False, encoding='utf-8')

def main():
    """主函数，执行所有数据处理流程"""
    creat_frame()                # 生成原始数据（适配新数据）
    data = load_data()           # 读取数据
    show_basic_info(data)        # 显示基本信息
    data_clean = handle_missing_values(data)  # 处理缺失值
    analyze_statistics(data_clean)           # 统计分析
    visualize_data(data_clean)               # 可视化
    save_processed_data(data_clean)          # 保存处理后的数据

if __name__ == "__main__":
    main()
