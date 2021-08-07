_rna_by_dna = str.maketrans("CGTA", "GCAU")


def to_rna(dna_strand: str) -> str:
    return dna_strand.translate(_rna_by_dna)
