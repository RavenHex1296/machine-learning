import sys
sys.path.append('src')
from dataframe import DataFrame
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
'''
print(df.group_by("Embarked").aggregate("Survived", "avg").select(["Embarked", "Survived"]).to_array(), "\n")
print(df.group_by("Embarked").aggregate("Survived", "count").select(["Embarked", "Survived"]).to_array())

