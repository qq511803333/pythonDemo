#!/usr/bin/env python3
# coding: utf-8
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

sender = '931162311@qq.com'
receiver = '511803333@qq.com'
password = 'jkghxvnhtjlpbcag'
smtp_server = 'smtp.qq.com'  # 服务器

# text
msg = MIMEText('你好', 'plain', 'utf-8')  # 中文需参数‘utf-8’，单字节字符不需要
msg['From'] = "931162311@qq.com"
msg['To'] = "511803333@qq.com"
# 标题
msg['Subject'] = Header("aaaa", "utf-8").encode()


server = smtplib.SMTP_SSL(smtp_server, 465)  # smtp模式和接口
server.set_debuglevel(1)
print(server.login(sender, password))
server.login(sender, password)
server.sendmail(sender, receiver, msg.as_string())
server.quit()
server.close()
