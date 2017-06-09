import abc

from pygerrit.events import GerritEvent

class ActionForGerritEvent:

   __metaclass__ = abc.ABCMeta

   @abc.abstractmethod
   def execute_for_event(self, event):
      raise NotImplementedError()
