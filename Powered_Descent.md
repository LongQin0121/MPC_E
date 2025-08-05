#  Achieving RTAs outside the Energy-Neutral Time Window: Energy-Neutral CDOs vs. Powered Descents

# RAUL     4.

这段文档详细描述了飞机下降轨迹优化的最优控制问题formulation。让我为你解析主要内容：
问题性质
这是一个多阶段、约束、非线性最优控制问题，目标是在满足RTA的前提下最小化燃油消耗。
动态约束模型
使用γ-command模型描述飞机动态：飞机动态模型方程Document # 飞机动态模型 (γ-command)

动态约束方程 (IV.2)：

```
f̃ⱼ = [
    1/T - D(v,h,γ)/m - g sin γ
    v sin γ  
    -q(v, h, T)
    1/(v cos γ + wₛ(h))
]
```

其中：
- **D(v,h,γ)**：空气动力阻力
- **g**：重力加速度  
- **q(v,h,T)**：燃油流量
- **wₛ(h)**：风速（高度的函数）
- **γ**：飞行路径角
- **v**：速度飞行阶段划分
整个下降过程被分为P=9个阶段，总共N=90个时间采样点：

Phase 0 (CRUISE)：巡航阶段
Phase 1 (DESCENT ABOVE FL100)：FL100以上下降
Phase 2 (DESCENT BELOW FL100)：FL100以下下降，有250kt速度限制
Phase 3-7 (CONF 1-FULL)：不同襟翼配置阶段
Phase 8 (LANDING)：着陆阶段

关键约束
路径约束

速度约束：M ≤ MMO, vCAS ≤ VMO
高度约束：特定阶段的高度限制
襟翼速度限制：VFE1, VFE2, VFE3, VFEFULL

控制约束 (方程IV.3)

下降梯度：γmin ≤ γ ≤ γmax
推力限制：Tmin ≤ T ≤ Tmax
速度刹车：0 ≤ β ≤ 1

终端约束 (方程IV.4)

着陆时的校准空速：vCAS = VREF
着陆高度：h = 50 ft

优化目标
成本函数 (方程IV.5)：最小化燃油消耗
πⱼ(v,h,T,γ) = q(v,h,T)/(v cos γ + w(h))
求解方法

建模框架：CasADi (符号自动微分框架)
求解器：SNOPT (序列二次规划算法)
数值积分：四阶龙格-库塔方法
可行性恢复：软约束方法

这个formulation非常完整，考虑了现实飞行中的各种操作约束和性能限制，能够生成符合实际飞行程序的优化轨迹。