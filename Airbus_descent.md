  # Getting to Grips with Aircraft Performance

  # DESCENT/Holding

  γ = Descent gradient

  RD = Rate of Descent (Vertical Speed) : The rate of descent (RD) represents the vertical component of the  aircraft’s speed. It is negative and expressed in feet per minute.

## 1.2 Descent Equations

While climb is due to excess thrust, descent is, on the other hand, caused by a lack of thrust. Therefore, the descent gradient and the rate of descent, which depend on the difference (Thrust – Drag), are negative.


### 1.2.1. Descent Gradient (γ)

```python
At a given weight, the magnitude of the descent gradient is minimum when the drag is minimum, or when the lift-to-drag ratio is maximum. The minimum descent angle speed is, therefore, green dot speed.
```

### 1.2.2. Rate of Descent (RD)

```
Conclusion: At a given aircraft weight, the rate of descent is minimum, when `TASxDrag` is minimum.
```

### 1.2.3. Speed Polar 速度极曲线
![alt text](ed2f9161-61d2-4412-bcff-c9423b9f7585.png)

The example below (Figure H2) illustrates both thrust and drag forces, as opposed to True Air Speed.  The above equations indicate that, for a given weight:  • The descent angle (γ) is proportional to the drag force, which is at its  minimum at green dot speed.  • The rate of descent (RD) is proportional to the power of the drag force. As RD = TAS.γ, the minimum rate of descent is obtained for a TAS lower than  green dot (when dRD/dTAS = 0).

## 1.3. Influencing Parameters
### 1.3.1. Altitude Effect
![alt text](7bb9c11d-5931-49d4-9d29-25f5224090b1.png)


FMS（飞行管理系统）并不直接调整飞机的飞行路径角（flight path angle）来控制垂直速度（下降率），而是通过设定垂直速度目标指令发给自动飞行控制系统（AFCS）。AFCS通过调节飞机的俯仰角（pitch angle），间接改变飞机的飞行路径角，从而实现对垂直速度的控制。

具体几点如下：

飞机的垂直速度（也即下降率）和下降梯度是由垂直速度控制系统管理的。FMS计算出所需的垂直速度（基于飞行计划高度、速度目标等），将其作为目标输入给AFCS。

AFCS核心是通过改变俯仰角来调节飞机的纵向运动，俯仰角的改变会引起飞行路径角（flight path angle，即飞机在垂直面内的航迹倾角）的变化，从而改变垂直速度。

飞行路径角的改变不是直接由FMS命令，而是飞控系统通过俯仰角调整来“实现”FMS设定的垂直速度目标。

如果不进行这种垂直速度控制，下降率和下降梯度在飞机处于怠速（idle）且不调俯仰角时确实会持续增大，这不符合飞行计划和安全舒适要求。

总结：
FMS通过设定垂直速度目标来“间接”控制下降率，AFCS通过调整俯仰角来改变飞行路径角，实现这一目标，从而防止下降率和下降梯度持续无序增大。

这一机制解释了为什么切换飞行模式时，下降梯度会出现明显变化，因为FMS调整了目标垂直速度，飞控系统对应调整俯仰姿态和飞行路径角来配合实现控制目标。

风的影响本质：影响的是地面轨迹而非空中性能，这对航路规划至关重要！




速度差异是关键：
巡航速度 vs 下降速度：

巡航速度：M0.78 ≈ 470kt TAS
下降速度：300kt IAS ≈ 350kt TAS（平均值）

重新计算时间：
策略1 - 早下降：

全程下降：125nm ÷ 350kt = 21.4分钟

策略2 - 晚下降：

平飞段：25nm ÷ 470kt = 3.2分钟
下降段：100nm ÷ 350kt = 17.1分钟
总时间：3.2 + 17.1 = 20.3分钟

结论：
策略2更快！快约1.1分钟
为什么策略2更快？
高速平飞的优势：

在高效的巡航速度下快速覆盖距离
470kt vs 350kt的速度差异显著

下降速度限制：

下降时受到速度限制（安全、舒适性、管制要求）
无法维持巡航的高速度

修正后的全面对比：
策略1：燃油省，但稍慢
策略2：燃油多耗，但更快
实际选择考虑：

时间敏感：选策略2
燃油经济：选策略1
管制要求：通常倾向策略2

感谢你的质疑！高速巡航段确实提供了时间优势。

非常好的工程问题！慢车下降的高距比确实有物理和运营边界。
高距比变化的可能性：
可以增大（更陡下降）的限制：
1. 速度限制：

