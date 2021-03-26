import sys
sys.path.append('src')
from dataframe import DataFrame
from linear_regressor import *
sys.path.append('kaggle/titanic')
from parse_line import *

'''
data_types = {
    "PassengerId": int,
    "Survived": int,
    "Pclass": int,
    "Name": str,
    "Sex": str,
    "Age": float,
    "SibSp": int,
    "Parch": int,
    "Ticket": str,
    "Fare": float,
    "Cabin": str,
    "Embarked": str
}

df = DataFrame.from_csv("kaggle/data/dataset_of_knowns.csv", header=True, data_types=data_types, parser=parse_line)

print("Asserting data loading")
assert df.columns == ["PassengerId", "Survived", "Pclass", "Name", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"]

assert df.to_array()[:5] == [[1, 0, 3, '"Braund, Mr. Owen Harris"', "male", 22.0, 1, 0, "A/5 21171", 7.25, None, "S"],
[2, 1, 1, '"Cumings, Mrs. John Bradley (Florence Briggs Thayer)"', "female", 38.0, 1, 0, "PC 17599", 71.2833, "C85", "C"],
[3, 1, 3, '"Heikkinen, Miss. Laina"', "female", 26.0, 0, 0, "STON/O2. 3101282", 7.925, None, "S"],
[4, 1, 1, '"Futrelle, Mrs. Jacques Heath (Lily May Peel)"', "female", 35.0, 1, 0, "113803", 53.1, "C123", "S"],
[5, 0, 3, '"Allen, Mr. William Henry"', "male", 35.0, 0, 0, "373450", 8.05, None, "S"]]
print('PASSED')
'''

data_types = {
    "PassengerId": int,
    "Survived": int,
    "Pclass": int,
    "Name": str,
    "Sex": str,
    "Age": float,
    "SibSp": int,
    "Parch": int,
    "Ticket": str,
    "Fare": float,
    "Cabin": str,
    "Embarked": str
}
df = DataFrame.from_csv("kaggle/data/dataset_of_knowns.csv", header=True, data_types=data_types, parser=parse_line)


df = df.apply('Name', lambda x: x.split(',')[0][1:])
name_index = df.columns.index('Name')
surnames = [name for name in df.data_dict['Name']]
del df.data_dict['Name']
df.data_dict['Surname'] = surnames
df.columns[name_index] = 'Surname'

cabin_types = []
cabin_numbers = []
cabin_index = df.columns.index('Cabin')

for cabin in df.data_dict['Cabin']:
    if cabin == None:
        cabin_types.append(None)
        cabin_numbers.append(None)

    else:
        cabin_types.append(cabin.split(' ')[0][0])

        if cabin.split(' ')[0][1:] != '':
            cabin_numbers.append(int(cabin.split(' ')[0][1:]))
        else:
            cabin_numbers.append(None)

df.data_dict['CabinType'] = cabin_types
df.data_dict['CabinNumber'] = cabin_numbers
df.columns[cabin_index] = 'CabinType'
df.columns.insert(cabin_index + 1, 'CabinNumber')


ticket_type = []
ticket_num = []
ticket_index = df.columns.index('Ticket')

for ticket in df.data_dict['Ticket']:
    splitted_ticket = ticket.split(' ')

    if len(splitted_ticket) > 1:
        if len(splitted_ticket) == 3:
            ticket_type.append(str(splitted_ticket[0]) + str(splitted_ticket[1]))
            ticket_num.append(splitted_ticket[2])
            continue

        ticket_type.append(splitted_ticket[0])
        ticket_num.append(splitted_ticket[1])

    else:
        try:
            int(splitted_ticket[0])
            ticket_type.append(None)
            ticket_num.append(splitted_ticket[0])

        except ValueError:
            ticket_type.append(splitted_ticket[0])
            ticket_num.append(None)

del df.data_dict['Ticket']
df.data_dict['TicketType'] = ticket_type
df.data_dict['TicketNumber'] = ticket_num
df.convert_column_type('TicketNumber', int)
df.columns[ticket_index] = 'TicketType'
df.columns.insert(ticket_index+ 1, 'TicketNumber')

assert df.columns == ["PassengerId", "Survived", "Pclass", "Surname", "Sex", "Age", "SibSp", "Parch", "TicketType", "TicketNumber", "Fare", "CabinType", "CabinNumber", "Embarked"]

