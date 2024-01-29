import pandas as pd
import numpy as np
data = pd.read_csv('공공보건의료기관현황.csv', index_col=0, encoding='utf-8-sig’)
print(data.columns)
data.head()
