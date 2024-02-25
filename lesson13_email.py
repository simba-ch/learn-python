from email import encoders
from email.parser import Parser
from email.header import Header,decode_header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
import smtplib
import poplib

def _format_addr(s):
  name,addr = parseaddr(s)
  return formataddr((Header(name,'utf-8').encode(),addr))

def sendEmail():
  from_addr = input('From: ')
  password = input('Password: ')
  to_addr = input('To')
  smtp_server = input('SMTP server: ')

  msg = MIMEText('hello,send by Python...','plain','utf-8')
  msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
  msg['To'] = _format_addr('管理员 <%s>' % to_addr)
  msg['Subject'] = Header('来自SMTP的问候。。。','utf-8').encode()

  server = smtplib.SMTP(smtp_server,25)
  server.set_debuglevel(1)
  server.login(from_addr,password)
  server.sendmail(from_addr,[to_addr],msg.as_string())
  server.quit()


def receiveEmail():
  email = input('Email: ')
  password = input('Password: ')
  pop3_server = input('POP3 server')

  server = poplib.POP3(pop3_server)
  server.set_debuglevel(1)
  print(server.getwelcome().decode('utf-8'))

  server.user(email)
  server.pass_(password)

  print('Messages: %s. Size: %s' % server.stat())
  resp,mails,octets = server.list()

  print(mails)

  index = len(mails)
  resp,lines,octets = server.retr(index)

  msg_content = b'\r\n'.join(lines).decode('utf-8')

  msg = Parser().parsestr(msg_content)
  print(msg)
  server.quit()


