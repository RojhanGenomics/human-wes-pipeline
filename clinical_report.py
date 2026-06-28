import pandas as pd

df = pd.read_csv('/mnt/d/narmafzar_kargah/r_python/dr_kaki_exomseq/PatientFiles/mahshidkhadem-sample/mahshid.csv')

df['gnomADe_AF'] = pd.to_numeric(df['gnomADe_AF'], errors='coerce')
df['CADD_PHRED'] = pd.to_numeric(df['CADD_PHRED'], errors='coerce')

priority = df[
    (df['FILTER'] == 'PASS') &
    (df['IMPACT'].isin(['HIGH', 'MODERATE'])) &
    (df['gnomADe_AF'].isna() | (df['gnomADe_AF'] < 0.01)) &
    (
        df['CLIN_SIG'].str.contains('pathogenic', case=False, na=False) |
        (df['CADD_PHRED'] >= 28)
    )
].copy()

print("=" * 80)
print("CLINICAL VARIANT REPORT - Patient: Mahshid Khadem")
print("=" * 80)

for _, row in priority.iterrows():
    print(f"\nGene:        {row['SYMBOL']}")
    print(f"Variant:     {row['HGVSc']}")
    print(f"Protein:     {row['HGVSp']}")
    print(f"Consequence: {row['Consequence']}")
    print(f"gnomAD AF:   {row['gnomADe_AF']}")
    print(f"CADD:        {row['CADD_PHRED']}")
    print(f"ClinVar:     {row['CLIN_SIG']}")
    print(f"Zygosity:    {row.get('GT', 'N/A')}")
    print("-" * 40)
