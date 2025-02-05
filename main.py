from stronghold.fib import rabbit_fib
from toolkit.toolkit import *
from toolkit.util import *
from stronghold import *
import random

random_dna_str = ''.join([random.choice(Nucleotides) for nuc in range(50)])
dna_str = validateSeq(random_dna_str)



# print(f'\n Sequence: {colored(dna_str)}\n')
# print(f'[1] Sequence Length: {len(dna_str)} \n')
# print(colored(f'[2] Nucleotide Frequency: {countNucFrequency(dna_str)} \n'))
# print(f'[3] RNA Transcription: {transcription(dna_str)} \n')
# print(f"[4] DNA String + Reverse Complement:\n5' {colored(dna_str)} 3'")
# print(f"   {''.join(['|' for c in range(len(dna_str))])}")
# print(f"3' {colored(reverse_complement(dna_str))} 5'\n")
