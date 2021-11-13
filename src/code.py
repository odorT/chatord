import curses

from tui import TUI
import time

tui = TUI("kamran")

while True:
    # online_users = [['Kamran', 'Isi', 'Elza'], ['Kamran', "Isi"], ['Elza', 'Rustam', 'Isi'], ['Nobody']]
    # logs = ['Program started with PID 1123', 'Trying to connect to server', 'Connected to server at localhost:30000',
    #         'Message from server: Hi kamran, welcome to chatord']
    #
    # time.sleep(1)
    # tui.status_pane.stdout(online_users[0])
    #
    # time.sleep(2)
    # tui.log_pane.stdout(logs[0])
    #
    # time.sleep(1)
    # tui.log_pane.stdout(logs[1])
    #
    # time.sleep(1)
    # tui.log_pane.stdout(logs[2])
    #
    # time.sleep(1)
    # tui.status_pane.stdout(online_users[1])
    #
    # time.sleep(1)
    # tui.status_pane.stdout(online_users[2])
    #
    # time.sleep(1)
    # tui.log_pane.stdout(logs[3])
    #
    # time.sleep(1)
    # tui.status_pane.stdout(online_users[3])
    #
    # tui.status_pane.stdout('hi')
    # tui.log_pane.stdout('hi')
    #
    # tui.sleep(3)
    # tui.log_pane.stdout()
    # tui.status_pane.stdout()

    text = tui.command_pane.stdin()
    tui.log_pane.stdout(message=text)
    tui.log_pane.stdout(tui.command_pane.max_textsize)
    tui.sleep(3)
    break
