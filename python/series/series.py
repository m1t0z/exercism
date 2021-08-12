def slices(series: str, length: int) -> list[str]:

    series_len = len(series)

    if not (0 < length <= series_len):
        raise ValueError("Incorrect input data!")

    cnt = len(series) - length + 1
    return [series[i : length + i] for i in range(0, cnt)]
