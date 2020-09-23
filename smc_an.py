import AppClass_sm


X = set('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')


class AppClass:

    def __init__(self):
        self._fsm = AppClass_sm.Analyzer_sm(self)
        self._is_acceptable = False
        self._com_name = ''
        self.current_symbol = ''

    def check_string(self, string):
        if len(string) > 80:
            return self._is_acceptable, self._com_name
        self._fsm.enterStartState()
        for c in string:
            self.current_symbol = c
            if c in X:
                self._fsm.X()
            elif c == ' ':
                self._fsm.space()
            elif c == '-':
                self._fsm.hyphen()
            elif c == '\n':
                self._fsm.EOS()
            else:
                self._fsm.unknown()
        self._fsm.EOS()
        return self._is_acceptable, self._com_name

    def save_name(self):
        self._com_name += self.current_symbol

    def acceptable(self):
        self._is_acceptable = True

    def unacceptable(self):
        self._is_acceptable = False
