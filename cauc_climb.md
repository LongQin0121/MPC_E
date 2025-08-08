# 飞机性能工程
## 5.1 爬升性能

起飞飞行航迹结束点 End point of takeoff flight trajectory

航路爬升： 从起飞飞行航迹结束点（1500ft）爬升到规定的巡航高度  
推力： 最大爬升推力， 全发；
目的: 经济安全   
重点： 时间 油量 距离    
Climb Route: Ascend from the end point of the takeoff flight path (1500ft) to the specified cruising altitude.
Thrust: Maximum climb thrust, all engines.
Objective: Economic safety
Key focus: Time, fuel consumption, distance

### 5.1.1 
爬升参数的计算    爬升参数的计算  爬升梯度与爬升率
Calculation of Climb Parameters    Climb Gradient and Climb Rate

飞机轴线（Aircraft Axis） 
气动轴线（Aerodynamic Axis）


爬升中除了满足不同的要求外， 为了便于飞行员操纵， 采用等表速/等马赫数爬升， 在低空等表速爬升， 在高空考虑压缩性的影响， 按固定马赫数爬升。
In addition to meeting different requirements during the climb, to facilitate pilot operation, a constant indicated airspeed/constant Mach number climb is used. At lower altitudes, a constant indicated airspeed climb is utilized, while at higher altitudes, considering compressibility effects, the climb is conducted at a constant Mach number.

低空等表速爬升时， 及Vc=C, Hp 上升， Vr上升   是加速爬升过程， 部分剩余推力用来增加动能。  
During a constant indicated airspeed climb at lower altitudes (Vc=C), as altitude (Hp) increases, the true airspeed (Vr) also increases. This process is known as an accelerated climb, where part of the excess thrust is used to increase kinetic energy.


高空等M数爬升时， Hp上升， a下降， Vr下降， 是减速爬升。   达到对流层顶后， 再向上等M爬升， 真空速不变。 


这段描述解释了飞机在高空以恒定马赫数（等M数）进行爬升时的气动变化。以下是对各个部分的解释：

恒定马赫数爬升（等M数）：飞机保持恒定的马赫数进行爬升。这意味着飞机的速度相对于音速的比率保持不变。

Hp上升（高度上升）：飞机在爬升过程中不断上升到更高的高度。

a下降（空气密度下降）：随着高度增加，空气密度下降。这会影响飞机的空气动力学特性。

Vr下降（真实空速下降）：虽然飞机保持恒定的马赫数，空气密度下降导致真实空速（Vr）下降。这是因为保持相同的马赫数，在低密度空气中需要更低的真实空速。

减速爬升：由于真实空速下降，即使保持恒定的马赫数，可能会感受到一种“减速”效应，因为真实空速在下降。

达到对流层顶后，再向上等M爬升，真空速不变：在对流层顶之后，大气温度趋于稳定或变化不明显，因此在等马赫数爬升时，真实空速（Vr）可以保持不变。这是因为在对流层顶和以上的平流层中，温度变化对音速和马赫数的影响不同于对流层。

这种方法在高空飞行中很常见，尤其是在巡航阶段优化飞行性能和燃油效率。真空速的恒定有助于确保飞机在高空的稳定性和经济性。
This description explains the aerodynamic changes that occur during a constant Mach number climb (constant M) at high altitudes. Here are the details of each aspect:

Constant Mach Number Climb (Constant M): The aircraft maintains a constant Mach number during the climb, meaning the ratio of its speed relative to the speed of sound remains unchanged.

Hp Increase (Altitude Increase): The aircraft continues to ascend to higher altitudes during the climb.

a Decrease (Air Density Decrease): As altitude increases, air density decreases, which impacts the aircraft's aerodynamic characteristics.

Vr Decrease (True Airspeed Decrease): Although the aircraft maintains a constant Mach number, the decrease in air density leads to a reduction in true airspeed (Vr). This is because, at lower air densities, maintaining the same Mach number requires a lower true airspeed.

Decelerated Climb: Due to the decrease in true airspeed, there might be a perception of "deceleration" even while maintaining a constant Mach number because the true airspeed is decreasing.

