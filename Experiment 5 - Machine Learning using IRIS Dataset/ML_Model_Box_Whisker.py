import matplotlib.pyplot as plt # Collection of command style functions that make matplotlib work like MATLAB
import pandas # Library for working with data sets
from pandas.plotting import scatter_matrix # Draw a matrix of scatter plots
from sklearn import model_selection # Split arrays or matrices into random train and test subsets

# Metrics for Classification Technique:-
from sklearn.metrics import accuracy_score # Accuracy classification score
from sklearn.metrics import classification_report # Build a text report showing the main classification metrics
from sklearn.metrics import confusion_matrix # Compute confusion matrix to evaluate the accuracy of a classification

# Model Building Libraries:-
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA # Linear Discriminant Analysis
from sklearn.linear_model import LogisticRegression # Logistic Regression (aka logit, MaxEnt) classifier
from sklearn.naive_bayes import GaussianNB # Gaussian Naive Bayes (GaussianNB)
from sklearn.neighbors import KNeighborsClassifier # Classifier implementing the k-nearest neighbors vote
from sklearn.tree import DecisionTreeClassifier # A decision tree classifier
from sklearn.svm import SVC # C-Support Vector Classification

 # Load Dataset:-
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length','sepal-width','petal-length','petal-width','class']
dataset = pandas.read_csv(url, names=names) # Read a comma-separated values (CSV) file into DataFrame

# Create training and validation datasets:-
array = dataset.values # Return a NumPy representation of the DataFrame
X = array[:,0:4] # Data - Assume Independent Variable
Y = array[:,4] # Target - Assume Dependent Variable
validation_size=0.20
seed = 7

X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y,
                                                                                test_size=validation_size,
                                                                                random_state=seed) # Controls the shuffling applied to the data before applying the split

models = results = names = []
scoring = 'accuracy' # Set the scoring criteria

# Build all the models:-
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(kernel='linear', random_state=0)))
models.append(('LDA', LDA(n_components=1)))

# Evaluate Each Model:-
for name, model in models:
    kfold = model_selection.KFold(n_splits=10, random_state=seed, shuffle=True) # Provides train/test indices to split data into train/test sets
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring) # Evaluate a score by cross-validation
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f(%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)

# Plot Model Results:-
figure = plt.figure() # Create a new figure, or activate an existing figure
figure.suptitle('Algorithm Comparison') # Add a centered suptitle to the figure
algPlot = figure.add_subplot(1,1,1) # Add an Axes to the current figure or retrieve an existing Axes
plt.boxplot(results) # Make a box and whisker plot
algPlot.set_xticklabels(names) # Set the xaxis' labels with list of string labels
plt.show() # Display all open figures

# Linear Discriminant Analysis:-
print("\nLinear Discriminant Analysis Classifier:\n")
LDA = LDA(n_components=1) # Number of components (< n_classes - 1) for dimensionality reduction
LDA.fit(X_train, Y_train) # Fit LDA model according to the given training data and parameters
predictions = LDA.predict(X_validation) # Predict class labels for samples in X
print(accuracy_score(Y_validation, predictions))
print(classification_report(Y_validation, predictions))

# Logistic Regression Prediction:-
print("\nLogistic Regression Classifier:\n")
LR = LogisticRegression(solver='liblinear', multi_class='ovr') # Algorithm to use in the optimization problem; A binary problem is fit for each label
LR.fit(X_train, Y_train) # Fit the model according to the given training data
predictions = LR.predict(X_validation) # Predict class labels for samples in X
print(accuracy_score(Y_validation, predictions))
print(classification_report(Y_validation, predictions))

# KNN Prediction:-
print("\nK-Neighbors Classifier:\n")
knn = KNeighborsClassifier() # Classifier implementing the k-nearest neighbors vote
knn.fit(X_train, Y_train) # Fit the k-nearest neighbors classifier from the training dataset
predictions = knn.predict(X_validation) # Predict class labels for samples in X
print(accuracy_score(Y_validation, predictions))
print(classification_report(Y_validation, predictions))

# Decision Tree Classifier Prediction:-
print("\nDecision Tree Classifier:\n")
DT = DecisionTreeClassifier() # A decision tree classifier
DT.fit(X_train, Y_train) # Perform training
predictions = DT.predict(X_validation) # Predict class labels for samples in X
print(accuracy_score(Y_validation, predictions))
print(classification_report(Y_validation, predictions))

# Naive Bayes Classifier Prediction:-
print("\nNaive Bayes Classifier:\n")
NB = GaussianNB() # Gaussian Naive Bayes (GaussianNB)
NB.fit(X_train, Y_train) # Fit Gaussian Naive Bayes according to X, y
predictions = NB.predict(X_validation) # Predict class labels for samples in X
print(accuracy_score(Y_validation, predictions))
print(classification_report(Y_validation, predictions))

# C-Support Vector Classification Prediction:-
print("\nSupport Vector Machine (SVM) Classifier:\n")
SVM = SVC(kernel='linear', random_state=0) # C-Support Vector Classification
SVM.fit(X_train, Y_train) # Fit the SVM model according to the given training data
predictions = SVM.predict(X_validation) # Predict class labels for samples in X
print(accuracy_score(Y_validation, predictions))
print(classification_report(Y_validation, predictions))
