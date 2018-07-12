from selenium import webdriver

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get("http://lekhini.org/nikhile.html")
inp = driver.find_element_by_id("txtInput")
out = driver.find_element_by_id("txtOutput")
btn = driver.find_element_by_id("btnTransform")

fin = open('telugu_sentences_utf.txt')
fout = open('transliterated.txt','w')

for i in range(92):
    lines = [next(fin) for j in range(20000)]
    itext = ''.join(lines)
    itext = "\\n".join(itext.split('\n'))
    itext = "\\'".join(itext.split("\'"))
    itext = '\\"'.join(itext.split('\"'))
    jsscript = "document.getElementById(\'txtInput\').value=\'" + str(itext) + "\';"
    driver.execute_script(jsscript)
    btn.click()
    otext = out.get_property('value')
    fout.write(otext)
    print(str(i+1) + "/92")

driver.quit()
fin.close()
fout.close()
