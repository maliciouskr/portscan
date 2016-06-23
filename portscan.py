import socket
def getbanner(ip,port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner
    except:
        return
#def checkVulns(banner):

def main():
    portlist = [21,22,25,80,443,1433,3306,8080,3389]
    for x in range(1,255):
        ip = '192.168.1.'+ str(x)
        for port in portlist:
            banner = getbanner(ip,port)
            if banner:
                print '[+]' + ip + '[' +str(port)+ ']'+':' +banner

if __name__ == '__main__':
    main()
