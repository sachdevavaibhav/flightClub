from twilio.rest import Client
import smtplib


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = "Twillio SID HERE"
        self.auth_token = "Twillio AUTH TOKEN"
        self.MY_EMAIL = "SENDERS EMAIL ADDRESS"
        self.MY_PASSWORD = "EMAIL PASSWORD HERE"

    def send_sms_notification(self, message):
        client = Client(self.account_sid, self.auth_token)

        message_to_send = client.messages.create(
            body=message,
            from_='+12405585615',
            to='TWILLIO REGISTERED NUMBER'
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



