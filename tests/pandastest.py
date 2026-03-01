import pandas as pd
import numpy as np

dict1={
    "name":['Anand','Payal','Palak'],
    "marks":[92,32,43],
    "city":['Sambalpur','Padampur','Nuapada']
}

df=pd.DataFrame(dict1)
print(df)