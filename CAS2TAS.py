#!/usr/bin/env python3
"""
空速类型转换关系详解
IAS、CAS、EAS、TAS之间的转换不需要额外数据，只需要大气参数
"""

import numpy as np
import matplotlib.pyplot as plt

def demonstrate_airspeed_conversions():
    """演示空速转换的原理和计算"""
    
    print("✈️ 空速类型转换关系说明")
    print("=" * 60)
    
    print("📚 空速类型定义:")
    print("IAS (Indicated Airspeed)  - 指示空速：飞行员从仪表读取的原始速度")
    print("CAS (Calibrated Airspeed) - 校正空速：修正了仪表误差的IAS")
    print("EAS (Equivalent Airspeed) - 等效空速：修正了压缩性误差的CAS")
    print("TAS (True Airspeed)       - 真空速：飞机相对于空气的实际速度")
    
    print(f"\n🔄 转换链条:")
    print("IAS → CAS → EAS → TAS")
    print("     ↑      ↑      ↑")
    print("  仪表修正  压缩性  密度修正")
    
    print(f"\n🧮 转换公式:")
    
    print("\n1️⃣ IAS → CAS:")
    print("   CAS = IAS + 仪表修正(ΔVic)")
    print("   ΔVic = f(空速, 迎角, 机型) - 通常很小")
    print("   在A320-232中：CAS ≈ IAS (现代飞机仪表精度高)")
    
    print("\n2️⃣ CAS → EAS:")
    print("   EAS = CAS × √(1 + CAS²/4a²)")  # 简化的压缩性修正
    print("   a = 当地声速")
    print("   在亚音速（CAS < 300kt）：EAS ≈ CAS")
    
    print("\n3️⃣ EAS → TAS:")
    print("   TAS = EAS / √(ρ/ρ₀)")
    print("   TAS = EAS / √σ")
    print("   σ = 密度比 = ρ/ρ₀")
    
    print("\n4️⃣ 简化的直接转换 (低速情况):")
    print("   TAS ≈ CAS / √σ")
    print("   TAS ≈ IAS / √σ  (当仪表误差很小时)")

def calculate_atmosphere_parameters(altitude_ft):
    """计算大气参数 - 这是转换的关键"""
    
    print(f"\n🌍 大气参数计算 (高度: {altitude_ft:,} ft)")
    print("-" * 40)
    
    alt_m = altitude_ft * 0.3048
    
    if alt_m <= 11000:  # 对流层
        temp = 288.15 * (1 - 0.0065 * alt_m / 288.15)
        pressure_ratio = (temp / 288.15) ** 5.256
        density_ratio = (temp / 288.15) ** 4.256
        print(f"对流层计算:")
    else:  # 平流层
        temp = 216.65
        temp_11km = 288.15 * (1 - 0.0065 * 11000 / 288.15)
        pressure_ratio_11km = (temp_11km / 288.15) ** 5.256
        density_ratio_11km = (temp_11km / 288.15) ** 4.256
        
        pressure_ratio = pressure_ratio_11km * np.exp(-(alt_m - 11000) / 6341.62)
        density_ratio = density_ratio_11km * np.exp(-(alt_m - 11000) / 6341.62)
        print(f"平流层计算:")
    
    sound_speed = np.sqrt(1.4 * 287.053 * temp)
    
    print(f"   温度: {temp:.1f} K ({temp-273.15:.1f}°C)")
    print(f"   密度比 σ: {density_ratio:.4f}")
    print(f"   压力比: {pressure_ratio:.4f}")
    print(f"   声速: {sound_speed:.1f} m/s")
    
    return {
        'temperature': temp,
        'density_ratio': density_ratio,
        'pressure_ratio': pressure_ratio,
        'sound_speed': sound_speed
    }

def conversion_example():
    """具体的转换示例"""
    
    print(f"\n📋 转换示例：300 kt CAS 在不同高度")
    print("=" * 50)
    
    cas_kt = 300  # 校正空速 300 kt
    altitudes = [0, 10000, 20000, 30000, 35000, 40000]
    
    print(f"{'高度(ft)':<10} {'密度比':<8} {'CAS(kt)':<8} {'TAS(kt)':<8} {'比值':<8}")
    print("-" * 50)
    
    for alt in altitudes:
        # 计算大气参数
        alt_m = alt * 0.3048
        
        if alt_m <= 11000:
            temp = 288.15 * (1 - 0.0065 * alt_m / 288.15)
            density_ratio = (temp / 288.15) ** 4.256
        else:
            temp = 216.65
            temp_11km = 288.15 * (1 - 0.0065 * 11000 / 288.15)
            density_ratio_11km = (temp_11km / 288.15) ** 4.256
            density_ratio = density_ratio_11km * np.exp(-(alt_m - 11000) / 6341.62)
        
        # CAS → TAS 转换
        tas_kt = cas_kt / np.sqrt(density_ratio)
        ratio = tas_kt / cas_kt
        
        print(f"{alt:<10} {density_ratio:<8.4f} {cas_kt:<8} {tas_kt:<8.0f} {ratio:<8.2f}")

