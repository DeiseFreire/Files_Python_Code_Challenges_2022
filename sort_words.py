def sort_words(input):
    return ' '.join(sorted(input.split(), key = str.casefold))
