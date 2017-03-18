#! python

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# me == my email address
# you == recipient's email address
me = "recipe.send.scraper@gmail.com"
you = "marissakawinski@gmail.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "This Week's Recipes" # eventually will be "Recipes for the Week of <Sunday of starting week>"
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
#text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"
html = """\
<html>
  <head></head>
  <body>
  	<h1> Chicken Taco Soup </h1>
  	<img src="http://images.media-allrecipes.com/userphotos/560x315/3706561.jpg" style="zoom:50%">
  	<p>
  		<b>Calories per serving:</b> 434 
  		<br>
  		<b>Cook time:</b> 7h 35m
  		<br><br>
  		<em>Original recipe yields 4 servings</em>
  	</p>

  	<h3>Ingredients</h3>
  	<ul>
  		<li>1 onion, chopped</li>
  		<li>1 (16 ounce) can chili beans</li>
        <li>1 (15 ounce) can black beans</li>
        <li>1 (15 ounce) can whole kernel corn, drained</li>
        <li>1 (8 ounce) can tomato sauce</li>
        <li>1 (12 fluid ounce) can or bottle beer</li>
        <li>2 (10 ounce) cans diced tomatoes with green chilies, undrained</li>
        <li>1 (1.25 ounce) package taco seasoning</li>
        <li>3 whole skinless, boneless chicken breasts</li>
        <li>1 (8 ounce) package shredded Cheddar cheese (optional)</li>
        <li>sour cream (optional)</li>
        <li>crushed tortilla chips (optional)</li>
    </ul>

   	<h3>Directions</h3>
   	<ol>
   		<li>Place the onion, chili beans, black beans, corn, tomato sauce, beer, and diced tomatoes in a slow cooker. 
   			<br>Add taco seasoning, and stir to blend. Lay chicken breasts on top of the mixture, pressing down slightly until just covered by the other ingredients. 
   			<br>Set slow cooker for low heat, cover, and cook for 5 hours. </li>
   		</li>
   		<li> Remove chicken breasts from the soup, and allow to cool long enough to be handled. Stir the shredded chicken back into the soup, and continue cooking for 2 hours. 
   			<br>Serve topped with shredded Cheddar cheese, a dollop of sour cream, and crushed tortilla chips, if desired.
   		</li>
   	</ol>
  </body>
</html>
"""

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