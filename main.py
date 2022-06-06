#! C:\xampp\python\python.exe

import cgi
from headTail import headHtml
from headTail import tailHtml

from forms import welcomeText
from dbAccess import getInvitee
from forms import loginForm
from forms import loginInput
from forms import doneForm
from forms import rsvpForm
from dbAccess import getAllowed


def main():
    headHtml()
    email = loginInput()
    guestsnm, inviteeId, party = getInvitee(email)
    if guestsnm != None:
        rsvp, party = getAllowed(inviteeId)
        if (party - rsvp) > 0:
            welcomeText()
            rsvpForm(guestsnm, inviteeId, "")
        else:
            doneForm()
    else:
        #  textmessage = '<h4>The email you entered is not found, check the spelling and try again.</h4><br>'
        textmessage = ' '
        loginForm(textmessage)
        #  rsvpForm(guestsnm, inviteeId, textmessage)
    tailHtml()


if __name__ == "__main__":
    try:
        main()
    except:
        cgi.print_exception()
