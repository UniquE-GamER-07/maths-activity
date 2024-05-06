import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 1 Creating a DataFrame from a csv file

## 1.1 Carbon footprint

# reading the csv file
df_traffic = pd.read_csv('maths.csv')

df_flow = df_traffic

df_flow= df_flow

df_flow.plot(kind='line',
              xlabel='Traffic Density ',
              ylabel='Position',
              title='UAE TRAFFIC ')

#save plot
plt.savefig('Carbon Footprint')
#show plot
plt.show()

df_flow.to_excel('Carbon_foorprint.xlsx')