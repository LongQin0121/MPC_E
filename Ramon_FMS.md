# Optimal trajectory management for aircraft descent operations subject to time constraints

# 1.  Introduction

✈️ 机载系统介绍 / On-board Systems Introduction

RAMON DALMAU CODINA - This PhD thesis only focuses on the on-board systems required to satisfy CTAs during CDOs.

🌐标题 / Title:
🌐实现连续下降操作期间满足控制到达时间要求的飞行管理系统
🌐Flight Management System for Satisfying Control Time of Arrival Requirements during Continuous Descent Operations

🌍✈️📉介绍 / Introduction:
现代航空对能满足精确时刻到达要求的飞行路径规划有着严格的需求。在连续下降操作（CDOs）中，实现控制到达时间（CTA）的关键在于采用先进的机载系统，其中飞行管理系统（FMS）扮演着核心角色。

Modern aviation demands precise time-of-arrival compliance for flight path planning. Achieving Control Time of Arrival (CTA) during Continuous Descent Operations (CDOs) relies on advanced onboard systems, with the Flight Management System (FMS) playing a pivotal role.

📌功能 / Functions:

实时轨迹规划 / Real-time Trajectory Planning:

FMS通过不断更新的环境信息（如风速变化），实时调整飞机的路径计划，以确保满足CTA要求。

The FMS dynamically adjusts the aircraft's trajectory plan with continuously updated environmental information (e.g., wind speed changes) to guarantee CTA compliance.

📌能量管理 / Energy Management:

采用智能能量管理策略，实现能量中和下降，以最小化燃油消耗和环境影响。

Employ intelligent energy management strategies to achieve energy-neutral descent, minimizing fuel consumption and environmental impact. `ONLY ELEVATOR`

📌敏感性分析 / Sensitivity Analysis:

进行敏感性分析以快速响应飞行路径的调整需求，优化资源使用和提高响应速度。

Conduct sensitivity analysis to quickly respond to trajectory adjustment demands, optimizing resource use and improving response speed.

📌综合优化 / Comprehensive Optimization:

整合多种指导策略，包括战术、战略和非线性模型预测控制（NMPC），以实现最佳飞行路径。

Integrate multiple guidance strategies, including tactical, strategic, and Nonlinear Model Predictive Control (NMPC), to achieve optimal flight path.

📌数据联网 / Data Networking:

通过网络共享风观测数据，实现更稳定和精确的路径规划。

Achieve more stable and precise trajectory planning by networking wind observation data.

🎯  总结 / Summary:
这套机载系统以其高效的实时规划、动态能量管理和多策略优化，为满足复杂空域中精确的到达时间要求提供了有力保障。这不仅提升了航班效率，也推动了航空运营的环保和经济效益。

This onboard system, with its efficient real-time planning, dynamic energy management, and multi-strategy optimization, robustly ensures precise time-of-arrival compliance in complex airspace. It not only enhances flight efficiency but also drives aviation operation's environmental and economic benefits.

🌍✈️📉系统的基本功能和作用！📘



```
Chapter V proposes two variants of the generic NMPC guidance strategy that rapidly update the optimal trajectory plan by using parametric sensitivities of the active trajectory plan. Then, the performance of these two variants are compared with those of an ideal NMPC, which updates the optimal trajectory plan instantaneously at each re-calculation instant, as well as those of the open-loop execution of the initial trajectory plan computed before the TOD.

```
在这个博士论文的研究范围内，水平路径不改变，主要关注的是优化控制到达时间（CTA）和下降的垂直剖面。

📌 具体内容说明：
CTA调整：

时间管理：核心是确保飞机在预计的时间到达指定点，时间调整可能涉及速度的调节以适应CTA。

下降剖面的优化：

垂直飞行剖面：调整飞行高度和速度以优化能量使用，并满足环境要求（例如减少燃油消耗和噪声）。

能量管理：利用升降舵和推力调整仅在垂直剖面上进行优化，而不是更改水平路径。

总结：
研究的重点是确保在既定的水平路径上，通过精细调整垂直飞行剖面和时间管理策略，以增强飞行的效率和符合CTA，而不改变整体飞行路线。若需要更多信息，请随时提出，我会乐意提供更深入的解释和支持！📈✈️



# 2. Framework on trajectory management
### 
Since this PhD thesis assumes an operational concept in which the lateral route is fixed and only the vertical profile is managed to satisfy controlled time of arrivals (CTAs), the concept of trajectory plan will refer `only` to the vertical profile.

