from twilio.rest import Client
import smtplib


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = "AC7bddcc90668267a0bd5682b627cd373c"
        self.auth_token = "d33c75ea19d0b653ed0af81179553a78"
        self.MY_EMAIL = "pythonpy09@gmail.com"
        self.MY_PASSWORD = "abcd1234()"

    def send_sms_notification(self, message):
        client = Client(self.account_sid, self.auth_token)

        message_to_send = client.messages.create(
            body=message,
            from_='+12405585615',
            to='+917015661467'
        )

        print(message_to_send.status)
        return None

    def send_email_notification(self, message, to_email_list, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.MY_EMAIL, password=self.MY_PASSWORD)
            for email in to_email_list:
                connection.sendmail(from_addr=self.MY_EMAIL,
                                    to_addrs=email,
                                    msg=f"Subject:New Low Price Flight! \n\n{message}\n"
                                        f"{google_flight_link}".encode("utf-8"))
                print("Sent")



