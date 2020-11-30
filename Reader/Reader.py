import rdm6300
from Request import Request


class Reader(rdm6300.Reader):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.quit_loop = False

    def set_card_callback(self, callback):
        self._callback = callback

    def card_inserted(self, card):
        print(f"card inserted {card}")

    def card_removed(self, card):
        print(f"card removed {card}")
        r = Request(user_id=str(card.value))
        self._callback(r)

    def invalid_card(self, card):
        print(f"invalid card {card}")


class TestReader:
    def __init__(self, *args, **kwargs):
        pass

    def set_card_callback(self, callback):
        self._callback = callback

    def card_inserted(self, card):
        print(f"card inserted {card}")

    def card_removed(self, card):
        print(f"card removed {card}")
        r = Request(user_id=card)
        self._callback(r)

    def invalid_card(self, card):
        print(f"invalid card {card}")

    def start(self):
        self.card_removed('16157103')


if __name__ == '__main__':
    reader = Reader('/dev/serial0')
    reader.start()
