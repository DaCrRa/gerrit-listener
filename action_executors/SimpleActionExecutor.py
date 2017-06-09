from pygerrit.client import GerritClient

from actions.ActionForGerritEvent import ActionForGerritEvent
from filters.GerritEventFilter import GerritEventFilter

class SimpleActionExecutor:

   def __init__(self, action, filter):
      self.gerrit_client = GerritClient("gerrit-host")
      self.action = action
      self.filter = filter
      print self.gerrit_client.gerrit_version()

   def do_work(self):

      self.gerrit_client.start_event_stream()

      while True:
         event = self.gerrit_client.get_event()
         if self.filter.filter_event(event):
            self.action.execute_for_event(event)
