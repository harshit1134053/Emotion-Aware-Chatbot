def truncate(text, max_len=300):
    return text if len(text) <= max_len else text[:max_len] + "..."