In current FMSs, the trajectory plan is constructed by `numerical integration of the differential equations` of the mathematical model describing the dynamics of the aircraft.

未来的飞行管理系统（FMS）将能够更优地规划和执行连续下降操作（CDOs），同时满足控制到达时间（CTAs）的要求。这些系统需要具备以下能力：

实时轨迹规划算法：需要能够快速生成实时最优轨迹计划，以符合输入的要求到达时间（RTAs）和典型的运行约束。这意味着系统可以动态调整并优化飞机的下降路径，以实现高效和精确的时间管理。

满足RTAs的指导系统：需具备引导系统，以确保飞机能在遵守环保要求的同时满足RTAs。这要求系统在规划过程中即使出现模型误差，也能找到最节能的飞行路径。

通俗的说，就是未来的飞机导航系统将能够动态调整飞行路径，以确保准时抵达，同时尽量减少对环境的影响，即减少噪音和排放。即使在计算上有一些小误差，系统仍力求找到最节能且环保的飞行方案。 

### 数值法  VS 解析法
`Analytical methods`: These involve solving problems using exact formulas or symbolic manipulations, such as solving quadratic equations, calculating integrals, and performing rational number operations. They provide exact solutions through mathematical derivations and symbolic computations, like:

Formula-based solutions: Using formulas such as the quadratic formula or integral expressions to obtain precise values.

Algebraic manipulations: Employing algebraic rules for symbolic calculations.

Calculus formulas: Using calculus-based derivations to solve differential equations or integration problems.

In high school, these are the traditional, rigorous approaches that are taught.

