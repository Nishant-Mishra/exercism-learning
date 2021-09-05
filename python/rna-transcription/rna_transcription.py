"""
Given a DNA strand, return its RNA complement (per RNA transcription).

Both DNA and RNA strands are a sequence of nucleotides.

Given a DNA strand, its transcribed RNA strand is formed by replacing each nucleotide with its complement:

    G -> C
    C -> G
    T -> A
    A -> U

"""


transcription_map = {
    "G": "C",
    "C": "G",
    "T": "A",
    "A": "U"
}


def to_rna(dna_strand: str) -> str:
    """

    :param dna_strand: str: Sequence of neucleotides of the DNA Strand
    :return: str: Transcripted sequence of neucleotides of corresponding RNA strand
    """
    return "".join([transcription_map[nucleotide] for nucleotide in dna_strand])
