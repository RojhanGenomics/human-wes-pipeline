report = """
╔══════════════════════════════════════════════════════════════════════════════╗
║           CLINICAL GENOMICS REPORT - WES Analysis                          ║
║           Patient: Mahshid Khadem                                          ║
╚══════════════════════════════════════════════════════════════════════════════╝

━━━ TIER 1: ACTIONABLE FINDINGS ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. DPYD c.85T>C (p.Cys29Arg) — HETEROZYGOUS
   Classification : Pathogenic / Drug Response
   Clinical Impact: PHARMACOGENOMICS ALERT
   Action Required: Avoid 5-Fluorouracil (5-FU) and Capecitabine
                    Risk of severe/fatal toxicity if used in chemotherapy
   CADD Score     : 18.87

2. RUNX1 c.1270T>C (p.Ser424Pro) — HETEROZYGOUS  
   Classification : Likely Pathogenic (ClinVar)
   Inheritance    : Autosomal Dominant
   Clinical Impact: Familial Platelet Disorder + AML predisposition
   Action Required: Hematology referral, CBC monitoring, family screening
   CADD Score     : 28.5

━━━ TIER 2: LIKELY SIGNIFICANT ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

3. PAH c.1207C>T (p.Arg403Trp) — HETEROZYGOUS
   Classification : Pathogenic (ClinVar) — PKU gene
   Clinical Impact: Carrier status for Phenylketonuria
   Note           : Second allele needs evaluation for compound heterozygosity
   CADD Score     : 28.9

4. RYR1 c.1882C>T (p.Arg628Cys) — HETEROZYGOUS
   Classification : Uncertain Significance
   Clinical Impact: Malignant Hyperthermia susceptibility
   Action Required: Alert anesthesiologist before any general anesthesia
   CADD Score     : 28.5

5. TRPM4 c.3224T>G (p.Leu1075Arg) — HETEROZYGOUS
   Classification : Uncertain Significance
   Clinical Impact: Cardiac conduction disorder risk
   Action Required: Cardiology evaluation (ECG)
   CADD Score     : 29.6

━━━ TIER 3: VARIANTS OF UNCERTAIN SIGNIFICANCE ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

6. LAMA5 c.6157C>T (p.Arg2053Cys) — HETEROZYGOUS
   Classification : Uncertain Significance / Pathogenic (conflict)
   Clinical Impact: Renal/neurological disease association

7. MAN2C1 c.2303G>A (p.Arg768Gln) — HETEROZYGOUS
   Classification : Pathogenic
   Clinical Impact: Metabolic disorder association

━━━ RECOMMENDATIONS ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. URGENT: Update medical record with DPYD status before any chemotherapy
2. Hematology referral for RUNX1 variant evaluation
3. Family screening for RUNX1 (autosomal dominant)
4. Anesthesia alert card for RYR1
5. Cardiology ECG for TRPM4
6. PAH carrier counseling + partner testing recommended

━━━ PIPELINE INFO ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Reference   : hg38
Variant Call: GATK HaplotypeCaller v4.1.6
Annotation  : Ensembl VEP
Filter      : PASS only, gnomAD AF < 1%, CADD > 18
"""
print(report)

with open('clinical_report_mahshid.txt', 'w') as f:
    f.write(report)
print("Report saved: clinical_report_mahshid.txt")
