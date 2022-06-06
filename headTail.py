#! C:\xampp\python\python.exe


def headHtml():
    print("Content_type: 'text/html'\n\n")
    print("<html><head>")
    # print("<style>*{background-color: #F1D0BD;}</style>")
    print('''<style>
            @import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');
            body{
                font-family: 'Montserrat', sans-serif;
                margin: 5%;
                background-color: #F1D0BD
            }
            *{
                box-sizing: border-box;
            }
            header {
                height: 300px;
                
                background-color: #145952;
                background: #FFFBF6 url(wedBanner.png);
                background-size: contain;
                background-position: center top;
                background-repeat:no-repeat;
                margin: 0;
            }
            h3 {
                color: #5B7F64;
                text-align: center;
                font-size: x-large;
                font-weight: 900;
            }
            h4 {
                color: #DB7E51;
                text-align: center;
                font-family: 'Montserrat', sans-serif;
            }
            h5 {
                color: #535644;
                text-align: center;
                font-family: 'Montserrat', sans-serif;
            }
            hr {
                max-width: 25%;
                border: 0;
                height: 1px;
                background-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0));
            }
            img {
                max-width:25%;
                border: 10px solid white;
                box-shadow: 0 10px 9px rgba(0,0,0,0.35);
            }
            .donetext {
                text-align:center;
            }
            .form-child {
                background-color: #A69C80;
                width: 96%;
                margin: 0 2% 10%;
                color: #145952;
            }
            input[type=text], input[type=email], select, textarea {
                color: #145952;
                width: 100%;
                padding: 12px;
                border: 1px solid #ccc;
                border-radius: 4px;
                resize: vertical;
                box-shadow: 0 10px 9px rgba(0,0,0,0.35);
              }
            label {
                padding: 12px 12px 12px 0;
                display: inline-block;
            }
            .form-text{
                background-color: #fff;
                color: #145952;
                font-family: 'Montserrat', sans-serif;
                text-align: center;
                font-weight: 400;
                border-radius: 4px;
                width: 82%;
                margin: 4rem 8%;
                padding: 2rem 6%;
                border: 1%;
                box-shadow: 0 10px 9px rgba(0,0,0,0.35);
            }
            input[type=submit] {
                background-color: #5B7F64;
                color: #F2E9BD;
                padding: 12px 20px;
                font-size: 16px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                float: center;
            }  
            input[type=submit]:hover {
                box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
            }
            .table{
                margin: 2%;
                box-shadow: 0 10px 9px rgba(0,0,0,0.35);
                text-align: center;
                margin-left: auto;
                margin-right: auto;
            }
            
            th {
                background-color: #8C423B;
                /*border-radius: 10px;*/
                color: #F2E9BD;
                font-family: 'Cormorant', serif;
                font-size: larger;
            }
            
            th, td {
                padding: 10px;
                text-align: left;
                border-bottom: 1px solid #145952;
            }
            td{
                color: #145952;
                background-color: #9FB9B1;
                font-size: small;
            }
            
            footer{
                margin-top: 35%;
                padding-bottom: 2rem;
                padding:2%;
                text-align: center;
                background-color: #145952;
                font-size: smaller;
            }
            </style>''')
    print("</head><body><header></header>")


def tailHtml():
    print('''<footer>
            <h5 style ="color: #F2E9BD"> CS275/Final Part 4  -  by Christina Mullen</h5>
            ''')
    print("</footer></body></html>")

