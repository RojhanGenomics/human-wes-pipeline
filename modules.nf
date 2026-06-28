process FASTP {
    tag "${sample}"
    publishDir "${params.outdir}/fastp", mode: 'copy'

    input:
    tuple val(sample), path(r1), path(r2)

    output:
    tuple val(sample), path("${sample}_R1.trim.fastq.gz"), path("${sample}_R2.trim.fastq.gz")

    script:
    """
    fastp -i $r1 -I $r2 \
        -o ${sample}_R1.trim.fastq.gz \
        -O ${sample}_R2.trim.fastq.gz \
        --thread ${params.threads} \
        --json ${sample}_fastp.json \
        --html ${sample}_fastp.html
    """
}

process BWA_MEM {
    tag "${sample}"

    input:
    tuple val(sample), path(r1), path(r2)
    path(ref_files)

    output:
    tuple val(sample), path("${sample}.sam")

    script:
    def ref = ref_files[0]
    """
    bwa mem -t ${params.threads} \
        -R "@RG\\tID:${sample}\\tSM:${sample}\\tPL:ILLUMINA\\tLB:${sample}" \
        ${ref} $r1 $r2 > ${sample}.sam
    """
}

process SAMTOOLS_SORT {
    tag "${sample}"
    publishDir "${params.outdir}/alignment", mode: 'copy'

    input:
    tuple val(sample), path(sam)

    output:
    tuple val(sample), path("${sample}.sorted.bam")

    script:
    """
    samtools view -bS $sam | samtools sort -@ ${params.threads} -o ${sample}.sorted.bam
    """
}

process SAMTOOLS_INDEX {
    tag "${sample}"
    publishDir "${params.outdir}/alignment", mode: 'copy'

    input:
    tuple val(sample), path(bam)

    output:
    tuple val(sample), path(bam), path("${bam}.bai")

    script:
    """
    samtools index $bam
    """
}

process GATK_HAPLOTYPECALLER {
    tag "${sample}"
    publishDir "${params.outdir}/variants", mode: 'copy'

    input:
    tuple val(sample), path(bam), path(bai)
    path(ref_files)

    output:
    tuple val(sample), path("${sample}.g.vcf.gz")

    script:
    def ref = ref_files[0]
    """
    gatk HaplotypeCaller \
        -R ${ref} \
        -I $bam \
        -O ${sample}.g.vcf.gz \
        -ERC GVCF \
        --native-pair-hmm-threads ${params.threads}
    """
}
