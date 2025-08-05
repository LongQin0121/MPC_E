# RAMON 3 The energy-neutral timer window


In this chapter, the feasible time windows for energy-neutral trajectories are quantified, assuming that the descent has been already initiated when the time of arrival at the metering fix needs to be changed by the on-board trajectory planner.
明假设飞机已经进入了下降阶段。在这种情况下，机载轨迹规划器需要调整飞机在计量点的到达时间。研究的重点是量化调整这一到达时间的可行范围，即在下降阶段开始后，如何在能量中性的条件下进行时间管理和轨迹调整。

## 1. State of the art
Another important limitation of previous works is that none of them (up to our best knowledge) took into account the remaining descent between the metering fix at which the CTA was assigned and the instrumental landing system (ILS) interception or the runway threshold. Adjusting the descent speed profile to minimise or maximise flight time may result in a change to the altitude at which the metering fix is overflown. If the energy of the aircraft at this fix were too low, additional thrust might be needed after overflying it, interrupting in this way the CDO. Similarly, if the energy were too high, it might be required to use speed brakes and/or to deploy high-lifting devices or the landing gear earlier than initially planned, leading to more airframe noise.
这段文字指出了之前研究中的一个重要限制，即在研究CTA分配时，未考虑从计量点到仪表着陆系统（ILS）截获点或跑道阈值之间剩余的下降阶段。这些细节可能会对飞行的能量管理产生重大影响。具体分析如下：

未考虑的下降阶段: 之前的研究在计算CTA时通常集中在计量点本身，而不考虑其与着陆阶段之间的剩余下降距离和能量需求。因此，在这些研究中未能系统评估整个下降阶段的能量管理问题。

速度轮廓调整的影响: 调整下降速度曲线以最小化或最大化飞行时间可能会导致飞机在计量点上空飞行的高度发生变化。如果飞机此时的能量过低，可能需要额外的推力来维持飞行路径，从而中断连续下降操作（CDO）。

高能量的解决方案: 如果飞机的能量过高，则可能需要使用减速板，提前部署增升装置或起落架来降低速度，而这些措施可能会导致更多噪声，这违背了某些环境目标。

简单来说，这段话强调了完整飞行规划中考虑所有下降阶段的重要性，尤其是计量点之后的路径。如果不尽可能精确地调控飞机能量，可能会破坏原本的能量中性目标，增加油耗和噪音污染。这提醒我们在研究和规划CDO时，需要全面考虑飞行状态及其在各个阶段的影响，以优化整体飞行性能和环境表现。




## 4. Discussion
这段讨论汇总了关于在终端机动区（TMA）引入连续下降运行（CDO）的研究观察与结论，特别是在处理到达时间控制（CTA）方面的影响。让我们分解这些重点信息：

CTA与空域能力： 有效的CTA分配能够促进CDO的实施，而CDO在空域容量和环境目标之间存在矛盾的权衡。

可行时间窗口的量化： 研究量化了空客A320在履行能量中性的CDO时的可行CTA时间窗口。具体而言，在理想飞行条件下，这些窗口可以达到2.8分钟。

先前分配的CTA的影响： 事先分配的CTA或成本指数（CI）对可调整的CTA窗口有显著影响。

最低时间与最低燃油： 研究发现最快的轨迹与最低燃油消耗的轨迹相似，只要优化是在下降过程中进行，且不使用额外的推力或减速装置。

鲁棒性与燃油消耗的权衡： 在不确定性中，为了实现稳定和最佳的CDO，若面对晚期更新，适当增加燃油消耗可能是有益的。

影响因素：

飞机重量: 较轻的飞机有更宽的可行时间窗口。

顶风条件: 顶风会缩小飞行条件范围，但增加可行时间窗口的幅度。

高速度: 在高速度飞行时接收CTA更新通常更有利。

计量点距离: 距离计量点越近，时间窗口越窄。

章节关键结论： CTA可以在飞过下降顶部（TOD）后进行更新，在某些飞行条件下，仍然可以达到较大的能量中性时间窗口。

通俗地说，该研究揭示了优化到达时间和飞行路径的复杂性，以及如何在实质性的条件下保持能量效率。在这些方面进行有效的分配和调整，可以帮助在飞行操作中达到高效和环境友好的效果。