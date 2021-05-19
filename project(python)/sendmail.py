import smtplib
server=smtplib.SMTP('smtp.gmail.com',535)
server.starttls()
server.login('prasanta1332001@gmail.com','Prasanta123@')
server.sendmail(
    'prasanta1332001@gmail.com',
    'priya2018.nalanda@gmail.com',
    'Hey Whats UP???'
)