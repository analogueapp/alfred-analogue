import sys
from workflow import Workflow, ICON_WEB, web
from lib import get_collections
from thumbnails import Thumbs
from enums import ANALOGUE_USERNAME

def main(wf):
    # Get users collections
    results = get_collections(wf.get_password(ANALOGUE_USERNAME))

    if not results:
        wf.add_item('No results found for "%s".' % query,
                    'Try a different query or add a link.',
                    icon=ICON_FILES)

    thumbs = Thumbs(wf.datafile('thumbs'))

    for collection in results:
        # The user is tagged in the url query action
        wf.add_item(
            title=collection['title'],
            subtitle=collection['description'],
            valid=True,
            arg = 'https://www.analogue.app/collection/{}'.format(collection['slug']),
        )

    # Send the results to Alfred as XML
    wf.send_feedback()


if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
