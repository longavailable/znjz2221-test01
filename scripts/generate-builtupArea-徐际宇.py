import numpy as np
import pandas as pd

# 整型变量
year0 = 1990
year1 = 2023


years = list(range(year0, year1))

years = np.array(years)

builtupArea = years * 0.308 + np.random.randint(-100, 100) * 0.023

# dictionary 映射/字典类型
data = {
	"year": years,
	"builtupArea": builtupArea
}

pdf = pd.DataFrame(data=data)

pdf.to_csv('builtupArea-徐际宇.csv', index=False)