`Numerical methods`: These methods provide approximate solutions and are used when analytical solutions are difficult or impossible to obtain due to complexity (like nonlinear equations or equations that can't be easily expressed using simple formulas). Numerical methods are particularly suited for computation, utilizing iterative and approximation techniques to achieve desired accuracy. They are efficient for handling real-world complex problems often modeled computationally.

Each approach has its strengths: analytical methods offer exact solutions, while numerical methods are more practical for complex, real-world applications where precision might be sacrificed for efficiency and solvability.

## 2.1 Models needed for trajectory management

✅ 通俗解释：
ODE 像是“自由演化”：你推一辆车下坡，只要知道初始速度和坡度，它自己会滚下去。

DAE 像是“受约束的演化”：现在加了一个刹车规定“车速必须保持60km/h”，于是每次车速一变，你必须用刹车或油门去强制调整，保持这个代数条件成立。

因为多了这个“强制条件”，就不再是纯粹的 ODE 了，必须变成“微分 + 代数”的混合系统（DAE）。
![alt text](1fb18f98-3682-4d38-b561-bf666b001a3a.png)
![alt text](47e2a79e-ea87-4ab6-9328-8d24359ced13.png)

### 2.1.1 Aircraft dynamics model

质量模型的特点：动力学考虑：

质量：假定飞机为一个集中于单点的质量。


由于只考虑平移运动，点质量模型不需要模型复杂的惯性张量，转动和稳定控制回路被视为高阶动力学并忽略。

主要物理因素包括：

`空气动力：如升力与阻力。`

`推进力：发动机提供的推力。`

`外部力：重力等。`

### 2.2.1 Optimal control problem formulation

As mentioned before, the optimisation of the vertical profile of an aircraft trajectory can be formulated as a multi-phase, constrained optimal control problem (Soler et al., 2015). The formulation of a generic optimal control problem is presented in Section II.2.1. Since the trajectory optimisation problem tackled in this PhD thesis cannot be solved analytically due to the nonlinearity and complexity of the constraints and cost function, a discretisation approach is presented in Section II.2.2 to solve it numerically.

最优控制问题的多阶段建模
多阶段建模：通过将时间范围划分为多个阶段（或阶段），在每个阶段内应用不同的动态、运行成本及代数和路径约束。

初始和终止约束：确保状态变量在两个连续阶段是连续的，以保证解的连续性。此外，还可以设置内点约束。

多阶段问题的时间离散化：将整个时间范围分为若干时间样本，对于每个阶段进行单独处理。

非线性规划（NLP）求解
NLP 问题的定义：多阶段最优控制问题被公式化为参数化的非线性规划问题（Eq. (II.16)），其中目标是最小化某一代价函数并满足一系列等式和不等式约束。

求解方法：

直接方法：这些方法相对容易设置，并针对时间和状态的离散化，将问题转化为有限维的非线性规划问题。

间接方法（省略于本博士论文）：通常需要更复杂的数学分析，适用于非常简单或有特定初始条件的问题。

处理不可能的解决方案：几种方法来应对不满足约束的情况，例如：

约束松弛法：调整约束范围以恢复可行性。

瞬态约束违反法：允许在特定时间段内违反约束。

软约束法：引入松弛变量以允许约束的有限松弛。

处理表格数据：使用逼近技术如多项式拟合或样条曲线来平滑表格数据，以确保数据的连续性和可微性。

潜在挑战和应对策略
间接和直接方法的比较：直接方法更适合此类复杂动力学问题，而间接方法因为需要详细的数学分析而不被选择。

使用样条曲线：例如，Betts（2010）建议在逼近复杂数据时使用张量乘积样条，它们在节点处保留足够的连续性和可导性。

总的来说，该章节在细致地探讨如何在复杂的动态系统中进行轨迹的多阶段最优控制，并提供了支持这些复杂计算的实用建议和数学工具。这些方法帮助在不同行为和状态变化情况下有效优化轨迹，实现更好的解决方案。




A trajectory plan computed by solving the problem described in Section II.2 is just that: a plan. In order to materialise it, the FMS uses its guidance system, which continuously generates commands for the elevator and throttle/speed brakes to nullify deviations from certain variables included in (or derived from) the trajectory plan z~.

If having two actuators at one’s disposal, only two variables can be simultaneously controlled. Accordingly, several guidance strategies can be defined, depending on which variable is controlling the elevator and which variable is controlling the throttle/speed brakes, and which mechanisms these actuators use to correct deviations.

1. Trajectory Guidance概述
轨迹计划：通过解决复杂的控制问题来生成，但本质上还是一个理论性的计划。

飞行管理系统（FMS）：利用指导系统通过操控升降舵和油门/减速板来修正轨迹偏差。

2. 基于TEMO的能量管理
飞机总能量（Et）：由动能（Ek）和势能（Ep）组成。

受推力和气动阻力的影响，通过调整能量，可以在速度和高度之间转换来修正时间和能量的偏差。

1. 指导策略
战术指导：

以速度-升降舵控制为基础，通过调整飞机姿态来维持速度，而油门和减速板用于保持预定能量水平。

主要优势在于精确跟随计划的轨迹，但可能对环境和发动机不利。

战略重规划：

追踪校准空速（CAS）及推力计划，且只在达到偏差阈限时对轨迹进行重新规划。

在考虑整个剩余的飞行过程时，能够更全面地抑制偏差。

混合指导：

结合战术和战略策略，例如，使用升降舵战术纠正持续时间误差，而通过推力策略来解决能量偏差。

非线性模型预测控制（NMPC）：

理想NMPC（INMPC）：即理想状态下实现即时轨迹更新，但在实际操作中计算复杂度高。

基于敏感度的NMPC（SbNMPC）：利用小参数扰动下的线性敏感度快速更新轨迹。

先进步NMPC（AsNMPC）：在时间样本提前解决优化问题，但可能无法准确提前计算由于模型误差引起的相应控制。

在这些策略中，选择合适的方法取决于任务要求和计算能力，以达到在精确性和实用性之间的最佳平衡。这些方法帮助航空动力学系统通过精准的操控来确保飞机按计划运行，同时有效地应对各种环境和动态变化。


第一段：计算最优轨迹
多阶段建模：

通过将飞行过程分解为多个阶段或时段，每个阶段有不同的动态、运行成本和约束条件。

目标是解决一个多阶段的最优控制问题，通过数学优化技术（如非线性规划）来找出轨迹规划。

数学形式和方法：

利用微分方程和代数约束来定义系统的行为。

采用直接或间接方法解决轨迹优化问题，确保生成的轨迹满足所有给定的约束条件并最小化目标函数。

第二段：执行最优轨迹
飞行管理系统（FMS）指导：

使用不同的指导策略来操作飞机，以实际接近计算出的最优轨迹。

管理包括升降舵、油门和减速板等的使用，以控制飞机的速度和高度，调整能量状态。

策略和能量管理：

不同的指导策略（如战术指导、战略重规划、混合指导）根据能量管理的原则调整飞机的操作。

目标是动态响应偏差，比如时间或能量的变化，以实现精确的航班控制。