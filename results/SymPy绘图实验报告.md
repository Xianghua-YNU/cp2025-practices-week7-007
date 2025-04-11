# SymPy 绘图实验报告

## 一、实验信息

- 小组名称：cp007
- 成员：马翔宇、涂若晗、杨睿、雷翊烜
- 实验日期：xxx

---

## 二、实验目的

- 熟悉SymPy的plot、plot_implicit、和plot3d_parametric_surface函数；
- 掌握曲线、隐函数和参数曲面的绘制方法。

---

## 三、实验内容与方法

分别说明三个问题的具体绘图方法和使用的函数接口。
##### problem1：基本函数绘图
方法：使用 plot 函数直接绘制显式函数 cos(tan(πx))，定义符号变量 x，设置区间 x ∈ [-1, 1]，添加坐标轴标签和标题。

接口：plot(expr, (x, -1, 1), xlabel='x', ylabel='y', title='...')


##### problem2：隐函数绘图
方法：使用 plot_implicit 绘制隐式方程 e^y + cos(x)/x + y = 0，将 x 区间分为 [-a, -b] 和 [b, a] 避开零点，设置 points=500 提高平滑度。

接口：plot_implicit(expr, (x, x_min, x_max), (y, y_min, y_max), points=500, ...)


##### problem3：参数曲面绘图
方法：使用 plot3d_parametric_surface 定义参数方程 x=exp(-s)cos(t), y=exp(-s)sin(t), z=t，设置 s ∈ [0, 8] 和 t ∈ [0, 5π]，添加三维标签和标题。

接口：plot3d_parametric_surface(x, y, z, (s, 0, 8), (t, 0, 5π), xlabel='x', ..., title='...')

---

## 四、实验结果与分析

### 问题1: 函数曲线 $\cos(\tan(\pi x))$ 绘制结果

![Figure_1](https://github.com/user-attachments/assets/f022d41f-ba25-446c-a13d-47d538057956)

周期性震荡：

tan(πx) 的周期为 1，导致 cos(tan(πx)) 在 x 轴上呈现周期性震荡。

当 x 接近 ±0.5 时，tan(πx) 发散（趋向 ±∞），导致 cos(tan(πx)) 在 x=±0.5 附近剧烈震荡。

奇点与断裂：

在 x=±0.5 处，tan(πx) 无定义，图像会出现垂直渐近线，导致曲线在此处断裂。

SymPy 的 plot 函数会自动跳过无效区域，但靠近 x=±0.5 时仍会显示密集震荡。

对称性：

由于 cos(tan(-πx)) = cos(-tan(πx)) = cos(tan(πx))，图像关于 y 轴对称。

### 问题2: 隐函数曲线 $e^y + \frac{\cos x}{x} + y = 0$ 绘制结果

![Figure_2](https://github.com/user-attachments/assets/ac6ab86a-d744-4e3e-bd54-18a91d5722a0)

定义域限制：

x ≠ 0，绘图需分左右两段（如 x ∈ [-5, -0.1] 和 x ∈ [0.1, 5]）。

当 x → 0⁻ 时，cos(x)/x → -∞，方程需通过 e^y + y 平衡，导致 y → -∞。

当 x → 0⁺ 时，cos(x)/x → +∞，方程无实数解（左侧始终为正）。

曲线形态：

左半部分 (x < 0)：

当 x 远离 0（如 x < -1），cos(x)/x 幅值较小，方程近似 e^y + y ≈ 0，解在 y ≈ -0.57 附近。

当 x → -∞ 时，cos(x)/x → 0，曲线趋近于 y ≈ -0.57 的水平线。

右半部分 (x > 0)：

cos(x)/x 在 x > 0 时幅值较小且正，但 e^y + y > 0 对所有实数 y，因此右半平面无解。

### 问题3: 参数曲面绘制结果

![Figure_3](https://github.com/user-attachments/assets/68ccfb52-e816-409a-8ef2-4f38ec8c98ee)

螺旋衰减结构：

参数 s 的影响：exp(-s) 随 s 增大指数衰减，导致 x 和 y 的幅值逐渐缩小，形成向 z 轴收缩的螺旋。

参数 t 的影响：t 从 0 到 5π 线性增长，使螺旋沿 z 轴延伸，共绕 z 轴旋转 2.5 圈。

几何特性：

初始状态 (s=0)：螺旋半径为 1（exp(0)=1），随着 s 增大，半径按 exp(-s) 衰减。

渐进行为：当 s → 8 时，x 和 y 趋近于 0，曲线收缩到 z 轴附近，形成“螺旋锥形”。

视觉表现：

曲面呈现为围绕 z 轴的螺旋带，从底部（z=0）向外扩展，向上逐渐变细。

---

## 五、实验总结与讨论

- 通过本实验你掌握了哪些绘图技巧？
  
    掌握了画二维函数、隐函数和三维函数图像的方法
- 实验中你遇到了哪些问题？如何解决？
  
  函数使用格式不熟悉，上网查询得到
- 你对SymPy的绘图功能有什么建议或意见？

---

## 六、参考文献

- SymPy官方文档：https://docs.sympy.org/latest/modules/plotting.html
