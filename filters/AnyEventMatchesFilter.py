from GerritEventFilter import GerritEventFilter

class AnyEventMatchesFilter(GerritEventFilter):

   def filter_event(self, event):
      return True
