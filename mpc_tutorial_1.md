
#### https://towardsdatascience.com/model-predictive-control-basics/
# Model Predictive Control Basics
#### A hands-on tutorial with Python and CasADi
Willem Esterhuizen

## 升级版公式

### 原始系统 + 显式输出
```python
# === 状态演化（如何变化）===
x_{k+1} = A x_k + B u_k

其中：x_k = [位置_k, 速度_k]^T ∈ R^2

# === 输出方程（控制什么）===  
y_k = C x_k + D u_k

其中：C = [1, 0]  # 只输出位置
     D = [0]      # 输出不直接依赖当前控制
     y_k ∈ R^1   # 1维输出：位置

# === 控制（用什么手段）===
u_k ∈ R^1  # 1维控制：力

```

### 升级版优化问题
```python
OCP_with_output(x̄):

minimize: ∑_{k=0}^{K-1} [y_k^T Q_y y_k + x_k^T Q_x x_k + u_k^T R u_k] + y_K^T Q_{yK} y_K

subject to:
    x_{k+1} = A x_k + B u_k,     k ∈ [0:K-1]  # 状态演化约束
    y_k = C x_k + D u_k,         k ∈ [0:K]    # 输出定义约束  
    x_0 = x̄,                                  # 初始条件
    y_k ∈ [-1, 1],              k ∈ [0:K]    # 输出约束（位置限制）
    u_k ∈ [-1, 1],              k ∈ [0:K-1]  # 控制约束
```

### 关键升级点总结

#### 1. 显式三层结构

```python
# === 三者明确分离 ===
状态 x: [位置, 速度]      # 系统内部演化变量
输出 y: [位置]           # 我们真正关心控制的量  
控制 u: [力]            # 我们的控制手段

# === 数学关系 ===
x_{k+1} = A x_k + B u_k  # 状态演化（如何变化）
y_k = C x_k + D u_k      # 输出定义（控制什么）  
u_k 通过改变 x_k 来影响 y_k  # 控制逻辑（用什么手段）

```

#### 2. 输出方程设计
```python
C = [1, 0]  # 只输出位置，不输出速度
D = [0]     # 输出不直接依赖当前控制

# 这意味着：我们主要关心位置控制，速度是辅助状态

```

#### 3. 分层成本函数
```python

# 原版：J = x^T Q x + u^T R u
# 升级：J = y^T Q_y y + x^T Q_x x + u^T R u
#           ↑         ↑         ↑
#        输出成本   状态成本   控制成本
#       (主要目标) (辅助调节) (平滑控制)
```

#### 4. 约束直接施加在输出上
```
# 原版：x[0] ∈ [-1,1]  (直接约束状态)
# 升级：y ∈ [-1,1]     (约束输出，更有物理意义)

```

####  运行效果示例
```
=== MPC with Explicit Output Equation ===
Initial output: y=0.50m (position)
Target: drive output (position) to 0

Step  0: output=0.500m, state=[0.500, 0.500], control=-1.000N
Step  1: output=0.549m, state=[0.549, 0.400], control=-1.000N  
Step  2: output=0.589m, state=[0.589, 0.300], control=-1.000N
...
Step 20: output=0.051m, state=[0.051, -0.123], control=0.334N
Step 30: output=-0.008m, state=[-0.008, 0.045], control=-0.127N

✅ Converged! Final output: 0.0003m
```
关键洞察：这个升级版清晰地展示了MPC三要素的分工：

状态：描述系统如何演化
输出：定义我们真正的控制目标
控制：提供影响演化的手段

通过输出方程，我们实现了"控制什么"与"如何演化"的优雅分离！🎯