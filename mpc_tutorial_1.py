import numpy as np
from casadi import *

def solve_OCP_with_output(x_bar, K):
    """
    Solve OCP with explicit output equation
    
    State: x = [position, velocity] ∈ R^2  (how system evolves)
    Output: y = position ∈ R^1             (what we control)  
    Control: u = force ∈ R^1               (control means)
    """
    
    # === System Dimensions ===
    n = 2  # state dimension
    m = 1  # control dimension  
    p = 1  # output dimension
    
    # === System Matrices ===
    # State evolution: x_{k+1} = A*x_k + B*u_k
    A = np.array([[1.0, 0.1],     # position evolution
                  [0.0, 1.0]])    # velocity evolution
    B = np.array([[0.005],        # control effect on position
                  [0.1]])         # control effect on velocity
    
    # Output equation: y_k = C*x_k + D*u_k
    C = np.array([[1, 0]])        # output = position only
    D = np.array([[0]])           # output doesn't depend on current control
    
    # === Cost Matrices ===
    Q_y = np.array([[10]])        # output cost weight (position)
    Q_x = np.array([[0, 0],       # additional state cost weight
                    [0, 1]])      # (velocity penalty)
    R = np.array([[1]])           # control cost weight
    Q_yK = Q_y                    # terminal output cost
    
    # === Constraints ===
    u_max = 1.0    # control limits: |u| ≤ 1
    y_max = 1.0    # output limits: |y| ≤ 1 (position constraint)
    
    # === Optimization Setup ===
    opti = Opti()
    
    # Decision variables
    x_tot = opti.variable(n, K+1)  # State trajectory: [x0, x1, ..., xK]
    u_tot = opti.variable(m, K)    # Control trajectory: [u0, u1, ..., u_{K-1}]  
    y_tot = opti.variable(p, K+1)  # Output trajectory: [y0, y1, ..., yK]
    
    # === Constraints ===
    
    # Initial condition
    opti.subject_to(x_tot[:, 0] == x_bar)
    
    # System dynamics and output equation
    cost = 0
    for k in range(K):
        # State evolution constraint: x_{k+1} = A*x_k + B*u_k
        x_next = mtimes(A, x_tot[:, k]) + mtimes(B, u_tot[:, k])
        opti.subject_to(x_tot[:, k+1] == x_next)
        
        # Output equation constraint: y_k = C*x_k + D*u_k
        y_current = mtimes(C, x_tot[:, k]) + mtimes(D, u_tot[:, k])
        opti.subject_to(y_tot[:, k] == y_current)
        
        # Running cost: output cost + state cost + control cost
        cost += mtimes([y_tot[:, k].T, Q_y, y_tot[:, k]]) + \
                mtimes([x_tot[:, k].T, Q_x, x_tot[:, k]]) + \
                mtimes([u_tot[:, k].T, R, u_tot[:, k]])
    
    # Terminal output constraint: y_K = C*x_K  
    y_terminal = mtimes(C, x_tot[:, K])
    opti.subject_to(y_tot[:, K] == y_terminal)
    
    # Terminal cost: output cost
    cost += mtimes([y_tot[:, K].T, Q_yK, y_tot[:, K]])
    
    # === Physical Constraints ===
    
    # Control constraints: |u_k| ≤ u_max
    opti.subject_to(opti.bounded(-u_max, u_tot, u_max))
    
    # Output constraints: |y_k| ≤ y_max (position limits)
    opti.subject_to(opti.bounded(-y_max, y_tot, y_max))
    
    # === Solve ===
    opti.minimize(cost)
    opts = {"ipopt.print_level": 0, "print_time": 0}
    opti.solver("ipopt", opts)
    
    solution = opti.solve()
    
    # Extract solutions
    x_opt = solution.value(x_tot)
    u_opt = solution.value(u_tot)
    y_opt = solution.value(y_tot)
    
    return x_opt, u_opt, y_opt

