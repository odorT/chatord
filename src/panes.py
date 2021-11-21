import curses
import curses.ascii

from nltk import flatten


class Pane:
    def __init__(self, size_y, size_x, pos_y, pos_x) -> None:
        self.size_y = size_y
        self.size_x = size_x
        self.pos_y = pos_y
        self.pos_x = pos_x
        self.max_textsize = self.size_x - 2

        self.window = curses.newwin(self.size_y, self.size_x, self.pos_y, self.pos_x)
        self.window.border()
        self.refresh_window()
        self.window.keypad(True)
        # TODO: place config above to appropriate place

    def refresh_window(self):
        self.window.refresh()


class InputPane(Pane):
    def stdin(self):
        pass

    def show_text(self, text=''):
        pass

    def refresh_window(self):
        self.window.clear()
        self.window.border()
        self.show_text()
        self.window.refresh()


class OutputPane(Pane):
    def stdout(self, message=''):
        pass

    def refresh_window(self):
        self.window.refresh()
        self.window.clear()
        self.window.border()


class StatusPane(OutputPane):
    def __init__(self, size_y, size_x, pos_y, pos_x) -> None:
        super().__init__(size_y, size_x, pos_y, pos_x)

    def stdout(self, messages: list = ''):
        if not messages:
            pass

        self.window.clear()
        self.window.border()
        messages = list(map(lambda x: str(f' * {x}'), messages))

        for count, msg in enumerate(messages, start=1):
            if count < self.size_y - 1:
                self.window.addstr(count, 1, msg)

        self.refresh_window()


class LogPane(OutputPane):
    def __init__(self, size_y, size_x, pos_y, pos_x) -> None:
        super().__init__(size_y, size_x, pos_y, pos_x)
        self.messages = []
        self.last_messages = []

    def add_to_messages(self, message: str):
        message = str(f' >>> {message}')
        if len(message) > self.max_textsize:
            self.messages.append([message[x:x + self.max_textsize] for x in range(0, len(message), self.max_textsize)])
        else:
            self.messages.append(message)

        self.last_messages = flatten(self.messages)[-(self.size_y - 2):]

    def stdout(self, message: str = ''):
        if not message:
            pass

        self.refresh_window()
        self.add_to_messages(message)

        count = 1
        for msg in self.last_messages:
            if isinstance(msg, str):
                self.window.addstr(count, 1, msg)
                count += 1
            elif isinstance(msg, list):
                for i in msg:
                    self.window.addstr(count, 1, i)
                    count += 1

        self.refresh_window()

        return 0


class CommandPane(InputPane):
    # TODO: implement reverse command search, when up arrow pressed show previous commands

    def __init__(self, size_y, size_x, pos_y, pos_x) -> None:
        super().__init__(size_y, size_x, pos_y, pos_x)
        self.max_textsize = self.max_textsize - 1  # max_textsize will be less by the prompt size
        # TODO: apply the same technique above to all classes

    def show_text(self, text=''):
        text = f'$ {text}'
        self.window.addstr(1, 1, text)
        self.window.clrtoeol()

    def stdin(self):
        input_text = ''
        while True:
            self.show_text(input_text)
            char = self.window.get_wch()

            if isinstance(char, str) and char.isprintable():
                if len(input_text) + 1 < self.max_textsize:
                    input_text += char
                else:
                    continue
            elif char == '\x7f' or char == 263:  # backspace
                input_text = input_text[:-1]
            elif char == '\n':  # return
                self.refresh_window()
                return input_text
            else:
                raise AssertionError(char)


class MessagePane(InputPane):
    def __init__(self, size_y, size_x, pos_y, pos_x) -> None:
        super().__init__(size_y, size_x, pos_y, pos_x)

    def show_text(self, text=''):
        text = f'>> {text}'
        if len(text) < self.max_textsize:
            self.window.addstr(1, 1, text)
            self.window.clrtoeol()
        else:
            text = [text[x:x + self.max_textsize] for x in range(0, len(text), self.max_textsize)]
            for line_count, text_slice in enumerate(text, start=1):
                if line_count < self.size_y - 1:
                    self.window.addstr(line_count, 1, text_slice)

    def stdin(self):
        input_text = ''
        while True:
            self.show_text(input_text)
            char = self.window.get_wch()

            if isinstance(input_text, str) and char.isprintable():
                input_text += char
            elif char == '\x7f' or char == 263:  # backspace
                input_text = input_text[:-1]
            elif char == '\n':  # return
                self.refresh_window()
                return input_text
            else:
                raise AssertionError(char)
