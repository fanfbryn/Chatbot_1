# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionMakan(Action):

    def name(self) -> Text:
        return "action_makanan"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        makan = tracker.get_slot("makan")
        dispatcher.utter_message(text= "Baik anda memesan {} !".format(makan))
        return []

class ActionMinum(Action):

    def name(self) -> Text:
        return "action_minuman"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        minum = tracker.get_slot("minum")
        dispatcher.utter_message(text= "Baik anda memesan {} !".format(minum))
        return []
