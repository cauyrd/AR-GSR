#!/bin/bash -l
bamToBed -i /home/dehms/shared/ryang/DNAseq/local_PCa/lumpy_delly/S-260_S44.pesr.unique.rmdup.bam | coverageBed -a test.region.bed -b - -d>S-260_S44_as_normal.cov.bed
python calculate.py S-260_S44_as_normal

