import abc

class GerritEventFilter:

   __metaclass__ = abc.ABCMeta

   @abc.abstractmethod
   def filter_event(self, event):
      raise NotImplementedError()
