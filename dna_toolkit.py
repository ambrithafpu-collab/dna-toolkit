# Step 2: GC Content Calculator
def gc_content(dna):
    g_count = dna.count('G')
    c_count = dna.count('C')
    total = len(dna)
    gc_percentage = ((g_count + c_count) / total) * 100
    return round(gc_percentage, 2)

# Test it
my_dna = "ATGCGATACGCTTCGATCGATCGATCGTAGCTAGCTAGCATCGATCGATCG"

print("\n🔬 GC Content Analysis:")
print(f"   DNA Sequence : {my_dna}")
print(f"   Total Length : {len(my_dna)} nucleotides")
print(f"   GC Content   : {gc_content(my_dna)}%")

# Health check
gc = gc_content(my_dna)
if 40 <= gc <= 60:
    print("   Status       : ✅ Normal GC range")
else:
    print("   Status       : ⚠️ Abnormal GC range - possible mutation!")
    # Step 3: DNA to RNA Transcription
def transcribe(dna):
    rna = dna.replace("T", "U")
    return rna

# Test it
print("\n🧬 Transcription Analysis:")
print(f"   DNA : {my_dna}")
print(f"   RNA : {transcribe(my_dna)}")
# Step 4: RNA to Protein Translation
def translate(dna):
    from Bio.Seq import Seq
    seq = Seq(dna)
    protein = seq.translate()
    return protein

# Test it
print("\n🧪 Translation Analysis:")
print(f"   DNA     : {my_dna}")
print(f"   RNA     : {transcribe(my_dna)}")
print(f"   Protein : {translate(my_dna)}")
# Step 5: Reverse Complement
def reverse_complement(dna):
    from Bio.Seq import Seq
    seq = Seq(dna)
    return seq.reverse_complement()

# Test it
print("\n🔄 Reverse Complement Analysis:")
print(f"   Original DNA : {my_dna}")
print(f"   Reverse Comp : {reverse_complement(my_dna)}")
