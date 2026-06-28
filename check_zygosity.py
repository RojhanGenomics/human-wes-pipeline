import pandas as pd

df = pd.read_csv('/mnt/d/narmafzar_kargah/r_python/dr_kaki_exomseq/PatientFiles/mahshidkhadem-sample/mahshid.csv')

# ژن‌های مهم
genes_of_interest = ['PAH', 'RUNX1', 'RYR1', 'TRPM4', 'LAMA5', 'MAN2C1', 'DPYD']

subset = df[df['SYMBOL'].isin(genes_of_interest)]
cols = ['SYMBOL', 'Consequence', 'HGVSp', 'CLIN_SIG', 'CADD_PHRED', 'FILTER', '20']
print(subset[cols].to_string())
