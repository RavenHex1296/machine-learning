import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
'''
df = pd.DataFrame(
    [['Shortbread', 0.14, 0.14, 0.28, 0.44], 
    ['Shortbread', 0.10, 0.18, 0.28, 0.44], 
    ['Shortbread', 0.12, 0.10, 0.33, 0.45],
    ['Shortbread', 0.10, 0.25, 0.25, 0.40],
    ['Sugar', 0.00, 0.10, 0.40, 0.50],
    ['Sugar', 0.00, 0.20, 0.40, 0.40],
    ['Sugar', 0.02, 0.08, 0.45, 0.45],
    ['Sugar', 0.10, 0.15, 0.35, 0.40],
    ['Sugar', 0.10, 0.08, 0.35, 0.47],
    ['Sugar', 0.00, 0.05, 0.30, 0.65],
    ['Fortune', 0.20, 0.00, 0.40, 0.40],
    ['Fortune', 0.25, 0.10, 0.30, 0.35],
    ['Fortune', 0.22, 0.15, 0.50, 0.13],
    ['Fortune', 0.15, 0.20, 0.35, 0.30],
    ['Fortune', 0.22, 0.00, 0.40, 0.38],
    ['Shortbread', 0.05, 0.12, 0.28, 0.55],
    ['Shortbread', 0.14, 0.27, 0.31, 0.28],
    ['Shortbread', 0.15, 0.23, 0.30, 0.32],
    ['Shortbread', 0.20, 0.10, 0.30, 0.40]],
    columns = ['Cookie Type' ,'Portion Eggs','Portion Butter','Portion Sugar','Portion Flour' ]
    )

def check_classifier_value(knn, df, row_index):
    independent_variables = df[[column for column in df.columns if column != 'Cookie Type']]
    dependent_variable = df['Cookie Type']

    values = independent_variables.iloc[[row_index]].to_numpy().tolist()[0]

    training_df = independent_variables.drop([row_index])
    X = training_df.reset_index(drop=True).to_numpy().tolist()
    testing_df = dependent_variable.drop([row_index])
    Y = testing_df.reset_index(drop=True).to_numpy().tolist()

    predicted_value = knn.fit(X, Y).predict([values])

    if predicted_value == df['Cookie Type'].iloc[[row_index]].to_numpy().tolist()[0]:
        return True

    return False


def get_accuracy(knn, df):
    correct_classifications = 0

    for row_index in range(len(df.to_numpy().tolist())):
        if check_classifier_value(knn, df, row_index):
            correct_classifications += 1

    return correct_classifications / len(df.to_numpy().tolist())

accuracies = []

for k in [n for n in range(1, 19)]:
    knn = KNeighborsClassifier(n_neighbors = k)
    accuracies.append(get_accuracy(knn, df))

plt.style.use("bmh")
plt.plot([k for k in range(1, 19)], accuracies)
plt.xlabel("k")
plt.ylabel("accuracy")
plt.title("Leave One Out Cross Validation")
plt.savefig("Leave-One-Out Cross Validation.png")
'''
