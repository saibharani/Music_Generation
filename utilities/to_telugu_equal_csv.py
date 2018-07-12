import xlwt

book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1")
sheet1.write(0, 1, "text")
fobj = open('transliterated.txt')
txt = fobj.read()
txt_list = txt.split(" ")
txt_len = len(txt_list)
req_len = txt_len // 65000
counter = 0
i = 1
str_txt = ""
for word in txt_list:
	if (word.strip() != ""):
		str_txt += word
		str_txt += " "
		counter+=1
	if (counter == req_len):
		counter = 0
		sheet1.write(i,1,str_txt)
		str_txt = ""
		i += 1

book.save("telugu_equal.xls")
