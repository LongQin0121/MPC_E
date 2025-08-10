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

那为啥红色的conf1   放下襟翼和flat, 对最大下降梯度， 在高空和低空的影响差异这么大？


ChatGPT 说：
这是个很好的问题！襟翼配置（Conf1）和 "Flaps"（襟翼） 对 最大下降梯度 的影响确实在高空和低空的表现差异很大。这是由几个主要因素引起的：

1. 空气密度与飞行气动特性
低空（例如 0-5000 ft）时，空气密度较大，导致襟翼的作用更加显著。在这种高密度空气中，飞机的阻力增大，需要更多的升力来保持同样的速度。因此，襟翼的作用不仅增加了阻力，还增加了下降率，让飞机能够保持较浅的下滑角（通常会导致角度变得平缓）。

高空（例如 10000-15000 ft）时，空气密度较低，襟翼的影响减弱。在这种条件下，虽然飞机的阻力增加，但由于空气更稀薄，襟翼提供的额外升力并没有低空时那么强，而且下降速率的影响相对较小。这使得在高空使用襟翼时，可以实现更陡的下滑角，因为结构和气动特性更允许较大的下滑坡度，而不至于影响失速或推力边界。

2. 襟翼作用与飞机升力-阻力比
襟翼的使用影响升力和阻力比（L/D比），即升力与阻力的比例：

低空时，襟翼的增阻作用让飞机的升力需求增加，因此飞行员会选择更平缓的下滑角来避免过快下降。襟翼让飞机增加的阻力会限制飞机的坡度，避免推力过低或失速。因此，低空的“最陡下滑角”通常会较为保守。

高空时，由于空气稀薄，阻力的增加较少，襟翼所增加的阻力对飞行性能的影响较小。此外，在这种环境下，飞机的最大升力/最大推力通常能够维持更长时间，因此可以容忍更陡的下滑坡度。

3. 襟翼配置的速度限制
襟翼配置如 Conf1 是为了提高飞机的升力，但也会限制其最大速度，尤其是在高空时。虽然低空时襟翼提供更多的升力来保持较平缓的下滑角，但如果过度使用襟翼，则飞行器可能会受到速度的限制，导致无法继续按照较陡的坡度继续下滑，特别是在较低空域中。

4. 进近和飞行状态差异
低空进近：襟翼和 flap 配置通常会用来减速和增加升力，但这种配置下的下滑角度必须更加平缓，以确保飞行员有足够的时间对准跑道和进行稳定进近。

高空下降：在远离机场时，襟翼的作用则更多体现在减速方面，允许飞机以较高的速度继续下滑并提高效率。这时可以容许更陡的下降梯度，因为不需要考虑进近稳定性或过于精细的控制。

总结
因此，低空和高空的襟翼对最大下降梯度的影响差异，其实是由以下因素的共同作用：

空气密度：低空高密度空气与高空低密度空气对襟翼作用的不同。

升力-阻力比（L/D）：低空需要更平缓的坡度，而高空则能承受更陡的下降角。

飞行模式和配置：低空使用襟翼和 Flaps 是为了安全进近，而高空则为了更有效率的下滑。

在程序设计时，为了确保安全和稳定，通常会根据不同高度层的飞行需求，给出不同的下滑角度限制，保证襟翼配置在最适宜的时机使用。
是不是类似在高空起这减速增加阻力占主导， 到了低空是增加升力的功能占了主导？


ChatGPT 说：
没错，基本就是这个道理！你可以把这当作 高空和低空飞行中的两种不同“襟翼行为” 来理解：

高空 — 增加阻力占主导
在高空，由于空气密度较低，襟翼增加的阻力作用变得更加明显。飞机为了保持恒定速度和下降率，必须牺牲更多的动能。襟翼的作用主要是增加空气阻力，让飞机能减速并以较高的下降角度稳定下滑。

高空的特点：

由于空气稀薄，襟翼增加的阻力相对更为显著。

不会有太大升力需求，所以襟翼对升力的影响较弱。

飞机可以通过增加阻力来保持更大的下滑角度（即使是在飞行较快的速度下）。

低空 — 增加升力占主导
在低空，空气密度大，襟翼主要作用于增加升力，这使得飞机能够以较低的速度维持较平稳的飞行路径。然而，这也会导致飞机的阻力增加，因此必须保持较小的下滑角度，避免过于陡峭的下降。

低空的特点：

襟翼增加升力的作用更加明显，可以帮助飞机保持较低的空速，同时降低失速风险。

需要更保守的坡度限制，以防阻力过大导致推力不足或无法稳定下降。

由于升力增加，飞机也能更容易“承受”较小的下滑角，避免快速下降。

两者的结合：升力与阻力的平衡
所以，高空时，襟翼主要通过增加阻力来控制下滑角，而低空时，襟翼的升力增加作用更为显著，但也伴随更多的阻力，必须控制好下滑角以确保安全。

