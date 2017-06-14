from GerritEventFilter import GerritEventFilter

from pygerrit.events import ReviewerAddedEvent

class ReviewerAddedFilter(GerritEventFilter):

   def __init__(self, filtered_reviewers=[]):
      self.filtered_reviewers=filtered_reviewers

   def filter_event(self, event):
      if isinstance(event, ReviewerAddedEvent):
         if len(self.filtered_reviewers) > 0:
            return event.reviewer.username in self.filtered_reviewers
         else:
            return True
      else:
         return False
