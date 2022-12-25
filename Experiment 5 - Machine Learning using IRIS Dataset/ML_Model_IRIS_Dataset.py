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
