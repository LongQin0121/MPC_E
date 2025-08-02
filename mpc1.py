"""
MPC基本术语图解
"""

import matplotlib.pyplot as plt
import numpy as np

# 创建时间轴和示例数据
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

# 时间点
current_time = 5
N = 8  # 预测窗口长度
M = 3  # 控制窗口长度

times = np.arange(0, 15)
pred_times = np.arange(current_time, current_time + N)
ctrl_times = np.arange(current_time, current_time + M)

# 上图：系统输出（位置）
past_output = [0, 0.5, 1.2, 2.1, 3.0]
predicted_output = [3.0, 3.8, 4.3, 4.6, 4.8, 4.9, 5.0, 5.0]
target = [5.0] * len(pred_times)

# 绘制过去和预测的输出
ax1.plot(range(current_time), past_output, 'b-', linewidth=3, label='过去的输出', marker='o')
ax1.plot(pred_times, predicted_output, 'r--', linewidth=2, label='预测输出', marker='s')
ax1.plot(pred_times, target, 'g-', linewidth=2, label='参考轨迹')

# 标记预测窗口
ax1.axvspan(current_time, current_time + N - 1, alpha=0.2, color='red', label='预测窗口 N=8')
ax1.axvline(x=current_time, color='black', linestyle='-', linewidth=2)
ax1.text(current_time, 1, '当前时刻', rotation=90, ha='right')

ax1.set_ylabel('输出 (位置)')
ax1.set_title('MPC预测窗口和控制窗口概念')
ax1.legend()
ax1.grid(True)
ax1.set_ylim(-0.5, 6)

# 下图：控制输入
past_control = [0, 1.0, 0.8, 0.6, 0.4]
planned_control = [0.2, 0.15, 0.1, 0, 0, 0, 0, 0]
executed_control = [0.2]  # 只执行第一个

# 绘制过去和计划的控制
past_times = list(range(current_time + 1))  # [0,1,2,3,4,5]
ax2.step(past_times, past_control + [past_control[-1]], 'b-', 
         linewidth=3, label='过去的控制', where='post')

pred_times_ext = list(pred_times) + [pred_times[-1] + 1]  # 扩展一个时间点
ax2.step(pred_times_ext, planned_control + [planned_control[-1]], 'r--', 
         linewidth=2, label='计划控制序列', where='post')

ax2.step([current_time, current_time+1], [0.2, 0.2], 'g-', 
         linewidth=4, label='实际执行的控制', where='post')

# 标记控制窗口
ax2.axvspan(current_time, current_time + M - 1, alpha=0.3, color='orange', label='控制窗口 M=3')
ax2.axvline(x=current_time, color='black', linestyle='-', linewidth=2)

ax2.set_ylabel('控制输入')
ax2.set_xlabel('时间步')
ax2.legend()
ax2.grid(True)
ax2.set_ylim(-0.2, 1.2)

plt.tight_layout()
plt.show()

# 打印术语解释
print("=== MPC基本术语 ===\n")

print("🎯 预测窗口 (Prediction Horizon, N):")
print("   - 向前预测的时间步数")
print("   - 例子中 N=8，预测未来8步")
print("   - 越长越能考虑长期效果，但计算量增加\n")

print("🎮 控制窗口 (Control Horizon, M):")
print("   - 优化控制输入的时间步数")
print("   - 例子中 M=3，优化前3步的控制")
print("   - 通常 M ≤ N，减少优化变量\n")

print("🔄 滚动优化 (Receding Horizon):")
print("   - 每一步都重新求解优化问题")
print("   - 只执行第一步控制")
print("   - 下一步基于新状态重新优化\n")

print("📊 预测模型 (Prediction Model):")
print("   - 描述系统动态的数学模型")
print("   - 用于预测未来状态")
print("   - 线性MPC使用线性模型\n")

print("🎯 目标函数 (Objective Function):")
print("   - 定义控制性能指标")
print("   - 通常包括跟踪误差和控制代价")
print("   - 例：minimize Σ(误差² + 控制²)\n")

print("⛔ 约束条件 (Constraints):")
print("   - 系统物理限制")
print("   - 输入约束：|u| ≤ u_max")
print("   - 状态约束：x_min ≤ x ≤ x_max")