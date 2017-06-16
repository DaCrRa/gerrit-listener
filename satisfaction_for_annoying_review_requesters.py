from filters.GerritEventFilter import CompositeAndFilter
from filters.event_type_filters import PatchsetCreatedFilter
from filters.event_attributes_filters import ChangeOwnerFilter

from actions.SetScoreLabels import SetScoreLabels

from action_executors.SimpleActionExecutor import SimpleActionExecutor

filter = ( CompositeAndFilter()
              .add_filter(PatchsetCreatedFilter())
              .add_filter(ChangeOwnerFilter(["list", "of", "annoying", "reviewers"])) )
         )

action = SetScoreLabels("gerrit-host", 2, 1)

executor = SimpleActionExecutor(action, filter)
executor.do_work()
