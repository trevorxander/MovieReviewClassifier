import os
from setuptools import setup, find_packages


def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()

setup(
    name='Movie Review Classifier',
    version='0.1',
    url='https://github.com/trevorxander/MovieReviewClassifier',
    license='',
    author='Trevor Xander',
    author_email='trevorcolexander@gmail.com',
    install_requires=[],
    packages=find_packages()
)
