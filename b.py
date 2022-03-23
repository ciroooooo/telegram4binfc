from asyncio.windows_events import NULL
import PySimpleGUI as sg
import cv2
import telegram
import time
sg.theme('LightGray2')   
layout1=[[sg.Button('Testo',key='Testo'),sg.FileBrowse('Immagine',target='Immagine',file_types=(("JPEG","*.JPG"),("PNG","*.png")),key='Immagine')]]  
layout=[    [sg.Text('Invia il tuo messaggio:',font=('Sans-Serif',10,'bold'))],
            [sg.Multiline(default_text='messaggio...',size=(80,10),no_scrollbar=True,)],
            [sg.Input('Immagine',key='Immagine', enable_events=True,visible=False)],
            [sg.Column(layout1,expand_x=True, element_justification='center')] ]
token="5171787115:AAENVAKU4aur9xItmvATYupcjX6o1FI2J84"
user_id="-726798912"
# Create the Window
window = sg.Window('TelePonti', layout,icon=r'icona.ico')

bot= telegram.Bot(token=token)
path='Immagine'
def telegram(values):
    try:
        bot.send_message(chat_id=user_id, text=values)
        sg.popup_quick_message('MESSAGGIO INVIATO CORRETTAMENTE')
    except Exception as ex:
        sg.Popup('INSERIRE UNA FRASE',title='ERRORE',icon=r'icona.ico')
    time.sleep(0.2)

def telegram_foto(path):
    try:
        bot.send_photo(chat_id=user_id, photo=open(path, 'rb'))
        sg.popup_quick_message('IMMAGINE INVIATA CORRETTAMENTE')
        window['Immagine'].update("")
    except Exception as ex:
        sg.Popup('INSERIRE UN IMMAGINE',title='ERRORE',icon=r'icona.ico')   
    
    time.sleep(0.2)


# Event Loop to process "events" and get the "values" of the inputs
while True:
    event,values = window.read()
    print(values)
    path=values['Immagine']
    if event=='Testo':
        telegram(values[0])
    if event=='Immagine':
        telegram_foto(path)
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    
    
    

window.close()