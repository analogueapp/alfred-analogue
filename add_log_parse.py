import sys
import webbrowser
from workflow import Workflow, ICON_FILES
from workflow.background import run_in_background, is_running

from lib import add_log
from thumbnails import Thumbs

from datetime import date, datetime
import time

log = None


if __name__ == u"__main__":
    wf = Workflow()
    log = wf.logger

    if len(wf.args):
        query = wf.args[0]
    else:
        query = None

    log.debug("query : %r", query)

    result = add_log(query)
    webbrowser.open_new_tab(result)
