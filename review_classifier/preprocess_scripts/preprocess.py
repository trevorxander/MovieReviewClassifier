from review_classifier.preprocess_scripts.filter import remove_non_alpha
from review_classifier.preprocess_scripts.stop_words import filter_stop_words

_preprocess = [str.lower, remove_non_alpha]


def preprocess(sentence):
    processed_sentence = sentence
    for process in _preprocess:
        processed_sentence = process(processed_sentence)

    return processed_sentence
