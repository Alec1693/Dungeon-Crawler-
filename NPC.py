class NPC:
    def __init__(self,name,speech,position):
        self._name = name
        self._speech = speech
        self._position = position

    def get_name(self):
        return self._name

    def set_name(self,name):
        self._name = name

    def get_speech(self):
        return self._speech

    def set_speech(self,speech):
        self._speech = speech

    def get_position(self):
        return self._position

    def set_position(self,position):
        self._position = position
