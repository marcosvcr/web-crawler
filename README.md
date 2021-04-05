
Sequencial crawler

Requirements:
	python 3.7 ou above
	packages:
	- selenium
	- pandas
	- numpy
	- BeautifulSoup
	- 
	webdriver for chrome (https://chromedriver.storage.googleapis.com/index.html?path=90.0.4430.24/)
	
	
	The webpage accessed is http://www.portaldalinguaportuguesa.org/ that includes information about language resources in portuguese.
	
	the crawler is a program that browses the  phonetical content website and randomly chooses the letters.
	
	Information Grabbed grabbed:
	
		- Application name agent
		- Version of the application
		- location
		- Platform
		- Time of the browser
		
		
	To run:
	
		python crawler.py <path/to/webdriver>
	


 New Feature*:  scraping the webpage to genarate a phonetic database and traning a model to decode a aphabetic string into a phonetic string Using Hidden Markov Models

  -  Run web_scraping.py to generate the data
  -  Run hmm.py to generate the model
