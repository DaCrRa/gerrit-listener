from ActionForGerritEvent import ActionForGerritEvent

class PrintEvent(ActionForGerritEvent):

   def execute_for_event(self, event):
      print event
