from filters.ReviewerAddedFilter import ReviewerAddedFilter
from actions.PrintEvent import PrintEvent
from action_executors.SimpleActionExecutor import SimpleActionExecutor

filter = ReviewerAddedFilter()
action = PrintEvent()

executor = SimpleActionExecutor(action, filter)
executor.do_work()
