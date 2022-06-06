#! C:\xampp\python\python.exe

import cgi
from headTail import headHtml
from headTail import tailHtml
from forms import coupleData


def main():
    headHtml()
    coupleData()
    tailHtml()
    return


if __name__ == "__main__":
    try:
        main()
    except:
        cgi.print_exception()
