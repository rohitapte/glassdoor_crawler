from nltk import word_tokenize
from gensim.models import Word2Vec

class MySentences(object):
    def __init__(self):
        self.filename='AggregateData.txt'

    def __iter__(self):
        with open(self.filename,encoding='utf-8') as f:
            for line in f:
                yield word_tokenize(line)

if __name__ == "__main__":
    sentences = MySentences()
    model = Word2Vec(sentences=sentences, vector_size=50, window=5, min_count=1, workers=4)
    model.save("word2vec.model")
