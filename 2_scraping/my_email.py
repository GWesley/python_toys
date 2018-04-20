import smtplib
from email.mime.text import MIMEText
import json

def sendMail(subject, body):
    with open('/Users/gwesley/Projects/config.cic.json', 'r') as f:
        config = json.loads(f.read()).get('mail_info')

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = config.get('from')
        msg['To'] = config.get('to')
        pwd = config.get('password')
        s = smtplib.SMTP_SSL(config.get('hostname'),465)
        s.set_debuglevel(1)
        s.login(msg['From'],pwd)
        s.send_message(msg)
        s.quit()

sendMail("小瘦仔发来一条提醒", "移民状态更新啦！ 打开看看吧： http://qq.com ")    
