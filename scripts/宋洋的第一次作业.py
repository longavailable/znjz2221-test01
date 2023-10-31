# 生成模拟的建成区面积的Python脚本


import pandas as pd
import numpy as np
#整型变量
year0 = 1990
year1 = 2023
years = list(range(year0,year1))#years 序列变量
years = np.array(years) # np.array）
builtupArea = years * 0.0146+np.random.randint(-100,100)*0.035
#dictionary

data = {
'year':years,
'builtupArea':builtupArea
}
pdf=pd.DataFrame(data=data)
pdf.to_csv('builtupArea-宋洋.csv',index=False)