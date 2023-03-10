

class PlayerNode:
    def __init__(self, player):
        self._player = player
        self._next = None
        self._last = None
        self._key = player.uid

    def get_player(self):
        return self._player

    def get_next(self):
        return self._next

    def get_last(self):
        return self._last

    def __str__(self):
        return str(self._player)