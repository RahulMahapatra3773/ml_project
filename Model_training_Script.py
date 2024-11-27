import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
data = pd.read_csv('/content/drive/MyDrive/diabetes_prediction_dataset.csv')

data.head()

data.info()

"""**ENCODING** : (part of preprocessing) we have to convert catagorical(object) data into numerical data for finding correlation and describe."""

data.describe()

"""Describe for columns of object datatype are missing (gender, smoking history)"""

data.shape

"""**ENCODING** :

class -> value

1.  Ordinal ('Male' -> 0 ,  'Female' -> 1)
2.  One not ('Male' -> [1,0],  'Female' -> [0,1]) increases dimension of data, add more features 'Male' and 'Female'.
3.  Map : same as Ordinal just we have to do manual mapping {Dictionary}

Finding all possible values in that object type feature
 : ***'smoking_history'***

---
"""

data["smoking_history"].unique()



data["gender"].unique()



"""Using Map(Dictionary) method:

For encoding Gender:

```
data['gender'] = data['gender'].map({'Male':1,'Female':2, 'Other':3})
```


For Encoding smoking history:

```
data['smoking_history'] = data['smoking_history'].map({'never':1, 'No Info':2, 'current':3, 'former':4, 'ever':5, 'not current':6})
```
"""

data['gender'] = data['gender'].map({'Male':1,'Female':2, 'Other':3})

data['smoking_history'] = data['smoking_history'].map({'never':1, 'No Info':2, 'current':3, 'former':4, 'ever':5, 'not current':6})

data.head()

data.corr()

data.info()

data.isna().sum()

data.describe()

sns.heatmap(data.corr())

"""**Box plot of all features at same time to find outliers**"""

data.plot(kind='box')

"""**Creating Input and Output split**"""

y = data['diabetes']
# droping diabetes column from x because we won't want to include diabetes (that is output label) in input.
data.drop('diabetes', axis=1, inplace=True)
x=data

"""**Test Train Split**"""

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)

from sklearn.linear_model import LogisticRegression

"""**Classification** : Decison Boundary from sigmoid function"""

model = LogisticRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

"""**EVALUATION MATRIX**"""

from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, roc_curve, auc, precision_score, recall_score

"""ACCURACY : how much correct"""

print("Accuracy :", accuracy_score(y_test, y_pred))



"""Can't select on the basis of accuracy

**Confusion Matrix**

 test\pred :        ```Yes                                 No```
* Yes :  True Positive    True Negetive
* No  :  False Positive   True Negetive
"""

confusion_matrix(y_test, y_pred)

"""Actual accuracy"""

f1_score(y_test, y_pred)

from sklearn.ensemble import RandomForestClassifier
rf_model = RandomForestClassifier()
rf_model.fit(x_train, y_train)
importances = rf_model.feature_importances_
indices = np.argsort(importances)[::-1]
features = [f'Feature {i}'for i in range(x.shape[1])]

plt.figure()
plt.title("Feature Importance")
plt.bar(range(x.shape[1]), importances[indices], color="r", align='center')
plt.xticks(range(x.shape[1]), [features[i] for i in indices], rotation=45) # Use features instead of feature
plt.tight_layout()
plt.show()

"""**Homework**

naive bais classifier, all matrices
file (code, output, intrepretation) or this model on web app streamlit
"""

