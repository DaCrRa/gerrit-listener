from filters.AnyEventMatchesFilter import AnyEventMatchesFilter
from actions.PrintEvent import PrintEvent
from action_executors.SimpleActionExecutor import SimpleActionExecutor

filter = AnyEventMatchesFilter()
action = PrintEvent()

executor = SimpleActionExecutor(action, filter)
executor.do_work()
