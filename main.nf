nextflow.enable.dsl = 2

include { FASTP; BWA_MEM; SAMTOOLS_SORT; SAMTOOLS_INDEX; GATK_HAPLOTYPECALLER } from './modules.nf'

workflow {

    samples_ch = Channel
        .fromPath(params.samples)
        .splitCsv(header: true)
        .map { row ->
            tuple(
                row.sample,
                file(row.fastq_1, checkIfExists: true),
                file(row.fastq_2, checkIfExists: true)
            )
        }

    ref_ch = Channel.value([
        file(params.reference),
        file("${params.reference}.amb"),
        file("${params.reference}.ann"),
        file("${params.reference}.bwt"),
        file("${params.reference}.pac"),
        file("${params.reference}.sa"),
        file("${params.reference}.fai"),
        file("/mnt/d/narmafzar_kargah/r_python/dr_kaki_exomseq/genome_R/hg38.fa/hg38.dict")
    ])

    trimmed_ch = FASTP(samples_ch)
    aligned_ch = BWA_MEM(trimmed_ch, ref_ch)
    sorted_ch  = SAMTOOLS_SORT(aligned_ch)
    indexed_ch = SAMTOOLS_INDEX(sorted_ch)
    GATK_HAPLOTYPECALLER(indexed_ch, ref_ch)
}
