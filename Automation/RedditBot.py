#Simple Reddit bot
import argparse
import urlparse

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup

def main():

	print "Selecting details..."
	parser = argparse.ArgumentParser()
	parser.add_argument("username", help = "reddit username")
	parser.add_argument("password", help = "reddit password")
	args = parser.parse_args()

	browser = webdriver.Firefox()
	browser.get("https://www.reddit.com/login")

	print "Entering details..."
	usernameElement = browser.find_element_by_id("user_login")
	usernameElement.send_keys(args.username)
	passwordElement = browser.find_element_by_id("passwd_login")
	passwordElement.send_keys(args.password)
	print "Submitting..."
	passwordElement.submit()

	print "[+] Success! Logged in, bot would start here.."




if __name__ == "__main__":
	main()