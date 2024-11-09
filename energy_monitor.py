import numpy
import psutil
import random
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Simulate Energy Consumption Data
def get_energy_data():
    cpu_usage = psutil.cpu_percent(interval=1)  # CPU usage percentage
    ram_usage = psutil.virtual_memory().percent  # RAM usage percentage
    disk_usage = psutil.disk_usage('/').percent  # Disk usage percentage

    # Calculate a mock "energy consumption" by adding up usage
    energy_consumption = (cpu_usage + ram_usage + disk_usage) / 3  # Just a simple average for demo
    
    return cpu_usage, ram_usage, disk_usage, energy_consumption

# Data storage for live plotting
cpu_data = []
ram_data = []
disk_data = []
energy_data = []
timestamps = []

# Create a plot for the graph
fig, ax = plt.subplots()
ax.set_title('Energy Consumption Over Time')
ax.set_xlabel('Time (seconds)')
ax.set_ylabel('Usage (%)')
line_cpu, = ax.plot([], [], label='CPU Usage', color='r')
line_ram, = ax.plot([], [], label='RAM Usage', color='g')
line_disk, = ax.plot([], [], label='Disk Usage', color='b')
line_energy, = ax.plot([], [], label='Energy Consumption', color='purple')

ax.legend(loc='upper right')

def update_plot(frame):
    timestamp = time.time()  # Get current timestamp for X axis
    
    # Get the latest energy usage data
    cpu, ram, disk, energy = get_energy_data()
    
    # Append the data to our lists
    timestamps.append(timestamp)
    cpu_data.append(cpu)
    ram_data.append(ram)
    disk_data.append(disk)
    energy_data.append(energy)
    
    # Limit the length of the data for better performance (keeping only the last 60 points)
    max_length = 60
    if len(timestamps) > max_length:
        timestamps.pop(0)
        cpu_data.pop(0)
        ram_data.pop(0)
        disk_data.pop(0)
        energy_data.pop(0)
    
    # Update the data for the lines
    line_cpu.set_data(timestamps, cpu_data)
    line_ram.set_data(timestamps, ram_data)
    line_disk.set_data(timestamps, disk_data)
    line_energy.set_data(timestamps, energy_data)

    # Adjust the X axis limits to show only the last 60 seconds
    ax.set_xlim(timestamps[0], timestamps[-1])
    
    return line_cpu, line_ram, line_disk, line_energy

# Animation function to continuously update the graph
ani = FuncAnimation(fig, update_plot, blit=True, interval=1000)

# Show the plot
plt.show()