# Human WES Clinical Analysis Pipeline

A production-grade Whole Exome Sequencing (WES) pipeline for clinical variant detection and interpretation, built with Nextflow and Docker.

## Pipeline Overview
FASTQ → FASTP → BWA-MEM → SAMTOOLS → GATK HaplotypeCaller → VEP → Clinical Report
## Tools & Versions
- Nextflow 26.04.3
- FASTP 0.23.4
- BWA 0.7.17
- SAMTOOLS 1.18
- GATK 4.5.0.0
- Ensembl VEP (latest)
- Python 3 (pandas)

## Reference Genome
- hg38 (GRCh38)
- dbSNP138

## Quick Start

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/human_wes_nf.git
cd human_wes_nf

# Edit samples.csv with your sample paths
# Edit nextflow.config with your reference path

# Run pipeline
nextflow run main.nf
```

## Output Structure
results/

├── fastp/          # Trimmed reads + QC reports

├── alignment/      # Sorted BAM files

├── variants/       # GVCF files from GATK

└── reports/        # Nextflow execution reports
## Clinical Filtering
Variants are filtered by:
- PASS filter status
- gnomAD AF < 1%
- CADD score > 18
- MODERATE or HIGH impact

## Author
Mahdieh — PhD Genetics

## nf-core/sarek Integration Note

Attempted integration with nf-core/sarek v3.9.0 (dev branch).

**Finding:** Nextflow v26 introduced breaking changes in config syntax that affect all stable releases of sarek (v3.2.3 through v3.6.0). The dev branch partially works but contains a SENTIEON_BWAMEM process collision bug when using local reference files.

**Workaround:** Custom pipeline built from scratch using individual biocontainers (FASTP, BWA-MEM, SAMTOOLS, GATK) with equivalent functionality to sarek germline variant calling workflow.

**Status:** Monitoring nf-core/sarek for Nextflow v26 compatibility fix.
