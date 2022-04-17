import random

import numpy as np

from calculate_gg_tries import calculate_gg_tries
import matplotlib.pyplot as plt

# Alpha-Beta-Gama Gate Size 164
# Delta Gate Size 128
# Epsilon Gate Size 99
# Zeta Gate Size 111
# Kappa Gate Size 120
# Lambda Gate Size 45
# Hades Gate Size 45
# Kuiper Gate Size 100

gate_size = 111  # Galaxy gate part count
gate_part_count_which_already_have = 0  # Galaxy gate parts you already have

show_charts = True

# Probability Ratios
ratios = {
    "ammo": .67,
    "xenomit": .12,
    "fix_coupon": .03,
    "gate_part": .13,
    "nano": .04,
    "file": .01
}

random.seed(42)

print("When ship nano body is not full")
result1 = calculate_gg_tries(gate_size, ratios, gate_part_count_which_already_have, show_charts)
print("==========================================")
ratios["gate_part"] /= 1 - ratios["nano"]
print("When ship nano body is full")
result2 = calculate_gg_tries(gate_size, ratios, gate_part_count_which_already_have, show_charts)
if show_charts:
    width = 0.40  # the width of the bars
    labels = ["x2", "x3", "x4", "x5", "x6"]
    x = np.arange(len(labels))  # the label locations
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, result1, width, label='Nano body is not full')
    rects2 = ax.bar(x + width / 2, result2, width, label='Nano body is full')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('GG Energy')
    ax.set_xlabel("Multiplier")
    ax.set_xticks(x, labels)
    ax.set_title("Multiplier and GG Energy")
    ax.legend()
    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    fig.tight_layout()
    plt.show()
