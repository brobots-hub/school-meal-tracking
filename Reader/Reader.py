from time import sleep

import rdm6300
from Request import Request


class Reader(rdm6300.BaseReader):
    def set_delay(self, delay):
        self._delay = delay

    def set_card_callback(self, callback):
        self._callback = callback

    def card_inserted(self, card):
        r = Request(user_id=str(card.value))
        self._callback(r)
        print(f"card inserted {card}")

        sleep(self._delay)

    def card_removed(self, card):
        print(f"card removed {card}")
        pass

    def invalid_card(self, card):
        print(f"invalid card {card}")
        pass


class TestReader:
    def __init__(self, *args, **kwargs):
        pass

    def set_delay(self, delay):
        self._delay = delay

    def set_card_callback(self, callback):
        self._callback = callback

    def card_inserted(self, card):
        r = Request(user_id=card)
        self._callback(r)
        print(f"card inserted {card}")

        sleep(self._delay)

    def card_removed(self, card):
        print(f"card removed {card}")
        pass

    def invalid_card(self, card):
        print(f"invalid card {card}")
        pass

    def start(self):
        self.card_inserted('1')


if __name__ == '__main__':
    reader = Reader('/dev/serial0')
    reader.start()
