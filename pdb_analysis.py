pip install biopython
python pdb_analysis.py
from Bio import PDB

pdb_id = "4AA8"  # Example PDB ID for chymosin

# Fetch and parse PDB file
parser = PDB.PDBParser(QUIET=True)
structure = parser.get_structure(pdb_id, f"{pdb_id}.pdb")

# Extract chain and residue information
for model in structure:
    for chain in model:
        print(f"Chain: {chain.id}, Residues: {len(chain)}")
