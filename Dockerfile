FROM broadinstitute/gatk:4.5.0.0

RUN apt-get update && apt-get install -y \
    bwa \
    samtools \
    fastp \
    && rm -rf /var/lib/apt/lists/*

ENV PATH /opt/conda/bin:$PATH
