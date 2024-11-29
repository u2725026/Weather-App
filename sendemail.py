import smtplib, os
from dotenv import load_dotenv

load_dotenv()


class SendEmail:
    def __init__(self):
        self.email = os.getenv("MY_EMAIL")
        self.password = os.getenv("PASS")

        print(self.email, self.password)

    def sendmail(self, city, description):
        con = smtplib.SMTP("smtp.gmail.com", 587)
        con.starttls()
        con.login(self.email, self.password)
        con.sendmail(
            from_addr=self.email,
            to_addrs="subedisaroj09@gmail.com",
            msg=f"Subject: Extreme Weather Notification\n\n {city} has {description} suggest your close ones to be careful",
        )
