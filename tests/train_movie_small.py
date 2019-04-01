from review_classifier import naive_bayes
from review_classifier import preprocess_scripts as ps

x_train = ['fun, couple, love, love',
           'fast, furious, shoot',
           'couple, fly, fast, fun, fun',
           'furious, shoot, shoot, fun',
           'fly, fast, shoot, love']

y_train = ['comedy',
           'action',
           'comedy',
           'action',
           'action']

test = 'fast, couple, shoot, fly'

MODEL_FILE = 'trained_model/movie-review-small.nb'


def train():
    nb = naive_bayes.Model()
    nb.train(map(ps.preprocess, x_train), y_train)
    nb.store_model(MODEL_FILE)
    return nb


if __name__ == '__main__':
    model = train()
    print(model.predict(ps.preprocess(test)))
