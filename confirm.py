#! C:\xampp\python\python.exe

import cgi
from headTail import headHtml
from headTail import tailHtml
from forms import confirmForm
from forms import rsvpInput
from dbAccess import addNewGuest
from dbAccess import getAllowed
from forms import rsvpForm


def main():
    headHtml()
    inviteeId, guestsnm, fname, lname, email, food, submit = rsvpInput()
    status = addNewGuest(inviteeId, fname, lname, email, food)
    if status == 0:
        rsvp, party = getAllowed(inviteeId)
        confirmForm(fname, food, rsvp, party)
    else:
        textmessage = '<h5>The invitee email is already registered,<br> ' \
                      'make sure you use a different email address for this guest.</h5>'
        rsvpForm(guestsnm, inviteeId, textmessage)
    tailHtml()
    return


if __name__ == "__main__":
    try:
        main()
    except:
        cgi.print_exception()
