# student_dict = {
#     "student" : ["Angela","James","Lily"],
#     "score" : [56,76,98]
# }

# #how to loop throught the keys of the dictionary 

# # for key,value in student_dict.items():
# #     print(value)


# import pandas as pd

# data = pd.DataFrame(student_dict)

# # print(data)

# #loop throught the dataframe using same method before 

# # for key,value in data.items():
# #     print(value)


# for (index,row ) in data.iterrows():
#     if(row.student == "Angela"):
#         print(row.score)

import pandas as pd

data = pd.read_csv("dataset.csv")

letters = {row['letter']: row['code'] for index, row in data.iterrows()}

name = input("ENter your Name ")
name = name.upper()
result = []
for letter in name:
    result.append(letters[letter])
print(result)

