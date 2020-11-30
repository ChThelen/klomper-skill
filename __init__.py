from mycroft import MycroftSkill, intent_file_handler


class Klomper(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('klomper-occupied.intent')
    def handle_occupied(self, message):
        self.log.info("set red light", message)
        self.speak_dialog('klomper-occupied')

    @intent_file_handler('klomper-free.intent')
    def handle_free(self, message):
        self.log.info("set green light", message)
        self.speak_dialog('klomper-free')


def create_skill():
    return Klomper()

