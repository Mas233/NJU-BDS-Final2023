# Rebounds and Points

- 简介：利用python清洗数据并计算`PLAYERS`表有效数据中Rebounds和Points的协方差和相关系数并分析。

- 分析方式：python、pandas

- 详细说明：
  
  - 从已生成的所有csv表格建立一个pandas中的dataframe类型，即
    
    ```python
    dataframes = []
    for i in range(1, 31):
        path = '../table_generation/tables/'+str(i)+'/PLAYERS.csv'
        df = pandas.read_csv(path)
        dataframes.append(df)
    
    df = pandas.concat(dataframes)
    ```
  
  - 选出Rebounds列和Points列
    
    ```python
    df = df[['Points', 'Rebounds']]
    ```
  
  - 数据清洗，即筛选掉所有不符合数字要求的数据
    
    ```python
    df = df.applymap(pandas.to_numeric, errors='coerce').dropna()
    df = df[(df['Rebounds'] > 0) & (df['Points'] > 0)]
    ```
  
  - 协方差和相关系数计算：
    
    ```python
    cov_matrix = df.cov()
    corr_matrix = df.corr()
    
    cov = cov_matrix.loc['Points','Rebounds']
    corr = corr_matrix.loc['Points','Rebounds']
    ```
  
  - 输出：
    
    ```python
    print("Between Points and Rebounds:\nCov:"+str(cov)+"\nCorr:"+str(corr))
    ```

- 输出结果：
  
  ![](C:\Users\Mad_Mas\AppData\Roaming\marktext\images\2023-07-01-01-31-01-image.png)

- 分析与结论：
  
  得分和篮板球相关系数约为0.143，其大于零说明得分和篮板球数量变化方向是一致的；其绝对值不接近1，说明这种相同变化方向趋势的相关性比较微弱，二者并不具有明显的线性相关关系。

- 源代码：

```python
import pandas


# get dataframe

dataframes = []
for i in range(1, 31):
    path = '../table_generation/tables/'+str(i)+'/PLAYERS.csv'
    df = pandas.read_csv(path)
    dataframes.append(df)

df = pandas.concat(dataframes)

# select columns

df = df[['Points', 'Rebounds']]

# clear invalid values

df = df.applymap(pandas.to_numeric, errors='coerce').dropna()
df = df[(df['Rebounds'] > 0) & (df['Points'] > 0)]

cov_matrix = df.cov()
corr_matrix = df.corr()

cov = cov_matrix.loc['Points','Rebounds']
corr = corr_matrix.loc['Points','Rebounds']

print("Between Points and Rebounds:\nCov:"+str(cov)+"\nCorr:"+str(corr))
```
