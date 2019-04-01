# MovieReviewClassifier
Bigram Naive Bayes model trained on IMDB movie review data. Given a movie review the model can predict the dominant sentiment.
<br>
## Installation
1 . Clone repo.

```
cd MovieReviewClassifier
```
<br>

2 . Navigate to project root.

```
cd MovieReviewClassifier
```
<br>

3 . Run tests to retrain and evaluate models.
```
python3 tests/train_movie_bigram.py
python3 tests/train_movie_bow.py
python3 tests/train_movie_small.py
```
<br>

## Usage
1 . Training and storing model.

```
nb = naive_bayes.Model()
nb.train(map(x_train, y_train)
nb.store_model('path/to/model')
```

2 . Loading and using model.
```
nb = naive_bayes.Model()
nb.load_model('path/to/model')
nb.predict('i love this movie')
```

<br>
Make sure python3 is installed in your system.
