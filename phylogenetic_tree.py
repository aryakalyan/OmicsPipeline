pip install biopython matplotlib
python phylogenetic_tree.py
from Bio import Phylo
import matplotlib.pyplot as plt

# Load Newick tree from a file
tree = Phylo.read("example_tree.nwk", "newick")

# Display the phylogenetic tree
Phylo.draw(tree)
plt.show()
