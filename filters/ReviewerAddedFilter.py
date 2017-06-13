from GerritEventFilter import GerritEventFilter

from pygerrit.events import ReviewerAddedEvent

class ReviewerAddedFilter(GerritEventFilter):

   def filter_event(self, event):
      return isinstance(event, ReviewerAddedEvent)
