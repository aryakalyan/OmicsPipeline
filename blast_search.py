pip install biopython
python blast_search.py
from Bio.Blast import NCBIWWW, NCBIXML
# Input protein sequence
query_seq = ">seq1\nMVLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPH" #modify query seq

# Run BLASTp
result_handle = NCBIWWW.qblast("blastp", "nr", query_seq)

# Parse and display BLAST results
blast_record = NCBIXML.read(result_handle)
for alignment in blast_record.alignments[:5]:
    print(f"Hit: {alignment.title}\nScore: {alignment.hsps[0].score}\n")
