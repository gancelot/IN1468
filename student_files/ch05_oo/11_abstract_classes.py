"""

    11_abstract_classes.py

    Note: Without internet, simply change the r = request.post() call to a print(msg.get_text())
          call and it should work.
"""
import abc

import requests


class AbstractBase1(abc.ABC):

    def __init__(self, item):
        self.item = item
        self.do_action()

    @abc.abstractmethod
    def do_action(self):                # subclasses will define what this method does
        pass


class Message(abc.ABC):
    def __init__(self, msg):
        self.msg = msg

    @abc.abstractmethod
    def get_text(self):
        pass


class PlaintextMessage(Message):
    def __init__(self, msg):
        super().__init__(msg)

    def get_text(self):
        return self.msg


class JsonMessage(Message):
    def __init__(self, msg):
        super().__init__(msg)

    def get_text(self):
        return f'{{ "text": "{self.msg}" }}'


class HtmlMessage(Message):
    def __init__(self, msg):
        super().__init__(msg)

    def get_text(self):
        return f'<span>{self.msg}</span>'


def send_message(url: str, msg: Message) -> None:
    r = requests.post(url, data={'text': msg.get_text()})          # For illustration only--returns a 405.


value = 'The meeting today is at 3pm.'

send_message('https://www.reddit.com/r/test/submit', PlaintextMessage(value))

# send_message('https://www.reddit.com/r/test/submit', Message(value))   # TypeError: Can't instantiate abstract class Message without an implementation for abstract method 'get_text'