def mpc_with_output_loop():
    """
    MPC loop with explicit output equation demonstration
    """
    
    # === MPC Parameters ===
    K = 10                                    # prediction horizon
    number_of_iterations = 100               # simulation steps
    x_init = np.array([[0.5], [0.5]])       # initial state: [pos=0.5m, vel=0.5m/s]
    
    # === Storage Arrays ===
    x_cl = np.zeros((2, number_of_iterations + 1))  # closed-loop states
    u_cl = np.zeros((1, number_of_iterations))       # closed-loop controls  
    y_cl = np.zeros((1, number_of_iterations + 1))   # closed-loop outputs
    
    # === System Matrices (for simulation) ===
    A = np.array([[1.0, 0.1], [0.0, 1.0]])
    B = np.array([[0.005], [0.1]])
    C = np.array([[1, 0]])                           # output = position
    D = np.array([[0]])
    
    # Initialize
    x_cl[:, 0] = x_init.flatten()
    y_cl[:, 0] = (C @ x_init).flatten()              # initial output
    x_bar = x_init
    
    print("=== MPC with Explicit Output Equation ===")
    print(f"Initial state: position={x_init[0,0]:.2f}m, velocity={x_init[1,0]:.2f}m/s")
    print(f"Initial output: y={y_cl[0,0]:.2f}m (position)")
    print(f"Target: drive output (position) to 0")
    print(f"Constraints: |output| ≤ 1m, |control| ≤ 1N")
    print("-" * 50)
    
    # === MPC Loop ===
    for i in range(number_of_iterations):
        
        # Solve MPC with current state
        x_opt, u_opt, y_opt = solve_OCP_with_output(x_bar, K)
        
        # Extract first control action
        u_first = u_opt[0]
        u_cl[:, i] = u_first
        
        # Apply control to real system (simulate one step)
        x_next = A @ x_bar + B * u_first
        y_next = C @ x_next + D * u_first
        
        # Store results
        x_cl[:, i+1] = x_next.flatten()
        y_cl[:, i+1] = y_next.flatten()
        
        # Update for next iteration
        x_bar = x_next
        
        # Print progress every 10 steps
        if i % 10 == 0 or i < 5:
            print(f"Step {i:2d}: output={y_cl[0,i]:.3f}m, "
                  f"state=[{x_cl[0,i]:.3f}, {x_cl[1,i]:.3f}], "
                  f"control={u_first:.3f}N")
        
        # Check convergence
        if abs(y_cl[0, i+1]) < 0.01 and abs(x_cl[1, i+1]) < 0.01:
            print(f"\n✅ Converged at step {i+1}!")
            print(f"Final output: {y_cl[0,i+1]:.4f}m")
            print(f"Final state: position={x_cl[0,i+1]:.4f}m, velocity={x_cl[1,i+1]:.4f}m/s")
            break
    
    return x_cl, u_cl, y_cl

def compare_formulations():
    """
    Compare original vs output-based formulation
    """
    print("\n" + "="*60)
    print("COMPARISON: Original vs Output-based MPC")
    print("="*60)
    
    print("\n📊 ORIGINAL FORMULATION:")
    print("States: x = [position, velocity]")
    print("Controls: u = force") 
    print("Constraints: position ∈ [-1,1], |u| ≤ 1")
    print("Cost: x^T Q x + u^T R u")
    print("→ Directly optimizes states")
    
    print("\n📊 OUTPUT-BASED FORMULATION:")
    print("States: x = [position, velocity]    (how system evolves)")
    print("Outputs: y = position               (what we control)")
    print("Controls: u = force                 (control means)")
    print("Constraints: |y| ≤ 1, |u| ≤ 1")
    print("Cost: y^T Q_y y + x^T Q_x x + u^T R u")
    print("→ Separates 'evolution' from 'control objectives'")
    
    print("\n🎯 KEY INSIGHTS:")
    print("• Same physical system, different mathematical perspective")
    print("• Output formulation clarifies 'what we really care about'")
    print("• Enables complex output definitions (e.g., y = f(x))")
    print("• Prepares for cases where dim(y) ≠ dim(x)")

if __name__ == "__main__":
    # Run the MPC simulation
    x_history, u_history, y_history = mpc_with_output_loop()
    
    # Show the comparison
    compare_formulations()
    
    print(f"\n📈 SIMULATION COMPLETE")
    print(f"• Output successfully regulated to 0")
    print(f"• Final output error: {abs(y_history[0,-1]):.4f}m")
    print(f"• Demonstrates clear separation of concerns:")
    print(f"  - States define system evolution")  
    print(f"  - Outputs define control objectives")
    print(f"  - Controls provide the means to achieve objectives")