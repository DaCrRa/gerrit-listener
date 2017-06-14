from GerritEventFilter import GerritEventFilter

class ChangeOwnerFilter(GerritEventFilter):

   def __init__(self, filtered_owners):
      self.filtered_owners=filtered_owners

   def filter_event(self, event):
      try:
         return event.change.owner.username in self.filtered_owners
      except AttributeError:
         return False