举个简单的例子：
高空：想象你滑雪下坡时，如果你在空气稀薄的高山坡上，你可以通过增大“雪板”接触面（相当于襟翼）来减速并加大坡度。减速和增加阻力帮助你控制速度和下滑角度。

低空：当你滑雪接近坡道底部，雪板的阻力和升力都更加显著，但如果坡度太大，过多的阻力会让你“停不下来”，因此你要保持较小的坡度。

总结来说，高空使用襟翼主要是为了控制速度（增加阻力），而在低空则是为了增加升力并保持较小、较稳定的下滑角。



## Recommendations for CDO procedure design: limit slopes allowing deceleration for the whole Airbus fleet
Example of the steepest slope allowing a deceleration rate of 4kts/10s

![alt text](e8040cdf-3d61-4197-9b16-0c4d8f54babe.png)
为什么要用「4 kt / 10 s 允许斜率」来做设计？
4 kt/10 s 是给定的减速能力/目标（约等于 0.4 kt/s，约 0.206 m/s²）。

如果下降太陡，飞机垂直下降速度大、通过速度限制区时可用时间短，就没有足够时间用减推力／迎角／阻力来把速度降低到目标值。

因此每个（机型+配置+重量+自动化模式+风）都会有一个最大允许下降斜率，超出它就可能在规定速限处超速。

## Recommendations for CDO procedure design:
Descent capability of Airbus fleet (constant CAS)

![alt text](a38a0cf5-fa16-4bec-851a-270031f81012.png)

## Recommendations for CDO procedure design:
Descent capability of Airbus fleet (deceleration)
与第一个图表的关键区别
这个图表的特殊条件：

减速率: -4kts/10s（每10秒减速4节）
同时进行: 下降 + 减速
Y轴: FPA（Flight Path Angle）飞行航迹角

数据对比分析
减速下降 vs 恒速下降：

减速下降角度: 约-1°到-2.5°（更平缓）
恒速下降角度: 约-2.5°到-3.5°（更陡）

为什么减速时下降更平缓？
能量管理原理：

总能量守恒: 动能 + 势能 = 常数
减速时: 动能减少，需要势能损失更慢
结果: 下降角度必须更平缓

实际意义：

飞机在进近阶段需要同时减速和下降
这个数据用于设计最后进近段的CDO程序
确保飞机能够平稳过渡到最终进近

CDO程序设计应用
分阶段设计：

高空段: 使用恒速下降数据（-2.5°到-3.5°）
中低空段: 使用减速下降数据（-1°到-2.5°）
最终进近: 标准3°下降角

这样的分析确保了整个下降剖面的连续性和可飞性。

## Fuel burn impact due to early descent

![alt text](image-2.png)


飞机配置：

A320-214: 着陆重量56吨
标准大气条件，无风

两种下降策略对比：

绿线: 最优下降时机
橙线: 提前下降（Early Descent）

关键发现
水平飞行的燃油代价：

FL350水平飞行: 50kg/段
FL100水平飞行: 78kg/段

早期下降的燃油损失：

额外消耗: 28kg燃油
原因: 提前10海里开始最优的T/D（Top of Descent）点

为什么低空飞行更费油？
物理原理：

空气密度: 低空空气更稠密，阻力更大
发动机效率: 高空稀薄空气中效率更高
推力需求: 低空需要更大推力维持速度

实际运营意义
CDO程序设计启示：

精确的T/D点计算至关重要
10海里的差异就能造成显著燃油损失
空管指令的时机直接影响环保效益

成本影响：

28kg燃油 ≈ 额外成本约$25-30
对于每日数百架次的机场，累计影响巨大

这就是为什么现代空管系统越来越重视精确的下降轨迹管理和4D航迹预测的原因。

## Fuel burn impact due to late descent
关键数据对比
延迟下降 vs 早期下降：

延迟下降额外消耗: 42kg 燃油
早期下降额外消耗: 28kg 燃油
延迟下降的代价更高: +50%

延迟下降的问题
能量管理挑战：

高度过高: 飞机在相同距离内高度太高
必须使用减速板: 增加阻力强制下降
能量浪费: 减速板将多余能量转化为热量散失

燃油消耗分解：

FL350水平飞行: 50kg/段（高空效率相对较好）
慢车下降段: 8kg（最经济的下降方式）
减速板使用: 造成显著额外消耗

为什么延迟下降更糟糕？
物理原因：

早期下降: 只是在低效率高度飞行更久
延迟下降: 需要主动浪费能量（减速板）
减速板: 纯粹的能量损失，没有任何效益

实际运营启示
空管管理重要性：

及时的下降许可比早期下降更关键
T/D点的精确性直接影响燃油效率
10海里的偏差可能造成40%以上的额外燃油损失

CDO程序设计：

必须确保飞机能够按时开始下降
空域设计要避免强制延迟下降的情况


## Fuel burn impact due to AT constraints  
![alt text](4dea206d-2dc8-405c-a4d0-317117ec3354.png)

## Conclusion about Aircraft capabilities in descent


