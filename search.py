import sys
from workflow import Workflow, ICON_WEB, web
from lib import search_analogue


def main(wf):
    if len(wf.args):
        query = wf.args[0]
    else:
        query = None

    result = search_analogue(query=query)

    for hit in result:
        # The user is tagged in the url query action
        wf.add_item(
            title=hit["title"],
            subtitle=hit["excerpt"],
            valid=True,
            arg="https://analogue.app/link/{}/".format(hit["slug"]),
            icon=hit["image_url"],
        )

    # Send the results to Alfred as XML
    wf.send_feedback()


if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
