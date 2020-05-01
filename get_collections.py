import sys
from workflow import Workflow, ICON_WEB, web
from lib import get_collections

def main(wf):
    # Get users collections
    result = get_collections()

    for title in result:
        # The user is tagged in the url query action
        wf.add_item(
            title=title,
            subtitle='test',
            valid=True,
            arg='test' # test
        )

    # Send the results to Alfred as XML
    wf.send_feedback()


if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
