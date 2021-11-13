from panes import *
from settings import *


class TUI:
    def __init__(self, nickname) -> None:
        self.stdscr = curses.initscr()
        self.lines = curses.LINES
        self.cols = curses.COLS

        self.check_terminal_size()

        command_pane_size_y = command_pane_height
        status_pane_size_y = self.lines - command_pane_size_y
        message_pane_size_y = message_pane_height
        log_pane_size_y = self.lines - (command_pane_size_y + message_pane_size_y)

        command_pane_size_x = self.cols
        status_pane_size_x = status_pane_length
        message_pane_size_x = self.cols - status_pane_size_x
        log_pane_size_x = self.cols - status_pane_size_x

        command_pane_pos_y = status_pane_size_y
        status_pane_pos_y = 0
        message_pane_pos_y = log_pane_size_y
        log_pane_pos_y = 0

        command_pane_pos_x = 0
        status_pane_pos_x = 0
        message_pane_pos_x = status_pane_length
        log_pane_pos_x = status_pane_length

        self.status_pane = StatusPane(status_pane_size_y, status_pane_size_x, status_pane_pos_y, status_pane_pos_x)
        self.log_pane = LogPane(log_pane_size_y, log_pane_size_x, log_pane_pos_y, log_pane_pos_x)
        self.command_pane = CommandPane(command_pane_size_y, command_pane_size_x, command_pane_pos_y,
                                        command_pane_pos_x)
        self.message_pane = MessagePane(message_pane_size_y, message_pane_size_x, message_pane_pos_y,
                                        message_pane_pos_x)
        if len(nickname) < min_nickname_length:
            self.nickname = nickname

    def check_terminal_size(self) -> None:
        if self.cols < min_cols or self.lines < min_lines:
            raise SystemExit("Error: Terminal size must be equal or more than 110x15. Terminating program")

    @staticmethod
    def sleep(seconds):
        curses.napms(seconds * 1000)
