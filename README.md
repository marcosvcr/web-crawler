
Sequencial crawler

Requirements:
	python 3.7 or above

Install the packages:
	pip3 install -r requirements.txt

	necessary download the webdriver for chrome (https://chromedriver.storage.googleapis.com/index.html?path=90.0.4430.24/)
	
	
	The webpage accessed is http://www.portaldalinguaportuguesa.org/ that includes information about language resources in portuguese.
	
	the crawler is a program that access the website and check whether  it access these API follows:
	
	Information Grabbed grabbed:
	
		- Console
		- Page Transition Event
		- Location
		- User Agent
		- Time
		
		
	To run:
	
		python crawler.py <path/to/webdriver> <path/to/list/sites>
		python parallelized_crawler.py <path/to/webdriver>
		
	obs: -1 on the info means the crawler faeiled to access the website 
	


 New Feature*:  scraping the webpage to genarate a phonetic database and traning a model to decode a aphabetic string into a phonetic string Using Hidden Markov Models

  -  Run web_scraping.py to generate the data
  -  Run hmm.py to generate the model



