import pandas as pd

df = pd.read_csv('/mnt/d/narmafzar_kargah/r_python/dr_kaki_exomseq/PatientFiles/mahshidkhadem-sample/mahshid.csv')

# فقط PASS variants با MODERATE یا بالاتر
pass_variants = df[
    (df['FILTER'] == 'PASS') & 
    (df['IMPACT'].isin(['HIGH', 'MODERATE']))
].copy()

print(f"PASS + MODERATE/HIGH variants: {len(pass_variants)}")

# فرکانس gnomAD
pass_variants['gnomADe_AF'] = pd.to_numeric(pass_variants['gnomADe_AF'], errors='coerce')

# نادر یا ناشناخته
rare = pass_variants[
    pass_variants['gnomADe_AF'].isna() | 
    (pass_variants['gnomADe_AF'] < 0.01)
].copy()

print(f"Rare/Novel PASS variants: {len(rare)}")
print("\n=== TOP CANDIDATES ===")
cols = ['SYMBOL','Consequence','HGVSc','HGVSp','gnomADe_AF','CLIN_SIG','CADD_PHRED']
print(rare[cols].to_string())
