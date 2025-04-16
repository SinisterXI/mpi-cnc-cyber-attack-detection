import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.metrics import confusion_matrix
from mpl_toolkits.mplot3d import Axes3D
import random

# Function to plot Confusion Matrix
def plot_confusion_matrix(true_labels, predicted_labels):
    cm = confusion_matrix(true_labels, predicted_labels)
    plt.figure(figsize=(6, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Normal', 'Anomaly'], yticklabels=['Normal', 'Anomaly'])
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.title('Confusion Matrix')
    plt.show()

# Function to plot Feature Distribution (Normal vs Anomalous)
def plot_feature_distribution(data_points):
    spindle_speeds = [point['spindle_speed'] for point in data_points]
    feed_rates = [point['feed_rate'] for point in data_points]
    
    # Create subplots for spindle speed and feed rate
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    axes[0].hist(spindle_speeds, bins=20, color='blue', alpha=0.7)
    axes[0].set_title('Spindle Speed Distribution')
    axes[0].set_xlabel('Spindle Speed')
    axes[0].set_ylabel('Frequency')
    
    axes[1].hist(feed_rates, bins=20, color='green', alpha=0.7)
    axes[1].set_title('Feed Rate Distribution')
    axes[1].set_xlabel('Feed Rate')
    axes[1].set_ylabel('Frequency')
    
    plt.tight_layout()
    plt.show()

# Function to plot Tool Path Visualization (2D & 3D)
def plot_tool_path(data_points):
    x = [point['coordinates'][0] for point in data_points]
    y = [point['coordinates'][1] for point in data_points]
    z = [point['coordinates'][2] for point in data_points]
    
    fig = plt.figure(figsize=(10, 8))
    
    # 2D Plot (X vs Y coordinates)
    plt.subplot(121)
    plt.scatter(x, y, c='blue', label='Normal Data')
    plt.title('Tool Path (XY Coordinates)')
    plt.xlabel('X')
    plt.ylabel('Y')
    
    # 3D Plot (X vs Y vs Z coordinates)
    ax = plt.subplot(122, projection='3d')
    ax.scatter(x, y, z, c='red', label='Normal Data')
    ax.set_title('Tool Path (XYZ Coordinates)')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    plt.tight_layout()
    plt.show()

# Function to plot Feature Correlation
def plot_feature_correlation(data_points):
    # Convert data_points to a Pandas DataFrame
    df = pd.DataFrame([{
        'spindle_speed': point['spindle_speed'],
        'feed_rate': point['feed_rate'],
        'coordinates_x': point['coordinates'][0],
        'coordinates_y': point['coordinates'][1],
        'coordinates_z': point['coordinates'][2]
    } for point in data_points])
    
    # Calculate the correlation matrix
    corr = df.corr()
    
    # Plot the heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=1, square=True)
    plt.title('Feature Correlation Matrix')
    plt.show()

# Function to plot Anomalies Detected Over Time
def plot_anomalies_over_time(time_series, anomaly_labels):
    plt.figure(figsize=(10, 6))
    
    # Plot the time series data
    plt.plot(time_series, label='Data', color='blue')
    
    # Highlight anomalies
    anomalies = [i for i, label in enumerate(anomaly_labels) if label == 1]
    plt.scatter(anomalies, [time_series[i] for i in anomalies], color='red', label='Anomalies')
    
    plt.title('Anomalies Detected Over Time')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()
    plt.show()

# Function to visualize normal data and anomalies (Scatter plot of X vs Y coordinates)
def visualize_data(runtime_data, anomalies):
    plt.scatter([data['coordinates'][0] for data in runtime_data],
                [data['coordinates'][1] for data in runtime_data], c='blue', label='Normal')

    plt.scatter([a['coordinates'][0] for a in anomalies],
                [a['coordinates'][1] for a in anomalies], c='red', label='Anomalies')

    # Labeling the axes
    plt.xlabel('X Coordinates')  # Label for the x-axis
    plt.ylabel('Y Coordinates')  # Label for the y-axis
    
    # Add title and legend
    plt.title('CNC Machine Anomaly Detection')
    plt.legend()

    # Show the plot
    plt.show()

# Example usage of all visualizations
if __name__ == "__main__":
    # Example true and predicted labels for confusion matrix
    true_labels = [0, 1, 0, 0, 1]  # True labels
    predicted_labels = [0, 1, 0, 0, 1]  # Predicted labels (output from anomaly detection system)

    # Plot Confusion Matrix
    plot_confusion_matrix(true_labels, predicted_labels)
    
    # Example data for feature distribution visualization
    data_points = [
        {'spindle_speed': 3000, 'feed_rate': 500, 'coordinates': (10, 20, 30)},
        {'spindle_speed': 6000, 'feed_rate': 20, 'coordinates': (50, 60, 70)},
        {'spindle_speed': 2500, 'feed_rate': 400, 'coordinates': (30, 40, 50)},
        {'spindle_speed': 4000, 'feed_rate': 600, 'coordinates': (70, 80, 90)},
        {'spindle_speed': 5200, 'feed_rate': 50, 'coordinates': (90, 100, 110)}
    ]

    # Plot Feature Distribution
    plot_feature_distribution(data_points)
    
    # Tool Path Visualization (2D & 3D)
    plot_tool_path(data_points)
    
    # Feature Correlation Plot
    plot_feature_correlation(data_points)
    
    # Anomaly detection over time (example data)
    time_series = [100, 102, 105, 107, 110, 120, 130, 140, 135, 125]
    anomaly_labels = [0, 0, 0, 0, 0, 1, 1, 1, 0, 0]  # Detected anomalies

    # Plot Anomalies Over Time
    plot_anomalies_over_time(time_series, anomaly_labels)
    
    # Example runtime data and anomalies for scatter plot
    runtime_data = [{'coordinates': (random.uniform(0, 100), random.uniform(0, 100))} for _ in range(50)]
    anomalies = [{'coordinates': (random.uniform(0, 100), random.uniform(0, 100))} for _ in range(5)]
    
    # Visualize normal data and anomalies
    visualize_data(runtime_data, anomalies)

