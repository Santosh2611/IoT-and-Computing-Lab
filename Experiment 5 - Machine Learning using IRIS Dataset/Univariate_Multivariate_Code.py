# Load Libraries:-
import pandas # Library for working with data sets
from pandas.plotting import scatter_matrix # Draw a matrix of scatter plots
import matplotlib.pyplot as plt # Collection of command style functions that make matplotlib work like MATLAB

# Load Dataset:-
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length','sepal-width','petal-length','petal-width','class']
dataset = pandas.read_csv(url, names=names) # Read a comma-separated values (CSV) file into DataFrame

print('Dataset Dimensions: ' + str(dataset.shape)) # Return a tuple representing the dimensionality of the DataFrame
print('\nHead of the Data: \n' + str(dataset.head(20))) # Return the first n=20 rows
print('\nData Statistics: \n' + str(dataset.describe)) # Generates descriptive statistics that summarize the central tendency, dispersion and shape of a dataset’s distribution, excluding NaN values.
print('\nClass Distribution: \n' + str(dataset.groupby('class').size())) # Group DataFrame using a mapper or by a Series of columns

dataset.plot(kind='box', layout=(2,2), sharex=False, sharey=False); plt.show() # Make plots of Series or DataFrame
dataset.hist(); plt.show() # Make a histogram of the DataFrame’s columns
scatter_matrix(dataset); plt.show() # Visualize data with scatter plots
