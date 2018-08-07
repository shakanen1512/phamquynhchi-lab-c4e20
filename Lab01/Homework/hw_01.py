from gmail import GMail, Message
gmail = GMail("chiphamfls@gmail.com", "jessemac")

html_content = """
<p>Hey,</p>
<p>Our <span style="color: #ff0000;"><strong>"{{tour_name}}"</strong></span> has just been released!</p>
<p>Check it out on our website willerexpress.com.</p>
<p>For any questions, just email en-info@willer.co.jp</p>
"""

tour_name = [
    "Mt Fuji Climbing Tour",
    "Ghibli Museum Walking Tour",
    "Shibazakura Tour",
    "Flower Park Tour"
]

from random import choice
new_content = html_content.replace("{{tour_name}}", choice(tour_name))

from datetime import datetime
now = datetime.now()

count = 0
while count < 1:
    if now.hour == 7:
        msg = Message(
            "Shameless promotion for Willer Express", 
            to="chiphamfls@gmail.com", 
            html=new_content)
        gmail.send(msg)
    count += 1
    break