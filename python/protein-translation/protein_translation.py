import re


translation_table = {
    'AUG': 'Methionine',
    'UUU': 'Phenylalanine',
    'UUC': 'Phenylalanine',
    'UUA': 'Leucine',
    'UUG': 'Leucine',
    'UCU': 'Serine',
    'UCC': 'Serine',
    'UCA': 'Serine',
    'UCG': 'Serine',
    'UAU': 'Tyrosine',
    'UAC': 'Tyrosine',
    'UGU': 'Cysteine',
    'UGC': 'Cysteine',
    'UGG': 'Tryptophan',
    'UAA': 'STOP',
    'UAG': 'STOP',
    'UGA': 'STOP'
}


def proteins(strand: str):
    aminos = []
    codons = re.findall(r"...", strand)
    for codon in codons:
        amino = translation_table.get(codon, None)
        if amino:
            if amino == 'STOP':
                break
            aminos.append(amino)

    return aminos

