"""
Open browser and sign in 

open file and read first track

search for the track

add it to the playlist

successful ? read next track : write track details to the failed file
"""

import argparse
import urlparse
import re
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup

def searchSpotify(list):
	time.sleep(5)
	browser.find_element_by_id('nav-search').click()
	for track in list:
		time.sleep(5)
		iframe = browser.find_element_by_id('suggest')
		print iframe
		searchBox = browser.find_elements_by_tag_name('input')
		for item in searchBox:
			print item
		searchBox[2].send_keys(track[0])
		searchBox.submit()


	#iframe = driver.find_elements_by_tag_name('iframe')[0]
	#driver.switch_to_default_content()

	#driver.switch_to_frame(iframe)
	#driver.find_elements_by_tag_name('iframe')[0]
	#browser.find_element_by_css_selector('a#nav-search.spoticon-search-32.standard-menu-item').click()

	#a#nav-search.spoticon-search-32.standard-menu-item
	#input.form-control.focus
def parseTracks(tracks):
	#Split the track list up into lines
	test = tracks.split("\n")
	print test[1]
	#Split lines up into the track, artist, album
	trackNames = [track.split(r',', 2) for track in test]
	for i in trackNames:
		for j in range(0, 3):
			i[j] = i[j][1:-1]
	print trackNames[1]

	# trackDetails = [re.split(r'\n', tracks)]
	# string = ''.join(trackDetails[0])

	# splitted = str(trackDetails[0]).split(',', 1)
	# splitter = splitted.split(',', 1)
	# print splitter
	# print type(trackDetails)
	# trackDetails = [re.sub(r'\n', lol, track) for track in trackDetails]

	return trackNames

def openSpotify():
	print "[+] Parsing details..."
	parser = argparse.ArgumentParser()
	parser.add_argument("username", help = "Username")
	parser.add_argument("password", help = "Password")
	args = parser.parse_args()

	print "[+] Opening Firefox..."
	global browser 
	browser = webdriver.Firefox()
	browser.get('https://play.spotify.com/')

	loginLink = browser.find_element_by_partial_link_text("Already").click()
	#loginLink = browser.find_element_by_xpath("//a[@id='has-account']")

	usernameElement = browser.find_element_by_id('login-usr')
	usernameElement.send_keys(args.username)
	passwordElement = browser.find_element_by_id('login-pass')
	passwordElement.send_keys(args.password)
	print "[+] Submitting details..."
	passwordElement.submit()

	print "[+] Logged in"

def main():

	openSpotify()

	print "[+] Opening track files..."
	tracks = open('tracks.txt', 'r')
	tracks = tracks.read()
	failed = open('fails', 'w')

	parsedList = parseTracks(tracks)

	searchSpotify(parsedList)


if __name__ == "__main__":
	main()