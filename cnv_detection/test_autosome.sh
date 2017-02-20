#!/bin/bash -l
for each in `cat sample_list.txt`
do
	bamToBed -i ../lumpy_delly/$each.pesr.unique.rmdup.bam | coverageBed -a test.region.bed -b - -d>$each.cov.bed
	#s-277 as normal
	python calculate_autosome.py $each 0.582105263158 0.991578947368
	#s-279 as normal
	python calculate_autosome.py $each 0.573802541544 0.980449657869
done

