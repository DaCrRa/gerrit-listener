import abc

class GerritEventFilter:

   __metaclass__ = abc.ABCMeta

   @abc.abstractmethod
   def filter_event(self, event):
      raise NotImplementedError()

class CompositeGerritEventFilter(GerritEventFilter):

   __metaclass__ = abc.ABCMeta

   @abc.abstractmethod
   def filter_event(self, event):
      raise NotImplementedError()

   def __init__(self):
      self.filters = []

   def add_filter(self, gerrit_event_filter):
      self.filters.append(gerrit_event_filter)
      return self

class CompositeAndFilter(CompositeGerritEventFilter):

   def filter_event(self, event):
      filter_matches = True
      for filter in self.filters:
         filter_matches = filter_matches and filter.filter_event(event)
         if not filter_matches:
            break
      return filter_matches
