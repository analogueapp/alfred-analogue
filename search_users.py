import sys
from workflow import Workflow, ICON_FILES
from workflow.background import run_in_background, is_running

from lib import search_analogue_users
from thumbnails import Thumbs

from datetime import date, datetime
import time
log = None

def main(wf):
    if len(wf.args):
        query = wf.args[0]
    else:
        query = None

    log.debug('query : %r', query)

    results = search_analogue_users(query=query)

    log.debug('%d results.', len(results))

    if not results:
        wf.add_item('No results found for "%s".' % query,
                    'Try a different query or add a link.',
                    icon=ICON_FILES)

    thumbs = Thumbs(wf.datafile('thumbs'))

    for hit in results:
        wf.add_item(
            title = hit['name'],
            subtitle = hit['username'],
            valid = True,
            arg = 'https://www.analogue.app/@{}'.format(hit['username']),
            icon = thumbs.thumbnail(hit.get('image_url')),
            icontype = None
        )

    wf.send_feedback()

    thumbs.save_queue()
    if thumbs.has_queue:
        thumbs.process_queue()
        # TODO run in background
        # if not is_running('generate_thumbnails'):
        #     run_in_background('generate_thumbnails',
        #                       ['/usr/bin/python',
        #                        wf.workflowfile('thumbnails.py')])

    return 0


if __name__ == u"__main__":
    wf = Workflow()
    log = wf.logger
    sys.exit(wf.run(main))
