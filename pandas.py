import pandas
import numpy
 
 
inp = {'Name':['John','Bran','Caret','Joha','Sam'],
   'Marks':[44,48,75,33,99],
   'Roll_num':[1,2,3,4,5]
}
 
#Creating a DataFrame
data_frame = pandas.DataFrame(inp)
print(data_frame.to_string())