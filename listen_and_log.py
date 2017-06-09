from pygerrit.client import GerritClient

client = GerritClient("gerrit-host")

print client.gerrit_version()

client.start_event_stream()

while True:
   print client.get_event()
