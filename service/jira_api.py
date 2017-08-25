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
    def get_jira_user_auth(self, user_name=None, password=None):
        if user_name != None and password != None:
            jira = JIRA(base_url, basic_auth=(user_name, password))
        else:
            # print "User name and password required!"
            jira = JIRA(base_url, basic_auth=(user_name, password))
        return jira

    @staticmethod
    def get_jira_issues(self, jira, query):
        issues = jira.search_issues(query, maxResults=1000)
        print type(issues)

        # convert result object to dic first
        issue_dic = []
        for result in issues:
            d = result.__dict__
            issue_dic.append(d)

        print "issue_dic"
        print issue_dic

        # issues_json = json.dumps(issue_dic)
        # print "issues_json"
        # print issues_json

        # response_str = json.dumps(issues)
        # print "======response_str======"
        # print response_str
        #
        # response_json = json.loads(response_str)
        # print "======response_json======"
        # print response_json
        #
        # print type(json_str[0])
        # for field_name in issues[0].raw['fields']:
        #     print "Field:", field_name, "Value:", issues[0].raw['fields'][field_name]

        # issues_json = json.dumps(issues)
        issues_json = issues
        print type(issues_json[0])
        for field_name in issues[0].raw['fields']:
            print "Field:", field_name, "Value:", issues[0].raw['fields'][field_name]

        return issues_json

if __name__ == '__main__':
    query = "project in ('Investor Tribe', LEN, INVENG, INVG) AND issuetype = Test AND labels != Obsolete " \
            "AND labels = API AND priority in (P0, P1) AND labels != low_priority AND component not in (Note_Split) " \
            "AND component = Orders_API AND project = LEN"

    print JiraController.get_jira_issues(JiraController(),
                                         JiraController().get_jira_user_auth(JiraController(),
                                                                                 '',
                                                                                 ''),
                                         query)
