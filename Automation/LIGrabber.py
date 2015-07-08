#LinkedIn Name and position grabber

import argparse, random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

LinkedIn = "https://www.linkedin.com/uas/login"
facebook = "https://www.facebook.com"
youtube = "https://www.youtube.com/subscriptions"
reddit = "https://www.reddit.com"
bbc = "https://www.bbc.co.uk"


def openPage(webBrowser, page):
	webBrowser.get(page)
	html = webBrowser.find_element_by_xpath("/html")
	html.send_keys(Keys.CONTROL + "t")
	import os
	
# from selenium import webdriver
# chromedriver = "/Users/adam/Downloads/chromedriver"
# os.environ["webdriver.chrome.driver"] = chromedriver
# driver = webdriver.Chrome(chromedriver)
# driver.get("http://stackoverflow.com")
# driver.quit()

	



def main():
	print "Reading args..."
	parser = argparse.ArgumentParser()
	parser.add_argument("email", help = "LinkedIn email")
	parser.add_argument("password", help = "LinkedIn password")
	args = parser.parse_args()

	browser = webdriver.Firefox()
	openPage(browser, facebook)
	openPage(browser, reddit)
	openPage(browser, youtube)
	openPage(browser, bbc)

	print "Entering details..."
	usernameElement = browser.find_element_by_id("session_key-login")
	usernameElement.send_keys(args.username)
	passwordElement = browser.find_element_by_id("session_password-login")
	passwordElement.send_keys(args.password)
	print "Submitting details..."
	#passwordElement.submit()

	bot()

if __name__ == "__main__":
	main()