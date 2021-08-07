def convert(number):
    result = ""

    pairs = ((3, "Pling"), (5, "Plang"), (7, "Plong"))
    for factor, sound in pairs:
        if number % factor == 0:
            result += sound

    # Fallback
    if len(result) == 0:
        result = str(number)

    return result
