import time, pyautogui
import PySimpleGUI as sg
import multiprocessing


def KeepWake():
    sg.theme('DarkAmber')

    layout = [
        [sg.Text('Program for putting computer in non sleep mode.\n'
                 'Window can be minimized.\n'
                 'To close either click Exit or terminate window.')],
        [sg.Text('Run program?', key='_OUTPUT_')],
        [sg.Button('Execute', button_color=('white', 'springgreen4'), key='_Execute_', visible=True), sg.Exit(button_color=('white', 'firebrick3'))],

    ]

    window = sg.Window('Windows Standby', layout)

    p2 = multiprocessing.Process(target=disturb)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit':
            if p2.is_alive():
                p2.terminate()
            break

        elif event == '_Execute_':
            p2.start()
            str = 'Running'
            window['_OUTPUT_'].update(str + '....')
            window['_Execute_'].update(visible=False)

    window.close()

def disturb():
    while True:
        pyautogui.press('volumedown')
        time.sleep(1)
        pyautogui.press('volumeup')
        time.sleep(300)

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=KeepWake)
    p1.start()