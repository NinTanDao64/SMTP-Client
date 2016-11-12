from socket import *
msg = '\r\n I love computer networks!'
endmsg = '\r\n.\r\n'
#Choose a mail server
mailServer = 'localhost'
mailPort = 25
#Create socket and establish TCP connection
SMTPClientSocket = socket(AF_INET,SOCK_STREAM)
SMTPClientSocket.connect((mailServer, mailPort))
recv = SMTPClientSocket.recv(1024)
print recv
if recv[:3] != '220' :
	print '220 reply not received from server.'

#Send HELLO command and print server response.
heloCommand = 'HELO gaia.ecs.csus.edu\r\n'
SMTPClientSocket.send(heloCommand)
recv1 = SMTPClientSocket.recv(1024)
print recv1
if recv1[:3] != '250' :
	print '250 reply not received from server.'

#Send MAIL FROM command and print server response.
mailfromCommand = 'MAIL FROM:<tandao@csus.edu>\r\n'
SMTPClientSocket.send(mailfromCommand)
recv2 = SMTPClientSocket.recv(1024)
print recv2
if recv2[:3] != '250' :
	print '250 reply not received from server.'

#Send RCPT TO command and print server response.
rcptToCommand = 'RCPT TO:<nintandao64@yahoo.com>\r\n'
SMTPClientSocket.send(rcptToCommand)
recv3 = SMTPClientSocket.recv(1024)
print recv3
if recv3[:3] != '250' :
	print '250 reply not received from server.'

#Send DATA command and print server resonse.
dataCommand = 'DATA\r\n'
SMTPClientSocket.send(dataCommand)
recv4 = SMTPClientSocket.recv(1024)
print recv4

SMTPClientSocket.send(msg)
SMTPClientSocket.send(endmsg)

#Send QUIT command and get server response.
quitCommand = 'QUIT\r\n'
SMTPClientSocket.send(quitCommand)
recv5 = SMTPClientSocket.recv(1024)
print recv5
