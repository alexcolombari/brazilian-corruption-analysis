import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

file_name = 'dataset.xlsx'
df = pd.read_excel(file_name, sheet_name = 1)

# Drop columns with NaN values
df = df.drop(df.columns[[3, 4, 5, 6]], axis=1)

# Filter DF data with only target name
empresa = 'ANDRADE GUTIERREZ'
partido = 'PR'
filtered = df [df["Source"] == empresa]
filtered_data = filtered [filtered["Target"] == partido]

valores = filtered_data["Value"].values
soma = [len(valores)]
soma = np.append(soma, valores) 

if len(soma) >= 10:
	x = "bilhões"
if len(soma) <= 9:
	x = "milhões"	# 1 000 000 000
else:
	x = "mil"

#print("Total: R$ {}".format(soma.sum()))
print("A empresa {} enviou um total de: R$ {} {} para o partido: {}"\
	.format(empresa,soma.sum(), x, partido))
'''total = df['Type'].max()
print("Total: {}".format(total))'''
