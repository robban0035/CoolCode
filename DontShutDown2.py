import time, pyautogui
import PySimpleGUI as sg
import multiprocessing


def KeepWindowAlive():
    while True:
        pyautogui.press('volumedown')
        time.sleep(1)
        pyautogui.press('volumeup')
        time.sleep(100)


def main_program():
    p1 = multiprocessing.Process(target=main)
    p1.start()

def create_running_window():
    sg.theme('DarkAmber')

    layout = [  [sg.Text('Program is running', font='Any 15')],
                [sg.B('Quit', button_color=('white', 'firebrick3'))]   ]

    window = sg.Window('DontShutDown', layout, keep_on_top=True)

    return window

def create_main_window():
    sg.theme('DarkAmber')

    layout = [ [sg.Text('Running program enable computer not to sleep.', font='Any 12')],
               [sg.B('Execute', button_color=('white', 'springgreen4'))],
               [sg.B('Exit', button_color=('White', 'firebrick3'))]]


    return sg.Window('DuntShutDown', layout)

def main():
    window = None

    p2 = multiprocessing.Process(target=KeepWindowAlive)

    while True:
        if window is None:
            window = create_main_window()

        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit':
            if p2.is_alive():
                p2.terminate()
            else:
                break

        if event == 'Execute':
            event, values = create_running_window().read(close=True)
            main_program()
            p2.start()
            if event == 'Quit':
                window.quit()
                window = None
                break

    window.close()

main()
