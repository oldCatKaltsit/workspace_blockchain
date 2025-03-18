# import hashlib
#
# # 原始数据
# original_data = "Hello, World!"
#
# # 计算原始数据的哈希值
# original_hash = hashlib.sha256(original_data.encode()).hexdigest()
#
# # 假设接收到的数据
# received_data = "Hello, World! "  # 如果数据被篡改，这里会不同
#
# # 重新计算接收到数据的哈希值
# received_hash = hashlib.sha256(received_data.encode()).hexdigest()
#
# # 比较两个哈希值
# if original_hash == received_hash:
#     print("数据没有被篡改")
# else:
#     print("数据已经被篡改")
import numpy as np

# 给定的数据
values = np.array([0, 1, 2, 3, 4, 5])
counts = np.array([9, 6, 4, 5, 8, 4])

# 总像素数
total_pixels = np.sum(counts)

# 计算概率分布
p = counts / total_pixels

# 计算累积概率和和累积均值
cumsum = np.cumsum(p)
m = np.cumsum(p * values)
m_G = m[-1]  # 全局均值

# 存储结果
results = []

# 计算t从0到6的所有参数
for t in range(7):
    if t == 0:
        # 对于t=0，类别0为空
        w0 = 0
        theta0 = 0
        w1 = cumsum[-1]
        theta1 = m_G
    elif t >= 6:
        # 对于t=6，类别1为空
        w0 = cumsum[-1]
        theta0 = m_G
        w1 = 0
        theta1 = 0
    else:
        # 其他情况
        w0 = cumsum[t - 1]
        w1 = 1 - w0

        if w0 == 0:
            theta0 = 0
        else:
            theta0 = m[t - 1] / w0

        if w1 == 0:
            theta1 = 0
        else:
            theta1 = (m_G - m[t - 1]) / w1

    # 计算类间方差
    if w0 == 0 or w1 == 0:
        theta_squared_w = 0
    else:
        theta_squared_w = w0 * w1 * (theta0 - theta1) ** 2

    results.append({
        't': t,
        'w0': w0,
        'theta0': theta0,
        'w1': w1,
        'theta1': theta1,
        'theta_squared_w': theta_squared_w
    })

# 打印结果表格
print("t\tw0\ttheta0\tw1\ttheta1\ttheta^2_w")
print("-" * 60)
for r in results:
    print(f"{r['t']}\t{r['w0']:.4f}\t{r['theta0']:.4f}\t{r['w1']:.4f}\t{r['theta1']:.4f}\t{r['theta_squared_w']:.4f}")

# 找出最佳阈值（类间方差最大的t值）
best_t = max(results, key=lambda x: x['theta_squared_w'])
print("\n最佳阈值 t =", best_t['t'])