assert df.to_array()[:5] == [[1, 0, 3, "Braund", "male", 22.0, 1, 0, "A/5", 21171, 7.25, None, None, "S"],
[2, 1, 1, "Cumings", "female", 38.0, 1, 0, "PC", 17599, 71.2833, "C", 85, "C"],
[3, 1, 3, "Heikkinen", "female", 26.0, 0, 0, "STON/O2.", 3101282, 7.925, None, None, "S"],
[4, 1, 1, "Futrelle", "female", 35.0, 1, 0, None, 113803, 53.1, "C", 123, "S"],
[5, 0, 3, "Allen", "male", 35.0, 0, 0, None, 373450, 8.05, None, None, "S"]]
'''
print(df.group_by("Pclass").aggregate("Survived", "avg").select(["Pclass", "Survived"]).to_array(), "\n")
print(df.group_by("Pclass").aggregate("Survived", "count").select(["Pclass", "Survived"]).to_array(), "\n")

print(df.group_by("Sex").aggregate("Survived", "avg").select(["Sex", "Survived"]).to_array(), "\n")
print(df.group_by("Sex").aggregate("Survived", "count").select(["Sex", "Survived"]).to_array())

print(df.group_by("SibSp").aggregate("Survived", "avg").select(["SibSp", "Survived"]).to_array(), "\n")
print(df.group_by("SibSp").aggregate("Survived", "count").select(["SibSp", "Survived"]).to_array())

print(df.group_by("Parch").aggregate("Survived", "avg").select(["Parch", "Survived"]).to_array(), "\n")
print(df.group_by("Parch").aggregate("Survived", "count").select(["Parch", "Survived"]).to_array())

print(df.group_by("CabinType").aggregate("Survived", "avg").select(["CabinType", "Survived"]).to_array(), "\n")
print(df.group_by("CabinType").aggregate("Survived", "count").select(["CabinType", "Survived"]).to_array())

print(df.group_by("Embarked").aggregate("Survived", "avg").select(["Embarked", "Survived"]).to_array(), "\n")
print(df.group_by("Embarked").aggregate("Survived", "count").select(["Embarked", "Survived"]).to_array())
'''

age_index = df.columns.index("Age")
age_excluding_none = []

for row in df.to_array():
    if row[age_index] != None:
        age_excluding_none.append(row)

df = DataFrame.from_array(age_excluding_none, df.columns)

'''
age_category = df.select(["Age", "Survived"]).where(lambda row: row["Age"] <= 10)
avg = sum([data[1] for data in age_category.to_array()]) / len(age_category.to_array())

age_category = df.select(["Age","Survived"]).where(lambda row: 10 < row["Age"] <= 20)
avg = sum([data[1] for data in age_category.to_array()]) / len(age_category.to_array())

age_category = df.select(["Age","Survived"]).where(lambda row: 20 < row["Age"] <= 30)

age_category = df.select(["Age", "Survived"]).where(lambda row: 30 < row["Age"] <= 40)

age_category = df.select(["Age", "Survived"]).where(lambda row: 40 < row["Age"] <= 50)

age_category = df.select(["Age", "Survived"]).where(lambda row: 50 < row["Age"] <= 60)

age_category = df.select(["Age", "Survived"]).where(lambda row: 60 < row["Age"] <= 70)

age_category = df.select(["Age", "Survived"]).where(lambda row: 70 < row["Age"] <= 80)

avg = sum([data[1] for data in age_category.to_array()]) / len(age_category.to_array())
print(avg, "(", len(age_category.to_array()), ")" )
'''

fare_index = df.columns.index("Fare")
fare_excluding_none = []

for row in df.to_array():
    if row[fare_index] != None:
        fare_excluding_none.append(row)

