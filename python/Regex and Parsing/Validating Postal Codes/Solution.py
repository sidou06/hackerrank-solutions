regex_integer_in_range = r"\b([1-9]([0-9]){5})\b"  # Matches a 6-digit number starting with a non-zero digit

regex_alternating_repetitive_digit_pair = r"(?=(\d).\1)"  # Matches any two consecutive digits that are the same