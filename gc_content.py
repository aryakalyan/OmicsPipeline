pip install biopython
python gc_content.py
from Bio.SeqUtils import gc_fraction
# Input DNA sequence
dna_seq = "AGCTTAGCCTAGGCTAGGCCT"
# Compute GC content
gc_content = gc_fraction(dna_seq) * 100
print(f"GC Content: {gc_content:.2f}%")
