from pygerrit.events import GerritEvent

class ActionForGerritEvent:

   def execute_for_event(self, event):
      print event
