# w2v
repository for developing word2vec
This repository was developed by `graph226` alone. Excuse me of my BAD English.

## `crawler.py`

This file is getting URLs from seed URL. It collects all the URLs in the htmls by setting "depth" (line 9). 
You can get JSON format file includes URLs.

## `mecab.py`

This file is getting separated `txts` from JSON file that you made. It dumps htmls from input file and separates them by using `mecab`. 
It also deletes html tags setted in `STOP WORD`.

## `word2vAozora`

This file is made for using word2vec from python. You need word-separated ONE txt file for training neural network.
If you want to use word2vec from trained data, you must set binary file for input. **You can change behavior of word2vec by using comment line in this code.**
