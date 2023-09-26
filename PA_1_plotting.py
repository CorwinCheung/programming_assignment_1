import matplotlib.pyplot as plt
import numpy as np

#timing data from terminal run commands in the Virtual Box
sizes = np.array([16, 32, 64, 128, 256, 512, 1024])
ip_times = np.array([5281, 36888, 396597, 3636799, 35191606, 413184577, 4362901420])
op_times = np.array([2093, 13003, 89391, 886589, 5943904, 48547174, 450969714])

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(sizes, ip_times, marker='o', label='Inner Product Time (ns)', linestyle='-')
plt.plot(sizes, op_times, marker='s', label='Outer Product Time (ns)', linestyle='-.')

# Plot on a log log scale
plt.xscale('log', base=2)
plt.yscale('log', base=10)

plt.xlabel('Matrix Dimension N (Square Matrix N x N)')
plt.ylabel('Run Time (ns)')
plt.title('Run Times for Inner Product and Outer Product Multiplications')
plt.legend()

plt.show()
