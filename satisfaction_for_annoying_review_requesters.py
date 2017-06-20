from gerrit.server import GerritServer

from filters.GerritEventFilter import CompositeAndFilter
from filters.event_type_filters import PatchsetCreatedFilter
from filters.event_attributes_filters import ChangeOwnerFilter

from actions.SetScoreLabels import SetScoreLabels

from action_executors.SimpleActionExecutor import SimpleActionExecutor

gerrit_server = GerritServer("gerrit-host")

filter = ( CompositeAndFilter()
              .add_filter(PatchsetCreatedFilter())
              .add_filter(ChangeOwnerFilter(["list", "of", "annoying", "reviewers"]))
         )

action = SetScoreLabels(gerrit_server, 2, 1)

executor = SimpleActionExecutor(action, filter)
executor.do_work()
