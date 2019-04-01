from review_classifier import preprocess_scripts as ps
from review_classifier.naive_bayes import Model

def read_csv(file_loc, sep=','):
    csv_dict = {}
    csv_file = open(file_loc, 'r+')

    header_line = csv_file.readline().strip()
    headers = header_line.split(sep)
    for header in headers:
        csv_dict[header] = []

    for line in csv_file:
        line = line.strip()
        data_pieces = line.split(sep)
        for piece, header in zip(data_pieces, headers):
            csv_dict[header].append(piece)

    return csv_dict


def train_from_csv(train_data, label, feature, store_model=None, ngram=1, delimeter=','):
    dataset = read_csv(train_data, sep=delimeter)

    x_train = map(ps.preprocess, dataset[feature])
    x_train = map(lambda x: ps.ngrams(x, ngram), x_train)
    y_train = dataset[label]

    nb = Model()
    nb.train(x_train, y_train)

    if store_model is not None:
        nb.store_model(store_model)
    return nb


def evaluate_test_csv_data(test_data, model_loc, label, feature, ngram=1, delimeter=',', smoothing = 1):
    dataset = read_csv(test_data, sep=delimeter)

    x_test = map(ps.preprocess, dataset[feature])
    x_test = map(lambda x: ps.ngrams(x, ngram), x_test)
    y_test = dataset[label]

    nb = Model()
    nb._SMOOTHING = smoothing
    nb.load_model(model_loc)

    return nb.evaluate(x_test, y_test)


def load_trained_model(model_file):
    nb = Model()
    nb.load_model(model_file)
    return nb