过陡下降 → 重力加速 → 超速风险
VMO/MMO限制
管制速度限制（如250kt below FL100）

2. 下降率限制：

乘客舒适性：>1,500 ft/min会引起不适
结构载荷：过大的垂直速度产生载荷

3. 能量管理：

过陡下降会导致能量过剩
接近机场时可能需要放减速板消散能量

可以减小（更平缓下降）的限制：
1. 物理下限：

最小自然下降梯度：约对应绿点速度
大概180-220 feet/nm (1.7°-2.1°)
更平缓就需要增加推力，不再是idle下降

2. 实际运营：

过于平缓会导致下降距离过长
影响空域效率和航路规划

典型范围：
慢车下降高距比范围：

最小：~200 feet/nm（绿点速度附近）
最大：~400 feet/nm（速度和舒适性限制）
常用：240-300 feet/nm

控制方法：
调节高距比的手段：
增大高距比（更陡）：

提高下降速度（但受限制）
使用减速板增加阻力
改变构型（放襟翼等）

减小高距比（更平缓）：

降低速度至绿点速度附近
但不能无限减小

实际考虑：
240 vs 300 feet/nm都在合理范围内

可以通过速度调节在此范围内选择
240：接近最佳滑翔，较平缓
300：稍陡但仍舒适，节省时间

总结：慢车下降的高距比可调节但有边界，大约在200-400 feet/nm之间，主要受速度限制和自然下降梯度限制。RetryH但是还可以再小吗？小于绿点对应的高距比？Edit分析下降速度与高距比，确定最佳飞行策略。6s用户问的是能否在慢车下降时实现小于绿点速度对应的高距比（更平缓的下降）。这是一个很好的技术问题。
让我想想：

绿点速度对应最大升阻比，即最小阻力
根据公式 γ = -D/W，在慢车推力（T≈0）时，γ = -D/W
如果要让下降梯度更小（更平缓），就需要阻力更小
但绿点速度已经是最小阻力点了
低于绿点速度，阻力会增加（诱导阻力增加）
高于绿点速度，阻力也会增加（摩擦阻力增加）

所以在纯慢车推力下，理论上不能比绿点速度对应的高距比更小。
但是，如果要实现更平缓的下降，就需要：

增加推力（不再是idle推力）
或者使用其他方法

让我再想想实际情况：

如果飞行员想要更平缓的下降，可能需要稍微增加推力
这就不再是纯粹的idle下降了
这就进入了"adapted thrust"的范围
**非常尖锐的技术问题！**答案是：理论上不能，实际上需要改变策略。
理论分析：
绿点速度的物理意义：

L/D最大 = 阻力最小
在慢车推力下：γ = -D/W
绿点速度提供最小可能的下降梯度

偏离绿点速度的后果：
速度低于绿点：

诱导阻力急剧增加：Di ∝ CL² ∝ 1/V²
总阻力增加 → 下降梯度增大（更陡）

速度高于绿点：

摩擦阻力增加：D0 ∝ V²
总阻力增加 → 下降梯度增大（更陡）

结论：
在纯慢车推力下，绿点速度对应的高距比是理论下限！
如果需要更平缓下降：
必须放弃"idle下降"：
1. 增加推力（Adapted Thrust）：

推力 > 慢车推力
公式变为：γ = -(D-T)/W
T增加 → γ减小（更平缓）

2. 能量管理策略：

提前减速到更低速度
利用能量转换实现平缓下降

3. 分段下降：

部分idle + 部分powered下降

实际运营中：
为什么很少这样做？
效率考虑：

增加推力 = 增加燃油消耗
违背了idle下降的经济性初衷

管制偏好：

过于平缓的下降占用过多空域
影响交通流效率

总结：
绿点速度的高距比是慢车下降的物理下限
要更平缓 = 必须增加推力 = 不再是idle下降
这就是为什么200-220 feet/nm通常是连续下降运营的平缓极限！

是的，完全正确！
速度关系排序：
从小到大：

最小速度（失速速度/最低操作速度）
最小下降率速度
绿点速度
更高速度

数学验证：
最小下降率的条件：
d(RD)/d(TAS) = 0
展开：d(TAS × D/W)/d(TAS) = 0
得到：D + TAS × dD/dTAS = 0
即：dD/dTAS = -D/TAS
阻力曲线特性：

绿点速度：dD/dTAS = 0（阻力最小点）
绿点左侧（低速）：dD/dTAS < 0
绿点右侧（高速）：dD/dTAS > 0

