# -*- coding: utf-8 -*-
from gensim.models import word2vec
#data = word2vec.Text8Corpus('text07161724.txt')
#model = word2vec.Word2Vec(data,size=300)
#model.save('text0716.bin')
model =word2vec.Word2Vec.load('text0716.bin')

key = raw_input("keyを入力してください: ")
print key
key = unicode(key,'utf-8')
print '-------------------------------'
out=model.most_similar(positive=[key],topn=10)
for x in out:
    print x[0],x[1]