df = DataFrame.from_array(fare_excluding_none, df.columns)
'''
fare_category = df.select(['Fare', "Survived"]).where(lambda row: row['Fare'] <= 5)

fare_category = df.select(['Fare', "Survived"]).where(lambda row: 5 < row['Fare'] <= 10)

fare_category = df.select(['Fare', "Survived"]).where(lambda row: 10 < row['Fare'] <= 20)

fare_category = df.select(['Fare', "Survived"]).where(lambda row: 20 < row['Fare'] <= 50)

fare_category = df.select(['Fare', "Survived"]).where(lambda row: 50 < row['Fare'] <= 100)

fare_category = df.select(['Fare', "Survived"]).where(lambda row: 100 < row['Fare'] <= 200)

fare_category = df.select(['Fare', "Survived"]).where(lambda row: row['Fare'] > 200)

avg = sum([data[1] for data in fare_category.to_array()]) / len(fare_category.to_array())

print(avg, "(", len(fare_category.to_array()), ")" )
'''

for n in range(len(df.data_dict['Sex'])):
    if df.data_dict['Sex'][n] == "male":
        df.data_dict['Sex'][n] = 0
        continue

    df.data_dict['Sex'][n] = 1

data_types['Sex'] = int

age_without_none = [age for age in df.data_dict['Age'] if age != None]
mean_age = sum(age_without_none)/len(age_without_none)

for n in range(len(df.data_dict['Age'])):
    if df.data_dict['Age'][n] == None:
        df.data_dict['Age'][n] == mean_age


df.columns.insert(df.columns.index('SibSp') + 1 , 'SibSp=0')
df.data_dict['SibSp=0'] = [1 if sibsp == 0 else 0 for sibsp in df.data_dict['SibSp']]
data_types['SibSp=0'] = int

df.columns.insert(df.columns.index('Parch') + 1 , 'Parch=0')
df.data_dict['Parch=0'] = [1 if parch == 0 else 0 for parch in df.data_dict['Parch']]
data_types['Parch=0'] = int
del df.data_dict['Parch']
del df.columns[df.columns.index('Parch')]

df.data_dict['CabinType'] = [['CabinType=' + str(cabin_type)] if cabin_type != '' else ['CabinType=None'] for cabin_type in df.data_dict['CabinType']]
df = df.create_dummy_variables('CabinType')
del df.data_dict['CabinType']

df.data_dict['Embarked'] = [['Embarked=' + str(embarked)] if embarked != '' else ['Embarked=None'] for embarked in df.data_dict['Embarked']]
df = df.create_dummy_variables('Embarked')
del df.data_dict['Embarked']

def get_set_acc(input_set, input_regressor):
    correct_predictions = 0
    list_of_dicts = []
    predictions = []

    for n in range(len(input_set.data_dict['Survived'])):
        data = {}

        for key in input_set.data_dict:
            if key != 'Survived':
                data[key] = input_set.data_dict[key][n]

        list_of_dicts.append(data)

    for dictionary in list_of_dicts:
        prediction = input_regressor.predict(dictionary)

        if prediction >= 0.5:
            predictions.append(1)

        else:
            predictions.append(0)


    for n in range(len(predictions)):
        if predictions[n] == input_set.data_dict['Survived'][n]:
            correct_predictions += 1

    return correct_predictions/len(predictions)

training_set = DataFrame.from_array(df.to_array()[:500], df.columns)
train_regressor = LinearRegressor(training_set.select(['Sex', 'Survived']), 'Survived')

print("(b) Training set", get_set_acc(training_set, train_regressor))
print(train_regressor.coefficients)

testing_set = DataFrame.from_array(df.to_array()[500:], df.columns)
test_regressor = LinearRegressor(testing_set.select(['Sex', 'Survived']), 'Survived')

print("Testing set", get_set_acc(testing_set, test_regressor), "\n")


training_set2 = DataFrame.from_array(df.to_array()[:500], df.columns)
train_regressor2 = LinearRegressor(training_set2.select(['Sex', 'Pclass', 'Survived']), 'Survived')

print("(c) Training set", get_set_acc(training_set2, train_regressor2))
print(train_regressor2.coefficients)

testing_set2 = DataFrame.from_array(df.to_array()[500:], df.columns)
test_regressor2 = LinearRegressor(testing_set2.select(['Sex', 'Pclass', 'Survived']), 'Survived')

print("Testing set", get_set_acc(testing_set2, test_regressor2), "\n")



training_set3 = DataFrame.from_array(df.to_array()[:500], df.columns)
train_regressor3 = LinearRegressor(training_set3.select(['Sex', 'Pclass', 'Fare', 'Age', 'SibSp', 'SibSp=0', 'Parch=0', 'Survived']), 'Survived')

