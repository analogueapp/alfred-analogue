import sys
from workflow import Workflow, ICON_WEB, web
from lib import get_token
from enums import ANALOGUE_API_TOKEN, ANALOGUE_USERNAME

wf = Workflow()
result, username = get_token(str(sys.argv[1]), str(sys.argv[2]))
wf.save_password(ANALOGUE_API_TOKEN, result)
wf.save_password(ANALOGUE_USERNAME, username)