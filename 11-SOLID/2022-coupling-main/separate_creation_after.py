from email.message import Message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

DEFAULT_EMAIL = "support@arjancodes.com"
LOGIN = "test"
PASSWORD = "my_password"

#creation logic in seperate function, test using mock object
#change SMTP to protocol as it has limited same methods - connect, quit and so on
def create_mime_multipart(
    from_address: str,
    to_address: str | None = None,
    subject: str = "No subject",
    message: str = "",
) -> Message:
    msg = MIMEMultipart()
    msg["From"] = from_address
    msg["To"] = to_address
    msg["Subject"] = subject
    mime = MIMEText(
        message,
        "html" if message.lower().startswith("<!doctype html>") else "plain",
    )
    msg.attach(mime)
    return msg


class EmailClient:
    #pass smtp server instead of creating it here
    def __init__(
        self,
        smtp_server: SMTP,
        credentials: tuple[str, str] = (LOGIN, PASSWORD),
        name: str = "",
        to_address: str = DEFAULT_EMAIL,
    ):
        self._server = smtp_server
        host, port = str(smtp_server._host).split(":")  # type: ignore
        self._host = host
        self._port = int(port)
        self._login, self._password = credentials
        self.name = name
        self.to_address = to_address

    def _connect(self) -> None:
        self._server.connect(self._host, self._port)
        self._server.starttls()
        self._server.login(self._login, self._password)

    def _quit(self) -> None:
        self._server.quit()
    #use message as an argument here instead of creating it
    def send_message(self, msg: Message) -> None:
        if not msg["To"]:
            msg["To"] = self.to_address
        self._connect()
        self._server.sendmail(msg["From"], msg["To"], msg.as_string())
        self._quit()
