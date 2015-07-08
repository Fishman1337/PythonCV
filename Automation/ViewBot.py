#Simple LinkedIn view bot
#Parsing email and password, clear the console, timing the 
import argparse, os, time
#Parse the URL tags
import urlparse, random
#TODO: comment these.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


def getAccountLinks(page):
	accountLinks = []
	for link in page.find_all("a"):
		url = link.get("href")
		if url:
			if 'profile/view?id' in url:
				accountLinks.append(url)

	return accountLinks

def getJobLinks(page):
	jobLinks = []
	for link in page.find_all("a"):
		url = link.get("href")
		if url:
			if "/jobs" in url:
				links.append(url)

	return jobLinks

def getID(url):
	parseUrl = urlparse.urlparse(url)
	return urlparse.parse_qs(parseUrl.query)["id"][0]

def viewRobot(browser):
	visitedAccounts = {}
	plannedAccounts = []
	visitCount = 0
	
	while True:
		#Wait a random amount of time to load next page.
		print "Sleeping so we look human..."
		time.sleep(random.uniform(2, 4))
		print "Get page source & grab links..."
		page = BeautifulSoup(browser.page_source)
		accounts = getAccountLinks(page)
		if accounts:
			print "Accounts on page..."
			for account in accounts:
				ID = getID(account)
				if ID not in visitedAccounts:
					plannedAccounts.append(account)
					visitedAccounts[ID] = 1

		if plannedAccounts:
			print "Planned accounts..."
			person = plannedAccounts.pop()
			browser.get(person)
			visitCount += 1
		else:
			print "Looking for jobs..."
			jobs = getJobLinks(page)
			if jobs:
				job = random.choice(jobs)
				print "Found job: %s" % job
				rootURL = "http://www.linkedin.com"
				rootsURL = "http://www.linkedin.com"
				if rootURL not in job or rootURL not in job:
					job = "https://www.linkedin.com" + job
					browser.get(job)
			else:
				print "No jobs, exiting."
				break
		print "[+] " + browser.title + " Visited! \n" + str(visitCount) + "/" + str(len(plannedAccounts)) + " - Visited/Queue"


def main():
	print "Reading args..."
	parser = argparse.ArgumentParser()
	parser.add_argument("email", help = "linkedin email")
	parser.add_argument("password", help = "linkedin password")
	args = parser.parse_args()
	print "Got args, open FireFox..."
	browser = webdriver.Firefox()
	browser.get("https://linkedin.com/uas/login")
	print "Find elements & log in..."
	emailElement = browser.find_element_by_id("session_key-login")
	emailElement.send_keys(args.email)
	passElement = browser.find_element_by_id("session_password-login")
	passElement.send_keys(args.password)
	passElement.submit()
	os.system("cls")

	print "[+] Success! Logged in, bot starting..."

	viewRobot(browser)
	browser.close

if __name__ == "__main__":
	main()

