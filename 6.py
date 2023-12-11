import pandas as pd
data= {
    'Names': ['Alice','Bob','Charlie','David'],
    'Age':[25,30,35,40]
}
df=pd.DataFrame(data)
print(df['Age'.median()])