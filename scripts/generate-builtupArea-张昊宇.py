# 生成模拟的建成区面积的Python脚本

import pandas as pd
import numpy as np
# 整形变量
year0 = 1990
year1 =2023
years = list(range(year0, year1))  #years 序列变量
years = np.array(years) # np.array)
builtupArea = years * 0.368 + np.random.randint(-100, 100) * 0.021
# dictionary 映射/字典类型

data = {
"year": years,
"builtupArea": builtupArea
}
pdf = pd.DataFrame(data = data)
pdf.to_csv('builtupArea-张昊宇.csv', index=False)