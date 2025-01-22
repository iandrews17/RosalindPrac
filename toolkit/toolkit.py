# DNA Toolkit
from toolkit.structures import *
import collections



# This function will check a sequence to ensure its a dna string. If any codons are lowercase will return as uppercase
def validateSeq(dna_seq):
    temp_seq = dna_seq.upper()
    for nuc in temp_seq:
        if nuc not in Nucleotides:
            return False
    return temp_seq

# Uses a dict to count nuc frequency
def countNucFrequency(dna_seq):
    temp_freq_dict = {'A': 0, 'C': 0, 'G' :0, 'T': 0}
    for nuc in dna_seq:
        temp_freq_dict[nuc] += 1
    return temp_freq_dict
    # can be one line as
    # return dict(collections.Counter(dna_seq))

# Will do a DNA -> RNA Transcription replacing 'T' with 'U'
def transcription(dna_seq):
    return dna_seq.replace('T', 'U')
    
# Will return the complement of DNA
def reverse_complement(dna_seq):
    return ''.join([DNA_reverse_complement[nuc] for nuc in dna_seq])[::-1]