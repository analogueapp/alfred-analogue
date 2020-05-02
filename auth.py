import sys
from workflow import Workflow, ICON_WEB, web
from lib import get_token
from enums import ANALOGUE_API_TOKEN, ANALOGUE_USERNAME

wf = Workflow()
result, username = get_token('hughmil3s@gmail.com', 'kd3k.f*.NwtR!dV6r4X2')
wf.save_password(ANALOGUE_API_TOKEN, result)
wf.save_password(ANALOGUE_USERNAME, username)