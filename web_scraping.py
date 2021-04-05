import requests
from pprint import pprint
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re
import string


def stripHtml(data):
	p = re.compile(r'<.*?>')
	return p.sub('', data)

arquivo = open('phoneticData.txt','w')
arquivo.close()


alfabeto = list(string.ascii_lowercase)
for letra in alfabeto:	

	num = 0
	retorno = True

	while retorno == True:
		
		arquivo = open('phoneticData.txt','a')

		url = "http://www.portaldalinguaportuguesa.org/index.php?action=fonetica&region=spx&act=list&letter=" + letra + "&start=" + str(num)
		f = urllib.request.urlopen(url)
		parsed_html = BeautifulSoup(f.read(), features="html.parser")
		elements = parsed_html.find(class_ = 'even')

			

		if elements != None:

			extracted = stripHtml(elements.text).split()
			
			final_result = [ x for x in extracted if "." in x  or "·" in x]
		
			x =range(len(final_result))
			c = 1
			npalavras = 1

			for i in x:
				if "·" in final_result[i]:
					npalavras = npalavras + 1

				if ("." in final_result[i]):
					if ("·" in final_result[i-1]):
						arquivo.write("{}\n".format(final_result[i-1]))
						arquivo.write("{}\n".format(final_result[i]))
						c = c + 1

			print("Letter: {}  Number of word: {}  Phonetic: {}  Result: {}".format(letra, npalavras, c, num))
	
			num = num + 20
		else:
			retorno = False
		
	arquivo.close()