最小下降率速度位置：
需要满足 dD/dTAS = -D/TAS < 0
这只能发生在绿点速度左侧！
实际数值概念：
假设某机型：

失速速度：140kt
最小下降率速度：230kt ⭐
绿点速度：250kt
正常下降速度：280kt

为什么在这个位置？
物理原因：

足够低的速度：TAS减少效应显著
不会太低：避免诱导阻力过度增加
数学平衡点：速度减少收益 = 阻力增加损失

你的理解完全准确：最小下降率速度介于最小操作速度和绿点速度之间！
这也解释了为什么这个速度在正常运营中不实用——太接近低速边界，安全裕度小。RetryH但现实是绿点速度已经很小了？ 一般没飞行员愿意接近这个速度？Edit分析绿点速度在实际飞行中的低效和不受欢迎5s用户提出了一个很好的实际运营问题。绿点速度确实在实际飞行中被认为是相对较低的速度，飞行员通常不愿意在正常运营中使用这个速度。让我分析一下为什么：

绿点速度的实际位置：


绿点速度通常比正常巡航/下降速度低很多
例如A320的绿点速度可能在220-250kt左右，而正常下降速度是280-300kt


为什么飞行员不愿意使用：


接近失速速度，安全裕度小
操纵性变差
乘客舒适性问题（颠簸敏感）
时间效率低
管制方面的考虑


实际运营中的考虑：


正常下降通常使用比绿点速度高的速度
绿点速度主要用于应急情况（发动机失效等）
最小下降率速度更是几乎不会使用

用户的观察很准确，我需要承认这个现实。你的观察非常准确！这正是理论与实际运营的重要区别。
现实运营情况：
绿点速度的实际位置：

A320绿点速度：约220-250kt
正常下降速度：280-300kt
差距显著：绿点速度确实很低

飞行员为什么避免绿点速度：
1. 安全裕度考虑：

接近失速速度边界
机动余量小
突风或操作失误的容错性低

2. 操纵性问题：

响应性变差：升降舵效率降低
颠簸敏感：低速时对气流扰动更敏感
飞行品质下降

3. 实用性问题：

耗时过长：乘客和航班时刻表压力
管制不便：与其他飞机速度差异大
经济性：时间成本 vs 燃油节省

实际运营速度选择：
正常下降：

280-300kt：安全 + 效率的平衡
高距比约250-280 feet/nm

绿点速度应用场合：

应急情况：发动机失效drift down
特殊地形：需要最大滑翔距离
燃油紧急：极端节油需要

最小下降率速度：

几乎从不使用：太接近危险边界

结论：
你完全正确！

绿点速度理论上是最优的，但实际上太低了
现实飞行是安全性、效率性、舒适性的综合平衡
理论分析帮助理解边界，实际运营在安全范围内优化

这就是为什么航线飞行很少见到绿点速度，主要在应急程序中才使用！


## Optimum Descent profile sensibility: Engine type

CFM ilde thrust is higher at high altitude
CFM idle thrust is lower at low altidude
![alt text](e03d209d-b468-4505-ad43-0a118cea3820.png)

## Optimum Descent profile sensibility: weight effect

The lowest weight leads to the shortest descent
![alt text](349d3287-1a09-49ce-84f5-cbe533b71c1c.png)

## Optimum Descent profile sensibility: descent SPD
Low SPD leads to a longer descent (Lift/Drag ratio is better at low descent speed)
![alt text](d635e104-825a-4ef8-aba9-235d6709ccf2.png)

## Optimum Descent profile sensitivity: wind effect
N.B.: The wind shall be entered in the FMS to impact Top of Descent position.
![alt text](75fd4468-4963-4a9b-8b9f-d33a72c1e001.png)

Remind of the main recommendations:
 “Window” ALT constraints shall be preferred compared to “AT”
 Altitude constraints shall not impose a “too steep” flight path angle to the aircraft
(too steep path required the use of Airbrake)
 The average local wind shall be considered (10kts of tailwind shall decrease the
limit slope by 0,1°)
 A gentle slope (between -1°to -1,5°) shall be allow ed before glide slope
interception
 The transition altitude shall be preferably above FL100
 Speed restrictions below 230kts and far from the FAF shall be avoided (this leads
to early S/F extension)
 The noise level can be reduced by using a SPD Limit at 230kts instead of 250kts


## Recommendations for CDO procedure design: limit slopes at constant CAS for the whole Airbus fleet
![alt text](548ab819-5781-48bf-bcbf-e1b70bd50087.png)