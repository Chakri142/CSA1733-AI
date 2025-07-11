from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_text

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Train decision tree
clf = DecisionTreeClassifier()
clf.fit(X, y)

# Display the tree rules
tree_rules = export_text(clf, feature_names=iris.feature_names)
print(tree_rules)
