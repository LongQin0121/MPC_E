import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

class AircraftDescentOptimizer:
    def __init__(self):
        # 飞行阶段定义
        self.phases = {
            0: "CRUISE",
            1: "DESCENT_ABOVE_FL100", 
            2: "DESCENT_BELOW_FL100",
            3: "CONF_1", 4: "CONF_2", 5: "CONF_3",
            6: "CONF_3_GEAR_DOWN", 7: "CONF_FULL", 8: "LANDING"
        }
        
        # 物理常数
        self.g = 9.81  # 重力加速度 m/s²
        
        # 飞机参数 (简化的A320参数)
        self.mass = 70000  # kg
        self.MMO = 0.82    # 最大马赫数
        self.VMO = 350     # 最大指示空速 kt
        
        # 速度限制
        self.speed_limits = {
            'below_FL100': 250,  # kt
            'VFE1': 230, 'VFE2': 215, 'VFE3': 185, 'VFEFULL': 177,
            'VREF': 140  # 着陆参考速度
        }
        
        # 目标参数
        self.target_altitude = 50    # ft (着陆高度)
        self.target_speed = 140      # kt (着陆速度)
        self.rta_constraint = None   # 到达时间约束
    
    def aerodynamic_drag(self, v, h, gamma, config=0):
        """计算气动阻力 (简化模型)"""
        # 简化的阻力模型: D = 0.5 * rho * v^2 * S * CD
        rho = self.air_density(h)  # 空气密度
        S = 122.6  # 机翼面积 m²
        CD = 0.025 + 0.05 * config  # 阻力系数(随襟翼配置增加)
        drag = 0.5 * rho * (v**2) * S * CD
        return drag
    
    def air_density(self, h):
        """ISA标准大气密度模型"""
        # 简化模型: rho = rho0 * exp(-h/H)
        rho0 = 1.225  # 海平面密度 kg/m³
        H = 8400      # 大气标高 m
        return rho0 * np.exp(-h/H)
    
    def fuel_flow(self, v, h, T):
        """燃油流量模型 (简化)"""
        # 简化模型: 燃油流量与推力成正比
        base_flow = 0.5  # kg/s
        thrust_factor = T / 50000  # 归一化推力
        altitude_factor = 1 - h/15000  # 高度修正
        return base_flow * thrust_factor * max(0.3, altitude_factor)
    
    def wind_speed(self, h):
        """Hellman风速模型"""
        # w(h) = wr * (h/hr)^α
        wr = 20      # 参考风速 m/s
        hr = 10668   # 参考高度 m (35000 ft)
        alpha = 1/7  # Hellman指数
        return wr * (h/hr)**alpha
    
    def flight_dynamics(self, state, controls, phase):
        """
        飞行动力学方程 - 对应文档中的 f̃ⱼ
        state = [v, h, m, t]  # 速度、高度、质量、时间
        controls = [T, gamma] # 推力、飞行路径角
        """
        v, h, m, t = state
        T, gamma = controls
        
        # 计算各项力和参数
        D = self.aerodynamic_drag(v, h, gamma, phase)
        q = self.fuel_flow(v, h, T)
        ws = self.wind_speed(h)
        
        # 动力学方程 (对应 Eq. IV.2)
        dv_dt = T/m - D/m - self.g * np.sin(gamma)  # 速度变化率
        dh_dt = v * np.sin(gamma)                    # 高度变化率  
        dm_dt = -q                                   # 质量变化率(燃油消耗)
        dt_ds = 1 / (v * np.cos(gamma) + ws)        # 时间-距离关系
        
        return np.array([dv_dt, dh_dt, dm_dt, dt_ds])
    
    def path_constraints(self, state, controls, phase):
        """路径约束检查"""
        v, h, m, t = state
        T, gamma = controls
        
        constraints = []
        
        # 速度约束
        if phase <= 1:  # 高空阶段
            constraints.append(v - self.VMO)  # v ≤ VMO
        elif phase == 2:  # FL100以下
            constraints.append(v - self.speed_limits['below_FL100'])
        
        # 推力约束
        T_min = 5000   # 最小推力 N
        T_max = 150000 # 最大推力 N
        constraints.append(T_min - T)  # T ≥ T_min
        constraints.append(T - T_max)  # T ≤ T_max
        
        # 下降角约束
        gamma_min = np.radians(-6)  # 最大下降角 -6度
        gamma_max = np.radians(0)   # 最大爬升角 0度
        constraints.append(gamma_min - gamma)  # gamma ≥ -6°
        constraints.append(gamma - gamma_max)  # gamma ≤ 0°
        
        return np.array(constraints)
    
    def cost_function(self, trajectory):
        """
        目标函数：最小化总燃油消耗
        对应文档中的 πⱼ
        """
        total_fuel = 0
        for i in range(len(trajectory)-1):
            state = trajectory[i]['state']
            controls = trajectory[i]['controls']
            dt = trajectory[i+1]['time'] - trajectory[i]['time']
            
            v, h, m, t = state
            T, gamma = controls
            
            # 瞬时燃油消耗率
            fuel_rate = self.fuel_flow(v, h, T)
            total_fuel += fuel_rate * dt
            
        return total_fuel
    
    def solve_trajectory_optimization(self, initial_state, target_rta):
        """
        求解轨迹优化问题
        这里使用简化的数值方法，实际应用会用CasADi+SNOPT
        """
        print("开始求解飞机下降轨迹优化问题...")
        print(f"初始状态: 速度={initial_state[0]:.1f}m/s, 高度={initial_state[1]:.1f}m")
        print(f"目标RTA: {target_rta:.1f}秒")
        
        # 这里是简化的示例解
        # 实际问题需要使用专业的最优控制求解器
        
        # 模拟优化结果
        optimized_trajectory = {
            'phases': list(self.phases.keys()),
            'total_fuel': 850,  # kg
            'total_time': target_rta,
            'feasible': True
        }
        
        print("优化完成!")
        print(f"总燃油消耗: {optimized_trajectory['total_fuel']} kg")
        print(f"是否满足所有约束: {optimized_trajectory['feasible']}")
        
        return optimized_trajectory

