import sys
from workflow import Workflow, ICON_WEB, web
from lib import search_user_logs

def main(wf):
    # Get current user logs
    result = search_user_logs()
    
    # Loop through the returned posts and add an item for each to
    # the list of results for Alfred
    for log in result:
        # The user is tagged in the url query action
        wf.add_item(title=log['content']['title'],
                    subtitle=log['content']['excerpt'],
		    valid=True,
                    arg="https://analogue.app/link/{}/".format(log['content']['slug']),
                    icon=log['content']['imageUrl'])

    # Send the results to Alfred as XML
    wf.send_feedback()

if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
