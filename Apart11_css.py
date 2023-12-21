########## Written by Mehrshad! ##########
exit_butt_light = '''QPushButton{
    background-color: red;
    border: 3px solid transparent;
    color:white;
    border-radius: 10px}
    QPushButton:hover{
    border: 3px solid red;}
    QPushButton:pressed{
    color:black;
	background-color: rgb(240, 240, 240);
    border: 3px solid red;}'''
# exit_butt_light = '''QPushButton{
#     background-color: qconicalgradient(cx:0.756, cy:1, angle:296.3, stop:0 rgba(255, 170, 170, 255), stop:0.931818 rgba(255, 45, 45, 255), stop:1 rgba(255, 255, 255, 255));
#     border: 1px solid black;
#     color:black;
#     border-radius: 10px}
#     QPushButton:hover{
#     color:white;}'''
exit_butt_dark = '''QPushButton{
    background-color: red;
    border: 3px solid transparent;
    color:white;
    border-radius: 10px}
    QPushButton:hover{
    border: 3px solid red;}
    QPushButton:pressed{
    color:white;
	background-color: rgb(53, 53, 53);
    border: 3px solid red;}'''
# exit_butt_dark = '''QPushButton{
#     background-color: qconicalgradient(cx:0.756, cy:1, angle:296.3, stop:0 rgba(255, 170, 170, 255), stop:0.931818 rgba(255, 45, 45, 255), stop:1 rgba(255, 255, 255, 255));
#     border: 1px solid transparent;
#     color:white;
#     border-radius: 10px}
#     QPushButton:hover{
#     color:black;}'''
label_light = 'background-color: transparent;color:black'
label_dark = 'background-color: transparent;color:white'
butt_main_light = '''QPushButton{
    background-color: rgb(240, 240, 240);
    border: 1px solid gray;
    color:black;
    border-radius: 10px}
    QPushButton:hover{
    color:rgb(27, 151, 243);
    border: 3px solid rgb(27, 151, 243);}
    QPushButton:pressed{
    color:white;
    background-color: rgb(27, 151, 243);}'''
butt_main_dark = '''QPushButton{
    background-color: rgb(53, 53, 53);
    border: 1px solid rgb(53, 53, 53);
    color:white;
    border-radius: 10px}
    QPushButton:hover{
    color:rgb(237, 255, 153);
    border: 3px solid rgb(237, 255, 153);}
    QPushButton:pressed{
    color:black;
    background-color: rgb(237, 255, 153);}'''
butt_transparent = 'background-color: transparent;'
background_light = 'background-color:rgba(225, 225, 225, 255);'
background_dark = 'background-color:rgba(30, 30, 30, 255);'
background_light_gradient = 'background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(225, 225, 225, 255));'
background_dark_gradient = 'background-color:qlineargradient(spread:pad, x1:1, y1:0.483, x2:0, y2:0.483, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(30, 30, 30, 255));'
background_start = '''QLabel{
    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(241, 255, 218, 255), stop:1 rgba(155, 255, 126, 255));
    text-align: center;
    border-radius: 10px;
    }'''
other_light = '''background-color: rgb(240, 240, 240);
    border: 1px solid rgb(240, 240, 240);
    color:black;
    border-radius: 10px'''
other_dark = '''background-color: rgb(53, 53, 53);
    border: 1px solid rgb(53, 53, 53);
    color:white;
    border-radius: 10px'''
butt_sabt_light = '''QPushButton{
    background-color: green;
    border: 3px solid transparent;
    color:white;
    border-radius: 10px}
    QPushButton:hover{
    border: 3px solid green;}
    QPushButton:pressed{
    color:black;
	background-color: rgb(240, 240, 240);
    border: 3px solid green;}'''
# butt_sabt_light = '''QPushButton{
#     background-color: qconicalgradient(cx:0.756, cy:1, angle:296.3, stop:0 rgba(170, 255, 255, 255), stop:0.931818 rgba(45, 255, 95, 255), stop:1 rgba(255, 255, 255, 255));
#     border: 1px solid black;
#     color:black;
#     border-radius: 10px}
#     QPushButton:hover{
#     color:white;}'''
butt_sabt_dark = '''QPushButton{
    background-color: green;
    border: 3px solid transparent;
    color:white;
    border-radius: 10px}
    QPushButton:hover{
    border: 3px solid green;}
    QPushButton:pressed{
    color:white;
	background-color: rgb(53, 53, 53);
    border: 3px solid green;}'''
# butt_sabt_dark = '''QPushButton{
#     background-color: qconicalgradient(cx:0.756, cy:1, angle:296.3, stop:0 rgba(170, 255, 255, 255), stop:0.931818 rgba(45, 255, 95, 255), stop:1 rgba(255, 255, 255, 255));
#     border: 1px solid transparent;
#     color:black;
#     border-radius: 10px}
#     QPushButton:hover{
#     color:white;}'''
line_light = '''QLineEdit{
    background-color: rgb(240, 240, 240);
    border: 1px solid rgb(240, 240, 240);
    color:black;
    border-radius: 10px;}
    QLineEdit:focus{
    border: 3px solid rgb(27, 151, 243);}'''
line_dark = '''QLineEdit{
    background-color: rgb(53, 53, 53);
    border: 1px solid rgb(53, 53, 53);
    color:white;
    border-radius: 10px;}
    QLineEdit:focus{
    border: 3px solid rgb(237, 255, 153);}'''
bar_light = '''QProgressBar{
        border: 1px solid transparent;
        text-align: center;
        color:rgba(0,0,0,100);
        border-radius: 10px;
        background-color: transparent;
        }
        QProgressBar::chunk{
        background-color: rgba(27, 151, 243,0.3);
        }'''
bar_dark = '''QProgressBar{
        border: 1px solid transparent;
        text-align: center;
        color:rgba(0,0,0,100);
        border-radius: 10px;
        background-color: transparent;
        }
        QProgressBar::chunk{
        background-color: rgba(237, 255, 153,0.3);
        }'''
bar_start = '''QProgressBar{
        border: 1px solid transparent;
        text-align: center;
        color:rgba(0,0,0,100);
        border-radius: 10px;
        background-color:rgba(255, 255, 255, 100)
        }
        QProgressBar::chunk{
        border-radius: 10px;
        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(155, 255, 200, 255), stop:1 rgba(27, 151, 243,255));
        }'''