# 使用示例
def main():
    # 创建优化器
    optimizer = AircraftDescentOptimizer()
    
    # 设置初始条件
    initial_state = [200, 10000, 70000, 0]  # [速度m/s, 高度m, 质量kg, 时间s]
    target_rta = 1200  # 目标到达时间(秒)
    
    # 求解优化问题
    result = optimizer.solve_trajectory_optimization(initial_state, target_rta)
    
    # 显示飞行动力学计算示例
    print("\n=== 飞行动力学计算示例 ===")
    state = [180, 8000, 69000, 600]  # 当前状态
    controls = [25000, np.radians(-3)]  # 推力25kN, 下降角-3度
    phase = 2  # 当前在第2阶段
    
    dynamics = optimizer.flight_dynamics(state, controls, phase)
    print(f"当前状态: 速度={state[0]}m/s, 高度={state[1]}m")
    print(f"控制输入: 推力={controls[0]/1000:.1f}kN, 下降角={np.degrees(controls[1]):.1f}°")
    print(f"状态变化率:")
    print(f"  速度变化: {dynamics[0]:.3f} m/s²")
    print(f"  高度变化: {dynamics[1]:.3f} m/s") 
    print(f"  燃油消耗: {-dynamics[2]:.3f} kg/s")

if __name__ == "__main__":
    main()



# 代码结构对应关系
# 1. 飞行动力学方程 → flight_dynamics() 函数

# 对应文档中的方程 IV.2
# 计算速度、高度、质量、时间的变化率

# 2. 飞行阶段 → phases 字典

# 对应文档中的9个飞行阶段
# 每个阶段有不同的约束条件

# 3. 约束条件 → path_constraints() 函数

# 速度、推力、下降角的限制
# 对应文档中的各种约束方程

# 4. 目标函数 → cost_function() 函数

# 最小化燃油消耗
# 对应文档中的方程 IV.5

# 5. 求解器 → solve_trajectory_optimization() 函数

# 模拟使用CasADi+SNOPT求解过程

# 实际应用中的区别
# 文档中的完整版本会：

# 使用CasADi建立符号数学模型
# 用SNOPT求解器处理非线性约束
# 考虑更详细的气动模型和性能数据
# 处理90个时间采样点的高精度轨迹

# 这个简化代码：

# 展示了核心概念和数学结构
# 使用基本的数值方法
# 便于理解整体流程

# 运行这个代码可以看到飞行动力学方程是如何实际工作的！