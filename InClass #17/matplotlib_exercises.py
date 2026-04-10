import numpy as np
import matplotlib.pyplot as plt



x = np.arange(1, 11)
y = 4 * x**2 + 2

plt.figure(figsize=(8, 5))
plt.plot(
    x,
    y,
    color='blue',
    linestyle='-',
    linewidth=2,
    marker='o',
    markersize=7,
    label=r'$y = 4x^2 + 2$'
)
plt.title('Quadratic Curve: y = 4x² + 2', fontsize=14)
plt.xlabel('X values', fontsize=12)
plt.ylabel('Y values', fontsize=12)
plt.xticks(x)
plt.yticks(np.arange(0, y.max() + 50, 50))
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()



x_sub = np.arange(1, 11)
params = [
    (1, 2),
    (2, 5),
    (3, -4),
    (4, 10)
]

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle('Subplots for y = 4ax² + c', fontsize=16)

for ax, (a, c) in zip(axes.flat, params):
    y_sub = 4 * a * x_sub**2 + c
    ax.plot(
        x_sub,
        y_sub,
        marker='o',
        linewidth=2,
        label=fr'$y = 4({a})x^2 + {c}$'
    )
    ax.set_title(f'a = {a}, c = {c}')
    ax.set_xlabel('X values')
    ax.set_ylabel('Y values')
    ax.set_xticks(x_sub)
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend()

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()



np.random.seed(42)
x_scatter = np.arange(1, 16)
y_scatter = np.random.randint(10, 100, size=15)

plt.figure(figsize=(8, 5))
plt.scatter(
    x_scatter,
    y_scatter,
    color='purple',
    s=80,
    marker='o',
    label='Random data points'
)
plt.title('Scatter Plot Example', fontsize=14)
plt.xlabel('X values', fontsize=12)
plt.ylabel('Y values', fontsize=12)
plt.xticks(x_scatter)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()




sales = np.array([1000, 800, 845, 1250, 1202, 1500, 1347, 750, 1136, 990])
cost = np.array([900, 790, 800, 1000, 1139, 1200, 1290, 800, 1000, 950])
months = np.arange(1, len(sales) + 1)
profit = sales - cost

fig, ax1 = plt.subplots(figsize=(11, 6))


profit_line = ax1.plot(
    months,
    profit,
    linestyle=':',
    color='red',
    linewidth=3,
    marker='o',
    markerfacecolor='red',
    markeredgecolor='red',
    markersize=8,
    label='Monthly Profit'
)
ax1.set_title('Monthly Profit Report', fontsize=14)
ax1.set_xlabel('Month Number', fontsize=12)
ax1.set_ylabel('Profit', fontsize=12)
ax1.set_xticks(months)
ax1.grid(axis='y', linestyle='--', alpha=0.5)


ax2 = ax1.twinx()
sales_bars = ax2.bar(
    months,
    sales,
    color='yellow',
    edgecolor='black',
    alpha=0.7,
    width=0.6,
    label='Monthly Sales'
)
ax2.set_ylabel('Sales', fontsize=12)


for bar in sales_bars:
    height = bar.get_height()
    ax2.text(
        bar.get_x() + bar.get_width() / 2,
        height + 15,
        f'{int(height)}',
        ha='center',
        va='bottom',
        fontsize=9
    )


handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(handles1 + handles2, labels1 + labels2, loc='upper left')

fig.tight_layout()
plt.show()
