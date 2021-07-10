from nltk import word_tokenize
from gensim.models import Word2Vec

class Word2VecCorpus(object):
    def __init__(self):
        self.filename='AggregateData.txt'

    def __iter__(self):
        with open(self.filename,encoding='utf-8') as f:
            for line in f:
                yield word_tokenize(line)

if __name__ == "__main__":
    sentences = Word2VecCorpus()
    vector_size=50
    window=5
    min_count=3
    model = Word2Vec(sentences=sentences, vector_size=vector_size, window=window, min_count=min_count, workers=8)
    model.save("word2vec.model_"+str(vector_size)+"_"+str(window)+"_"+str(min_count))