def create_conversion_chart():
    """创建转换关系图表"""
    
    print(f"\n📊 创建CAS-TAS转换关系图...")
    
    # 高度范围
    altitudes = np.linspace(0, 41000, 100)
    
    # 不同CAS值
    cas_values = [200, 250, 300, 350]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # 左图：TAS vs 高度 (不同CAS)
    for cas in cas_values:
        tas_values = []
        
        for alt in altitudes:
            alt_m = alt * 0.3048
            
            if alt_m <= 11000:
                temp = 288.15 * (1 - 0.0065 * alt_m / 288.15)
                density_ratio = (temp / 288.15) ** 4.256
            else:
                temp = 216.65
                temp_11km = 288.15 * (1 - 0.0065 * 11000 / 288.15)
                density_ratio_11km = (temp_11km / 288.15) ** 4.256
                density_ratio = density_ratio_11km * np.exp(-(alt_m - 11000) / 6341.62)
            
            tas = cas / np.sqrt(density_ratio)
            tas_values.append(tas)
        
        ax1.plot(tas_values, altitudes, label=f'{cas} kt CAS', linewidth=2)
        ax1.axvline(x=cas, color='gray', linestyle=':', alpha=0.5)
    
    ax1.set_xlabel('True Airspeed (kt)', fontsize=12)
    ax1.set_ylabel('Altitude (ft)', fontsize=12)
    ax1.set_title('CAS to TAS Conversion\nvs Altitude', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    ax1.set_xlim(150, 600)
    
    # 右图：密度比 vs 高度
    density_ratios = []
    for alt in altitudes:
        alt_m = alt * 0.3048
        
        if alt_m <= 11000:
            temp = 288.15 * (1 - 0.0065 * alt_m / 288.15)
            density_ratio = (temp / 288.15) ** 4.256
        else:
            temp = 216.65
            temp_11km = 288.15 * (1 - 0.0065 * 11000 / 288.15)
            density_ratio_11km = (temp_11km / 288.15) ** 4.256
            density_ratio = density_ratio_11km * np.exp(-(alt_m - 11000) / 6341.62)
        
        density_ratios.append(density_ratio)
    
    ax2.plot(density_ratios, altitudes, 'r-', linewidth=3, label='Density Ratio (σ)')
    ax2.axvline(x=1.0, color='black', linestyle='-', alpha=0.5, label='Sea Level')
    ax2.axhline(y=11000*3.28084, color='blue', linestyle='--', alpha=0.5, label='Tropopause')
    
    ax2.set_xlabel('Density Ratio (ρ/ρ₀)', fontsize=12)
    ax2.set_ylabel('Altitude (ft)', fontsize=12) 
    ax2.set_title('Atmospheric Density Ratio\nvs Altitude', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    ax2.set_xlim(0, 1.1)
    
    plt.tight_layout()
    plt.savefig('CAS_TAS_Conversion_Chart.png', dpi=300, bbox_inches='tight')
    print("✅ 转换关系图已保存: CAS_TAS_Conversion_Chart.png")
    plt.show()

def answer_key_question():
    """回答关键问题"""
    
    print(f"\n❓ 回答您的关键问题:")
    print("=" * 40)
    
    print("🔍 问题：IAS和TAS的换算是否需要IAS数据？")
    print("\n💡 答案：不需要！")
    
    print(f"\n📋 原因说明:")
    print("1️⃣ IAS ≈ CAS (现代飞机仪表精度高)")
    print("2️⃣ CAS → TAS 只需要大气密度比")
    print("3️⃣ 密度比只依赖于高度 (标准大气)")
    print("4️⃣ 转换公式：TAS = CAS / √(ρ/ρ₀)")
    
    print(f"\n🎯 所需数据:")
    print("✅ 高度 (altitude)")
    print("✅ CAS值 (或近似的IAS值)")
    print("✅ 标准大气模型 (ISA)")
    print("❌ 不需要额外的IAS数据库")
    
    print(f"\n🔧 计算过程:")
    print("输入：高度 + CAS")
    print("  ↓")
    print("计算：大气密度比 σ = f(高度)")
    print("  ↓") 
    print("输出：TAS = CAS / √σ")
    
    print(f"\n✨ 结论:")
    print("IAS-TAS转换是纯数学计算，只需要物理公式和标准大气模型，")
    print("不需要查表或额外的IAS数据！")

def main():
    """主函数"""
    
    print("🛩️ 空速类型转换关系详解")
    print("=" * 60)
    
    # 1. 基本概念解释
    demonstrate_airspeed_conversions()
    
    # 2. 大气参数示例
    calculate_atmosphere_parameters(35000)
    
    # 3. 转换示例
    conversion_example()
    
    # 4. 创建图表
    create_conversion_chart()
    
    # 5. 回答关键问题
    answer_key_question()
    
    print(f"\n🎉 空速转换原理说明完成！")

if __name__ == "__main__":
    main()