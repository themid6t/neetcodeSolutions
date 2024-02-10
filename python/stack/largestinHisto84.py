def largestRectangleArea(heights: list[int]) -> int:
    pass

from matplotlib import pyplot as plt
def plot_histogram(heights):
    # Plot the histogram
    plt.bar(range(len(heights)), heights, width=1, edgecolor='black')
    
    # Add labels and title
    plt.xlabel('Height')
    plt.ylabel('Frequency')
    plt.title('Height Histogram')
    
    # Display the plot
    plt.grid(True)
    plt.show()

heights = [2,1,5,6,2,3]
plot_histogram(heights)
print(largestRectangleArea(heights))