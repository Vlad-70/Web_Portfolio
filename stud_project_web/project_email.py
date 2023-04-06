import smtplib, ssl


def project_email(message):
    host = "smtp.gmail.com"
    port = 465

    gmail_user = "megacoursepyt@gmail.com"
    gmail_password = "ywhckdgfhqhhspko"

    receiver = "khamvgdev@gmail.com"
    ssl_context = ssl.create_default_context()

    server = smtplib.SMTP_SSL(host, port, context=ssl_context)
    server.login(gmail_user, gmail_password)
    server.sendmail(gmail_user, receiver, message)