After Reaching the Tropopause, Climbing Further with Constant M, True Airspeed Remains Constant: Beyond the tropopause, the atmospheric temperature tends to stabilize or change minimally. Thus, during a constant Mach number climb, the true airspeed (Vr) can remain constant. This is because, in and above the tropopause, the effect of temperature changes on sound speed and Mach number is different from that in the troposphere.

This method is common in high-altitude flight, especially for optimizing flight performance and fuel efficiency during the cruise phase. Maintaining a constant true airspeed helps ensure the aircraft's stability and economy at high altitudes.

陡升爬升 vs 快升爬升:

   `爬升距离最短（陡升爬升）`： 从起飞到爬升顶点的水平距离最短， 爬升梯度最大 , 以陡升速度爬升， 对应绿点速度。    
   `爬升时间最短（快升爬升）`： 从起飞到爬升顶点的时间最短， 爬升率最大，快升速度爬升。   

   速度大了，升梯度上不去；升梯度大了，速度就跑不上去。If the speed is high, the climb gradient can't be large; if the climb gradient is large, the speed can't be high.



   ```````````````
从飞机起飞结束（1500英尺）到达规定的巡航速度和

高度的过程，称航线爬升。民航运输机典型航线上升程序为：在中低空保持等表速上升，在高空保持等M数上升。

Key Differences from Vx (Best Angle of Climb):
Vx: Best angle of climb speed provides the greatest altitude gain over a given horizontal distance, useful for clearing obstacles during takeoff. 
Vy: Best rate of climb speed provides the greatest altitude gain per unit of time, used for quickly reaching a desired altitude. 
Always Different (Usually): Except at the aircraft's absolute ceiling, Vx is always lower than Vy. 

爬升航段燃油消耗最少的爬升方式。 它近似对应于最大爬升率的爬升， 但考虑到飞行员的操作方面的要求， 近似与等表速， 等马赫数的爬升方式，

Vy约等于cost index等于0.


# 下降性能

Vy（最大爬升率速度）
定义：能够提供最大垂直爬升率（英尺/分钟）的空速
目的：在最短时间内获得最大高度增益
特点：

通常比最佳滑翔速度稍快
优化的是爬升性能，不是燃油效率
主要用于起飞后初始爬升阶段

Cost Index = 0的速度
定义：巡航阶段最经济的飞行速度
目的：获得最低的燃油消耗率（每海里燃油消耗最少）
特点：

通常比Vy慢很多
优化的是燃油经济性
用于巡航阶段的长距离飞行

为什么不同？
飞行阶段不同

Vy用于爬升阶段
CI=0用于巡航阶段

优化目标不同

Vy优化爬升率（时间效率）
CI=0优化燃油效率（成本效率）

空气动力学考虑

爬升时需要克服重力，速度-功率关系与平飞不同
巡航时主要克服阻力，追求升阻比最佳点

实际数值举例（以B737为例）

Vy：大约140-160节
CI=0巡航速度：大约M0.74-0.76（高度和重量相关）

所以这两个速度概念完全不同，不能等同。Vy关注爬升效率，而CI=0关注巡航时的燃油经济性。

\A320的最佳爬升率速度（Vy）不是固定值，会随着飞机重量、高度、气温和大气压力等条件变化而变化。一般经验法则是：

在干净配置下，最佳爬升率速度Vy大约为绿点速度（Green Dot Speed，即最佳升阻比速度）乘以1.3左右。

绿点速度是飞机仪表上的一个小绿色圈，代表飞机在当前条件下的最佳升阻比速度，Vy一般高于绿点速度。

换句话说，A320的Vy速度通常位于绿点速度和经济爬升速度之间，多数情况下可取绿点速度的1.3倍作为参考，但具体数值需参考飞机重量和爬升高度等因素计算。

所以没有固定的某一数值，典型情况下：

Vy ≈ 1.3 × 绿点速度

此速度确保最大垂直爬升率，有利于快速达到巡航高度并节省时间和燃料。

