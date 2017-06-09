from pygerrit.client import GerritClient

from filters.GerritEventFilter import GerritEventFilter

client = GerritClient("gerrit-host")
filter = GerritEventFilter()

print client.gerrit_version()

client.start_event_stream()

while True:
   event = client.get_event()
   if filter.filter_event(event):
      print event
