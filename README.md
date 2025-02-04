# OmicsPipeline
A collection of bioinformatics scripts for sequence analysis, structural biology, and data visualization.
# 🔬 Bioinformatics Algorithms 🚀  

This repository contains Python scripts for essential **bioinformatics tasks**, including sequence alignment, BLAST search, structural analysis, and phylogenetic tree visualization. These algorithms are widely used in **computational biology, genomics, and structural bioinformatics**.

## 📜 Contents  

### 🧬 **1. Pairwise Sequence Alignment (Needleman-Wunsch Algorithm)**
- Implements **global sequence alignment** to compare two biological sequences.  
- Uses **Biopython’s `pairwise2` module** for optimal alignment.  
- 📌 File: [`needleman_wunsch.py`](scripts/needleman_wunsch.py)  

### 🔎 **2. BLAST Search Automation**
- Automates **BLASTp searches** using **NCBI’s qblast API** to find homologous sequences.  
- Extracts and reports **top hits, scores, and E-values**.  
- 📌 File: [`blast_search.py`](scripts/blast_search.py)  

### 🏗️ **3. Protein Structure Analysis (PDB Files)**
- Parses **PDB files** to extract chain information and residue count.  
- Uses **Biopython’s PDB module** for protein structure analysis.  
- 📌 File: [`pdb_analysis.py`](scripts/pdb_analysis.py)  

### 🧬 **4. GC Content Calculation**
- Computes **GC content** of a given DNA sequence.  
- Uses **Biopython’s `gc_fraction`** function.  
- 📌 File: [`gc_content.py`](scripts/gc_content.py)  

### 🌳 **5. Phylogenetic Tree Visualization**
- Reads and **visualizes a phylogenetic tree** from a Newick file.  
- Uses **Biopython’s Phylo module** and `matplotlib` for visualization.  
- 📌 File: [`phylogenetic_tree.py`](scripts/phylogenetic_tree.py)  
