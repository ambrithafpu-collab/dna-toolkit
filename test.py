from Bio.Seq import Seq
dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
print("DNA:", dna)
print("RNA:", dna.transcribe())
print("Protein:", dna.translate())
