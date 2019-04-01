def ngrams(text, n):
    ngrams = ''
    iter_count = 1
    for word in text.split():
        ngrams += word

        if iter_count % n == 0:
            ngrams += ' '
        else:
            ngrams += '_'
        iter_count += 1
    return ngrams
