from jira import JIRA

import json
import logging

base_url="https://jira.prosper.com"
log = logging.getLogger(__name__)


class JiraController(object):
    """
    Represents a single point of contact for JIRA API.
    """
    def __init__(self):
        print "Initialize"

    @staticmethod
    def get_jira_user_auth(user_name=None, password=None):
        """
        To get JIRA user authentication
        :param user_name: valid user name
        :param password: password for the same user.
        :return: return jira object
        """
        if user_name != None and password != None:
            jira = JIRA(base_url, basic_auth=(user_name, password))
        else:
            print "User name and password required!"
        return jira

    @staticmethod
    def get_jira_issues_with_auth(query, user_name, password):
        """
        To get jira query result with user name and password.
        :param query: 
        :param user_name: 
        :param password: 
        :return: query result in json.
        """
        jira = JiraController.get_jira_user_auth(user_name, password)
        return JiraController.get_jira_issues(jira, query)

    @staticmethod
    def get_jira_issues(jira, query):
        """
        To get jira issues for the given query
        :param jira: 
        :param query: 
        :return: 
        """
        issues = jira.search_issues(query, maxResults=1000)
        print type(issues)

        json_key_list = {
            "keys": [],
            "count": len(issues)
        }
        for issue in issues:
            json_key_list["keys"] += [{
                "key": issue.key
            }]
        print "build json" + str(json_key_list)
        json_response = json.dumps(json_key_list)
        print json_response
        # json_response = json.loads(json_response)
        return json_response

if __name__ == '__main__':
    query = "project in ('Investor Tribe', LEN, INVENG, INVG) AND issuetype = Test AND labels != Obsolete " \
            "AND labels = API AND priority in (P0, P1) AND labels != low_priority AND component not in (Note_Split) " \
            "AND component = Orders_API AND project = LEN"

    print JiraController.get_jira_issues_with_auth(query, '', '')
