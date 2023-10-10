'''
建成区面积生成脚本

'''
    

import pandas as pd
import numpy as np
year0=1990
year1=2023
years=list(range(year0,year1))
years=np.array(years) #no.arrary()
builtupArea=years*0.0166+np.random.randint(-100,100)*0.00427
#dictionary
data={
'year':years,
'builtupArea':builtupArea
}    
pdf=pd.DataFrame(data=data)
pdf.to_csv('builtupArea-王霞.csv',index=False)