import pandas as pd
import numpy as np

data_csv='/Users/haixiangliu/Documents/水质数据及代码模型/water_clean_data.csv'
df=pd.DataFrame(pd.read_csv(data_csv))
#列重命名
df=df.rename(columns={'时间日期':'datetime', '液位':'water_level', 'DO':'do', 'MISS':'miss', '进风流量':'input_wind_throughput', '进气阀开度':'input_wind_openness', 'ts':'ts','进水COD':'input_water_cod', '出水COD':'output_water_cod', '进水氨氮':'input_water_ammonia', '出水总氮':'output_water_ammonia',
 '进水PH值':'input_water_ph','出水总磷':'output_water_phosphorus','进水SS':'input_water_ss','出水SS':'output_water_ss'})
#查看前5条数据
df.head()
df.describe()  #描述表信息：mean--均值，std--标准差
df['water_level'].min(),df['water_level'].max()
df['water_level'].size
#修改数据类型
df[['input_wind_throughput','input_wind_openness','input_water_cod','output_water_cod','output_water_ammonia','input_water_ss','output_water_ss']]=df[['input_wind_throughput','input_wind_openness','input_water_cod','output_water_cod','output_water_ammonia','input_water_ss','output_water_ss']].astype(float)
#直方图
df['water_level'].hist() 