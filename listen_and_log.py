from pygerrit.client import GerritClient

from filters.GerritEventFilter import GerritEventFilter
from actions.ActionForGerritEvent import ActionForGerritEvent

client = GerritClient("gerrit-host")

filter = GerritEventFilter()
action = ActionForGerritEvent()

print client.gerrit_version()

client.start_event_stream()

while True:
   event = client.get_event()
   if filter.filter_event(event):
      action.execute_for_event(event)
