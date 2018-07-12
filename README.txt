* charRNN_vanilla.py
  A lyrics generator based on character level RNN. It requires the data in the form of a csv in the same format as the file "div_songs.csv" that contains Tyagaraja's songs. It uses 4 RNNs, one each for pallavis and anupallavis. It also has a separate RNN for the last caraNam of each song, and one for the rest. The RNN for the last caraNam of each song is to generate Tyagaraja's signature in the last caraNam. The number of caraNams is determined by sampling from a Normal distribution using the mean and std deviation of the given data.
  Generated samples in charRNN_vanilla_samples.txt

* charRNN_finetuned.py
  Based on the above model, where the weights of the charRNNs are initialised to the value obtained by training on a much larger dataset of telugu text.
  Generated samples in charRNN_finetuned.txt

Both files above are implemented using python2 with pytorch==0.4
  
* Utilities
 Contains tools to transliterate telugu text and to convert it to the required csv file. Also contains a link to a telugu text with a million lines transliterated to english.
