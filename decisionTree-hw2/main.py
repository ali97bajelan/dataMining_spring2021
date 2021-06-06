import pandas
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, plot_roc_curve
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


def classifier(algorithm, data):
    columns = data.columns.tolist()
    x_data = data.drop(labels=columns[-1], axis=1)
    y_data = data.drop(labels=columns[:-1], axis=1)
    X_train, X_test, y_train, y_test = train_test_split(x_data, y_data,test_size=0.15)
    model = algorithm(criterion='entropy')
    model.fit(X=X_train, y=y_train.values.ravel())
    y_pred = model.predict(X=X_test)
    confusion = confusion_matrix(y_true=y_test, y_pred=y_pred)
    accuracy = (confusion[0][0] + confusion[1][1]) / \
        (sum(confusion[0])+sum(confusion[1]))
        
    print("***\t", algorithm.__name__, "Model\t***")
    print("confusion matrix :\n", confusion)
    print("Accuracy is :", round(accuracy*100, 1), '%\n')
    roc_curve = plot_roc_curve(model, X_test, y_test)
    plt.show()


data = pandas.read_csv('diabetes.csv')
algorithm = [DecisionTreeClassifier, RandomForestClassifier]

for i in algorithm:
    classifier(i, data)
