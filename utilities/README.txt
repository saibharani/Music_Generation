* link_to_transliterated_data.txt 
  contains the url to a large text file needed to train the model before fine-tuning.


the below scripts are written in python3. sel_transliterate.py is preferred to transliterate.py

* to_telugu_equal_csv.py   #requirements: xlwt
  takes file "./transliterated.txt" and splits it to "./telugu_equal.xls" needed to train the model before finetuning.

* transliterate.py         #requirements: requests, fake_useragent
  takes telugu file "./telugu_sentences_utf.txt" and transliterates it to "./transliterated.txt"

* sel_transliterate.py     #requirements: selenium (uses chrome webdriver)
  takes telugu file "./telugu_sentences_utf.txt" and transliterates it to "./transliterated.txt"
