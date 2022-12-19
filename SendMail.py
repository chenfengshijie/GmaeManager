import smtplib
from email.mime.text import MIMEText
import json


class Email:
    def __init__(self, email, password, host):
        self.email = email
        self.password = password
        self.mail_host = host

    def send_email(self, info, sender, receivers):
        content = json.dumps(info)
        message = MIMEText(content, "plain", "utf-8")
        message["Subject"] = "GameManager INFO"
        message["From"] = self.email
        message["To"] = receivers[0]
        try:
            smtp_Obj = smtplib.SMTP()
            smtp_Obj.connect(self.mail_host, 25)
            smtp_Obj.login(self.email, self.password)
            smtp_Obj.sendmail(sender, receivers, message.as_string())
        except smtplib.SMTPException as e:
            print("error :{}".format(e))


if __name__ == "__main__":
    # 已经经过测试，能够成功发送邮件
    test = Email("13359701229@163.com", "VTJHAZWHAVWWDVXL", "smtp.163.com")
    info = {"message": "test send mail", "security": "yes"}
    test.send_email(info, "13359701229@163.com", "495964337@qq.com")


