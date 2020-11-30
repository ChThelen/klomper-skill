from mycroft import MycroftSkill, intent_file_handler


class Klomper(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('klomper.intent')
    def handle_klomper(self, message):
        self.log.info("this is my first skill!", message)
        self.speak_dialog('klomper')


def create_skill():
    return Klomper()

