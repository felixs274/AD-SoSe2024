import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv("data.csv")

# Remove duplicate ListSize values
data = data.drop_duplicates(subset=['ListSize'])

# Group data by ListSize and calculate average operations for each sorting algorithm
averages = data.groupby('ListSize').mean().reset_index()

# Extract data for plotting
list_size = averages['ListSize']
count_sort_ops_avg = averages['countSort_Ops']
heap_sort_ops_avg = averages['heapSort_Ops']
map_sort_ops_avg = averages['mapSort_Ops']

# Plotting Operations
plt.figure(figsize=(10, 6))

plt.plot(list_size, count_sort_ops_avg, label='Count Sort Ops')
plt.plot(list_size, heap_sort_ops_avg, label='Heap Sort Ops')
plt.plot(list_size, map_sort_ops_avg, label='Map Sort Ops')

plt.xlabel('List Size')
plt.ylabel('Average Operations')
plt.title('Average Operations of Sorting Algorithms by List Size')
plt.legend()
plt.grid(True)

plt.savefig('average_sorting_algorithms_operations.png')  # Save the plot to a file

# Plotting Time
plt.figure(figsize=(10, 6))

count_sort_time_avg = averages['countSort_Time']
heap_sort_time_avg = averages['heapSort_Time']
map_sort_time_avg = averages['mapSort_Time']

plt.plot(list_size, count_sort_time_avg, label='Count Sort Time')
plt.plot(list_size, heap_sort_time_avg, label='Heap Sort Time')
plt.plot(list_size, map_sort_time_avg, label='Map Sort Time')

plt.xlabel('List Size')
plt.ylabel('Average Time')
plt.title('Average Time of Sorting Algorithms by List Size')
plt.legend()
plt.grid(True)

plt.savefig('average_sorting_algorithms.png')  # Save the plot to a file

plt.close()  # Close the plot to release resources
