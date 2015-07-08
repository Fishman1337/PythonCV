#PortScanner
import optparse
from socket import *
from threading import *

screenLock = Semaphore(value = 1)

def connectionScan(targetHost, targetPort):
	try:
		connectionSkt = socket(AF_INET, SOCK_STREAM)
		connectionSkt.connect((targetHost, targetPort))

		connectionSkt.send("Hello!\r\n")

		results = connectionSkt.recv(100)
		screenLock.acquire()
		print "[+] " + str(targetPort) + "/tcp open"
	except:
		screenLock.acquire()
		print "[-] " + str(targetPort) + "/tcp closed"
	finally:
		screenLock.release()
		connectionSkt.close()

def portScan(targetHost, targetPorts):
	try:
		targetIP = gethostbyname(targetHost)
	except:
		print "[-] Cannot resolve " + targetHost + ": Unknown host"
		return
	
	try:
		targetName = gethostbyaddress(targetIP)
		print "\n[+] Scan results for: " + targetName[0]
	except:
		print "\n[+] Scan results for: " + targetIP

	setdefaulttimeout(1)
	for targetPort in targetPorts:
		t = Thread(target = connectionScan, args = (targetHost, int(targetPort)))
		t.start()

def main():
	#Handle input strings - take the -H (host IP), -p (Port number) and assign them to variables.
	parser = optparse.OptionParser("usage %prog -H <target host> " + \
		"-p <target port>")
	parser.add_option("-H", dest = "targetHost", type = "string", \
		help = "specify target host")
	parser.add_option("-p", dest = "targetPort", type = "string", \
		help = "specify target port[s] seperated by comma, seperate ranges with a '-'")
	(options, args) = parser.parse_args()
	if(options.targetHost == None) | (options.targetPort == None):
		print parser.usage
		exit(0)
	else:
		targetHost = options.targetHost
		if "-" in str(options.targetPort):
			targetPorts = options.targetPort.split("-")
			targetPorts = range(int(targetPorts[0]), int(targetPorts[1]))
		else:
			targetPorts = str(options.targetPort).split(",") 

	portScan(targetHost, targetPorts)

if __name__ == "__main__":
	main()