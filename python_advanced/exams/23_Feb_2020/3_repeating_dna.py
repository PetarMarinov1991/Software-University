def get_repeating_DNA(dna):
    start = 0
    end = 10

    combinations = []
    while end <= len(dna):
        combinations.append(dna[start:end])
        start += 1
        end += 1
    return [x for n, x in enumerate(combinations) if x in combinations[:n]]
