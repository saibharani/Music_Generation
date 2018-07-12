import requests
from fake_useragent import UserAgent

f = open('telugu_sentences_utf.txt')
out = open('translated1.txt','w')
ua = UserAgent()

header = {'User-Agent':str(ua.firefox)}
cookie = {'sgtransliteration-sourcelist':'velthuis,hk,telugu', 'sgtransliteration-targetlist':'devanagari,iso15919,itrans'}
i=0
lines = []

for line in f:
    i += 1
    lines.append(line)
    if i%10000 is 0 or i is 1843386:
        print(i)
        telugu_text = "".join(lines)
        lines=[]
        r = requests.post("https://www.ashtangayoga.info/index.php", headers=header, cookies=cookie, data={'action': 'translate', 'controller': 'Ajax\Transliterator', 'eID': 'sgAjax', 'extensionName': 'SgTransliterator', 'format': 'json', 'parameters[from]': 'telugu', 'parameters[text]': telugu_text, 'parameters[to]': 'itrans'})
        translated_lines = r.json()['translation'].split("<br />")
        out.write("".join(translated_lines))

f.close()
out.close()