print("(d) Training set", get_set_acc(training_set3, train_regressor3))
print(train_regressor3.coefficients)

testing_set3 = DataFrame.from_array(df.to_array()[500:], df.columns)
test_regressor3 = LinearRegressor(testing_set3.select(['Sex', 'Pclass', 'Fare', 'Age', 'SibSp', 'SibSp=0', 'Parch=0', 'Survived']), 'Survived')

print("Testing set", get_set_acc(testing_set3, test_regressor3), "\n")



training_set4 = DataFrame.from_array(df.to_array()[:500], df.columns)
train_regressor4 = LinearRegressor(training_set4.select(['Sex', 'Pclass', 'Fare', 'Age', 'SibSp', 'SibSp=0', 'Parch=0', 'Embarked=C', 'Embarked=None', 'Embarked=Q', 'Embarked=S', 'Survived']), 'Survived')

print("(e) Training set", get_set_acc(training_set4, train_regressor4))
print(train_regressor4.coefficients)

testing_set4 = DataFrame.from_array(df.to_array()[500:], df.columns)
test_regressor4 = LinearRegressor(testing_set4.select(['Sex', 'Pclass', 'Fare', 'Age', 'SibSp', 'SibSp=0', 'Parch=0', 'Embarked=C', 'Embarked=None', 'Embarked=Q', 'Embarked=S', 'Survived']), 'Survived')

print("Testing set", get_set_acc(testing_set4, test_regressor4), "\n")




training_set5 = DataFrame.from_array(df.to_array()[:500], df.columns)
train_regressor5 = LinearRegressor(training_set5.select(['Sex', 'Pclass', 'Fare', 'Age', 'SibSp', 'SibSp=0', 'Parch=0', 'Embarked=C', 'Embarked=None', 'Embarked=Q', 'Embarked=S', 'CabinType=A', 'CabinType=B', 'CabinType=C', 'CabinType=D', 'CabinType=E', 'CabinType=F', 'CabinType=G', 'CabinType=None', 'Survived']), 'Survived')

print("(f) Training set", get_set_acc(training_set5, train_regressor5))
print(train_regressor5.coefficients)


testing_set5 = DataFrame.from_array(df.to_array()[500:], df.columns)
test_regressor5 = LinearRegressor(testing_set5.select(['Sex', 'Pclass', 'Fare', 'Age', 'SibSp', 'SibSp=0', 'Parch=0', 'Embarked=C', 'Embarked=None', 'Embarked=Q', 'Embarked=S', 'CabinType=A', 'CabinType=B', 'CabinType=C', 'CabinType=D', 'CabinType=E', 'CabinType=F', 'CabinType=G', 'CabinType=None', 'Survived']), 'Survived')


print("Testing set", get_set_acc(testing_set5, test_regressor5), "\n")



training_set6 = DataFrame.from_array(df.to_array()[:500], df.columns)
train_regressor6 = LinearRegressor(training_set5.select(['Sex', 'Pclass', 'Fare', 'Age', 'SibSp', 'SibSp=0', 'Parch=0', 'Embarked=C', 'Embarked=None', 'Embarked=Q', 'Embarked=S', 'CabinType=A', 'CabinType=B', 'CabinType=C', 'CabinType=D', 'CabinType=E', 'CabinType=F', 'CabinType=G', 'CabinType=None', 'CabinType=T', 'Survived']), 'Survived')

print("(f) Training set", get_set_acc(training_set6, train_regressor6))
print(train_regressor6.coefficients)


testing_set5 = DataFrame.from_array(df.to_array()[500:], df.columns)
test_regressor5 = LinearRegressor(testing_set6.select(['Sex', 'Pclass', 'Fare', 'Age', 'SibSp', 'SibSp=0', 'Parch=0', 'Embarked=C', 'Embarked=None', 'Embarked=Q', 'Embarked=S', 'CabinType=A', 'CabinType=B', 'CabinType=C', 'CabinType=D', 'CabinType=E', 'CabinType=F', 'CabinType=G', 'CabinType=None', 'CabinType=T' , 'Survived']), 'Survived')


print("Testing set", get_set_acc(testing_set6, test_regressor6), "\n")