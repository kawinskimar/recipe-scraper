#! python

import smtplib, os, glob

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# me == my email address
# you == recipient's email address
me = "recipe.send.scraper@gmail.com"
you = "marissakawinski@gmail.com"
html = ''

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "This Week's Recipes" # eventually will be "Recipes for the Week of <Sunday of starting week>"
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
#text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"

os.chdir('../recipe_files')
for file in glob.glob('*.html'):
    msg['Subject'] = os.path.splitext(file)[0]
    rec_file = open(file, 'rw+')os.chdir('../recipe_files')
    html = rec_file.read()
    rec_file.close()

    # Record the MIME types of both parts - text/plain and text/html.
    #part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    #msg.attach(part1)
    msg.attach(part2)

    # Send the message via local SMTP server.
    s = smtplib.SMTP('smtp.gmail.com:587')
    s.ehlo()
    s.starttls()
    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    s.login('recipe.send.scraper@gmail.com', 'Scraper123')
    s.sendmail(me, you, msg.as_string())
    s.quit()
