import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    user_name = "megacoursepyt@gmail.com"
    app_password = "ywhckdgfhqhhspko"     # it's better to use Environment Variables
    receiver = "khamvgdev@gmail.com"
    my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(user_name, app_password)
        server.sendmail(user_name, receiver, message)


