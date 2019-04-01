from review_classifier import naive_bayes

MODEL_FILE = 'trained_model/movie-review-bigram.NB'
NGRAM = 2
DELIMETER = '|,|'
SMOOTHING = 1 * 10 ** -5.52


def train():
    nb = naive_bayes.train_from_csv('dataset/review_train.csv',
                                    'sentiment',
                                    'review',
                                    store_model=MODEL_FILE,
                                    ngram=NGRAM,
                                    delimeter=DELIMETER)
    return nb


def eval():
    error = naive_bayes.evaluate_test_csv_data('dataset/review_test.csv',
                                               MODEL_FILE,
                                               'sentiment',
                                               'review',
                                               ngram=NGRAM,
                                               delimeter=DELIMETER,
                                               smoothing=SMOOTHING)
    return error


if __name__ == '__main__':
    print('ngram = {ngram}, smoothing={smoothing}'.format(ngram=NGRAM, smoothing=SMOOTHING))
    trained_model = train()
    error = eval() * 100
    print("Error: {error}%".format(error=error))
