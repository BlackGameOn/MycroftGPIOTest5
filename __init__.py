from os.path import dirname, abspath
import sys
import requests
import json
import threading

sys.path.append(abspath(dirname(__file__)))

from adapt.intent import IntentBuilder
try:
    from mycroft.skills.core import MycroftSkill
except:
    class MycroftSkill:
        pass

__author__ = 'blacks'


class GPIO_ControlSkill(MycroftSkill):

    def __init__(self):
        super(GPIO_ControlSkill, self).__init__(name="GPIO_ControlSkill")

    def initialize(self):
        self.load_data_files(dirname(__file__))

        command_intent = IntentBuilder("IoCommandIntent").require("command").require("ioobject").optionally("ioparam").build()
        system_intent = IntentBuilder("SystemQueryIntent").require("question").require("systemobject").build()

        self.register_intent(command_intent, self.handle_command_intent)
        self.register_intent(system_intent, self.handle_system_intent)

    def handle_system_intent(self, message):
        if message.data["systemobject"] == "Name":
            self.speak_dialog("name")
            self.speak(__name__)

    def handle_command_intent(self, message):
        elif message.data["command"].upper() == "TURN":
            if message.data["ioobject"].upper() == "LED":
                if "ioparam" in message.data:
                    if message.data["ioparam"].upper() == "ON":
                        python //kerems//LED_AC.py
                    elif message.data["ioparam"].upper() == "OFF":
                        python //home//pi//kerems//LED_KAPAT.py
                else:
                    self.speak_dialog("ipparamrequired")

    def stop(self):


def create_skill():
    return GPIO_ControlSkill()
