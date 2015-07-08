#Password cracker
import optparse
import crypt

def testPass(cryptPass, dname):
	salt = cryptPass[0:2]
	dictFile = open(dname, "r")
	for word in dictFile.readlines():
		word = word.strip("\n")
		cryptWord = crypt.crypt(word, salt)
		if(cryptWord == cryptPass):
			print "[+] Found Password! - " + word + "\n"
			return

	print "[-] Password not found. \n"
	return

def main():
	passFile = open("passwords.txt", "r")
	for line in passFile.readlines():
		if ":" in line:
			user = line.split(":")[0]
			cryptPass = line.split(":")[1].strip(" ")
			print "[*] Cracking password for: " + user
			testPass(cryptPass, "dictionary.txt")
			
if __name__ == "__main__":
	main()	
