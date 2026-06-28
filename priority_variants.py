import pandas as pd

df = pd.read_csv('/mnt/d/narmafzar_kargah/r_python/dr_kaki_exomseq/PatientFiles/mahshidkhadem-sample/mahshid.csv')

# فقط PASS + MODERATE + نادر
pass_mod = df[
    (df['FILTER'] == 'PASS') & 
    (df['IMPACT'].isin(['HIGH', 'MODERATE']))
].copy()
pass_mod['gnomADe_AF'] = pd.to_numeric(pass_mod['gnomADe_AF'], errors='coerce')
rare = pass_mod[pass_mod['gnomADe_AF'].isna() | (pass_mod['gnomADe_AF'] < 0.01)]

# واریانت‌های pathogenic یا likely_pathogenic
print("=== PATHOGENIC / LIKELY PATHOGENIC ===")
path = rare[rare['CLIN_SIG'].str.contains('pathogenic', case=False, na=False) & 
            ~rare['CLIN_SIG'].str.contains('likely_benign|benign', case=False, na=False)]
cols = ['SYMBOL','Consequence','HGVSp','gnomADe_AF','CLIN_SIG','CADD_PHRED','FILTER']
print(path[cols].to_string())

# CADD بالا (>25) بدون annotation
print("\n=== HIGH CADD (>25) - Novel Candidates ===")
high_cadd = rare[
    (pd.to_numeric(rare['CADD_PHRED'], errors='coerce') > 25) &
    (rare['CLIN_SIG'] == '-')
]
print(high_cadd[cols].to_string())
