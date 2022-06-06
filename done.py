#! C:\xampp\python\python.exe

import cgi
from headTail import headHtml
from headTail import tailHtml
from forms import doneForm
from dbAccess import calcFood


def main():
    headHtml()
    doneForm()
    calcFood()
    tailHtml()
    return


if __name__ == "__main__":
    try:
        main()
    except:
        cgi.print_exception()
