def encode(decoded: str) -> str:
    if len(decoded) == 0:
        return ""

    encoded = ""
    cur_ch = decoded[0]
    cnt_cur_ch = 1

    for ch in decoded[1:]:
        if ch == cur_ch:
            cnt_cur_ch += 1
        else:
            cnt = str(cnt_cur_ch) if cnt_cur_ch > 1 else ""
            encoded += cnt + cur_ch

            cur_ch = ch
            cnt_cur_ch = 1

    cnt = str(cnt_cur_ch) if cnt_cur_ch > 1 else ""
    encoded += cnt + cur_ch

    return encoded


def decode(encoded: str) -> str:

    decoded = ""
    cur_number_as_str = ""

    for ch in encoded:
        if ch.isdigit():
            cur_number_as_str += ch
        else:
            cur_number = int(cur_number_as_str) if len(cur_number_as_str) > 0 else 1
            decoded += ch * cur_number
            cur_number_as_str = ""

    return decoded
