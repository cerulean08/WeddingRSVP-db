#! C:\xampp\python\python.exe

import cgi
from dbAccess import calcFood
import logging
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


def loginForm(textmessage):
    print('''
    <h3 style ="color: #5B7F64;"> Welcome! </h3>
    <h3> Please enter your invitee email address </h3>
    <form action="main.py" method="get">
    <label for="email">Email</label>
    <input type="email" id="email" name="email" placeholder="Your email address"><br><br>
    {}
    <br><input type="submit" value="Submit"></form>
    '''.format(textmessage))


def loginInput():
    f = cgi.FieldStorage()
    email = f.getvalue('email', default='')
    # submit = f.getvalue('submit', default='')
    return email


def welcomeText():
    print('''
        <h3 style ="color: #5B7F64;"> You are cordially invited to our Wedding </h3>
        ''')


def rsvpForm(guestnm, inviteeId, textmessage):
    #  if guestnm == None:
    #      print('''Guest of ''')
    print('''<form action="confirm.py" method="get">
        <h3 style ="color: #5B7F64;"> {} and Guest(s)</h3>
    <h4>Kindly enter your name and select a food option</h4>
    <h5><br></h5>
    <fieldset><legend>Guest Info:</legend>
    <input type="hidden" name="guestsnm" value="{}" />
    <input type="hidden" name="inviteeId" value="{}" />
    <label for="fname">First Name</label>
    <input type="text" id="fname" name="fname" placeholder="first name"><br><br>
    <label for="lname">Last Name</label>
    <input type="text" id="lname" name="lname" placeholder="last name"><br><br>
    <label for="email">Email</label>
    <input type="email" id="email" name="email" placeholder="Your email address"><br><br>
    <label for="text">Food Option</label><br>
    <input type="radio" id="chicken" name="food" value="chicken">
    <label for="chicken"> Slow Roasted Chicken thighs with fingerling potatoes</label><br>
    <input type="radio" id="fish" name="food" value="fish">
    <label for="fish"> Chilean Sea bass and Risotto</label><br>
    <input type="radio" id="veg" name="food" value="veg">
    <label for="veg"> (Vegan) Roasted Mushroom and garlic gnocchi</label><br>
    <input type="radio" id="kids" name="food" value="kids">
    <label for="kids"> Kids option: Pizza </label><br><br>
    <br><input type="submit" value="Submit"></div>
    </fieldset></form>'''.format(guestnm, guestnm, inviteeId))
#   <label for="message">How many guests in your party?</label>
#   <input type="text" id="party" name="party" placeholder="how many guests?"><br><br>


def rsvpInput():
    f = cgi.FieldStorage()
    inviteeId = f.getvalue('inviteeId', default='')
    guestsnm = f.getvalue('guestsnm', default='')
    fname = f.getvalue('fname', default='')
    lname = f.getvalue('lname', default='')
    email = f.getvalue('email', default='')
    food = f.getvalue('food', default='')
    submit = f.getvalue('submit', default='')
    return inviteeId, guestsnm, fname, lname, email, food, submit


def confirmForm(fname, food, rsvp, party):
    print('''<h3>{}, your food choice of {} has been recorded.<br>
        <hr>
        Thank you!</h3><br>'''.format(fname, food))
    remaining = party - rsvp
    if remaining > 0:
        print('''
            <h4> You can add another {} guests to your party, are you ready to do that now?</h4>
            <input type="submit" onclick="window.location.href='main.py';" value="Yes"/>    
            <input type="submit" onclick="window.location.href='done.py';" value="Done"/> 
            '''.format(remaining))
    else:
        print("<h4>Your party is completely RSVP'd. Thank You!</h4><br>")
        print('''<input type="submit" onclick="window.location.href='done.py';" value="Done"/> ''')


def doneForm():
    print('''<div class=donetext><h3>Thank you! 
    <br> You can find our registry, gallery, and wedding day info here.</h3><br>
     <img src="nathan-dumlao-rV9fZwhE1ak-unsplash.jpg"></div>
     ''')


def coupleData():
    totalFood = calcFood()
    totalGuests = 0
    totalCost = 0
    print('''
        <fieldset><legend>Wedding Food: </legend>
        <section class="foodtable"><h3>Total RSVPs to-date</h3> </section>
        <table class="table">
        <thead>
        <tr>
          <th>Food Choice</th>
          <th>Count</th>
          <th>Cost</th>
        </tr>
     </thead><tbody>''')
    for row in totalFood:
        print(" <tr><td>{}</td><td> {} </td><td>${}</td></tr> ".format(row[0], row[2], row[3]))
        if row[2] != None:
            totalGuests = totalGuests + row[2]
        if row[3] != None:
            totalCost = totalCost + row[3]
    print('''
        <tr><td>Total </td><td>{}</td><td>${}</td></tr>'''.format(totalGuests, totalCost))
    print('''
        </tbody>
        </table>
        </fieldset>''')
