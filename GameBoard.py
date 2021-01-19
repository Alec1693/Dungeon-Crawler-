class GameBoard:
    def __init__(self,board,currentIndex,pogIndex,pogMessage):
        self._board = board
        self._cPosition = cPosition
        self._pogIndex = pogIndex
        self._pogMessage = pogMessage

    def get_board(self):
        return self._board
    def set_board(self,board):
        self._board = board
    def get_currentIndex(self):
        return self._currentIndex
    def set_currentIndex(self,currentIndex):
        self._currentIndex = currentIndex
    def get_pogIndex(self):
        return self._pogIndex
    def set_pogIndex(self,pogIndex):
        self._pogIndex = pogIndex
    def get_pogMessage(self):
        self._pogMessage = 'You Found the Pot of Gold!! Congratulations!"
        return self._pogMessage
