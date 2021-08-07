def distance(strand_a: str, strand_b: str) -> int:

    if len(strand_a) != len(strand_b):
        raise ValueError(f"DNA strands have different lengths.")

    return sum(dna_a != dna_b for dna_a, dna_b in zip(strand_a, strand_b))
