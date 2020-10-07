# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

class FormDataCollect(FormAction):
    def name(self) -> Text:
        return "Form_Info"
    @staticmethod
    def required_slots(tracker: "Tracker") -> List(Text):
        return ["name","visiting_place","visiting_time","returning_time"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict[Text,Any]]]]:
        return {
            "name":[self.from_text()],
            "visiting_place":[self.from_text()],
            "visiting_time":[self.from_text()],
            "returning_time":[self.from_text()]
        }
    def submit(
        self,


        dispatcher:"collectingDispatcher",
        tracker:"Tracker",
        domain:Dict[Text,Any],

    ) -> List[EventType]:

        dispatcher.utter_message("Here are the information that you have provided, it will be use for reducing crowd in our Zurich city. Do you want to save it?\nName: {0}, \nvisiting_place: {1}, \nvisiting_time: {2}, \nreturning_place: {3}" .format(
            tracker.get_slot("name"),
            tracker.get_slot("visiting_place"),
            tracker.get_slot("visiting_time"),
            tracker.get_slot("returning_time"),


        ))
        return []

