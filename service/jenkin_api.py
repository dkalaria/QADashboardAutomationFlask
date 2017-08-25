import urllib2
import json
import base64
import logging

base_url="https://jenkins.prosper.com/job/Investor/job/QA"
log = logging.getLogger(__name__)


class JenkinController(object):
    """
    Represents a single point of contact for Jenkins API.
    """
    def __init__(self):
        print "Initialize"

    @staticmethod
    def get_jenkin_user_auth(username=None, password=None):
        """
        To get the jenkin user authentication
        :param username: Required user name.
        :param password: Required password for the user.
        :return: return base64 string.
        """
        if username != None and password != None:
            base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
        else:
            print "User name and password required!"
            base64string = None
        return base64string

    @staticmethod
    def get_jenkin_jobs_list_with_user_auth(url, user_name, password):
        base64string = JenkinController.get_jenkin_user_auth(user_name, password)
        JenkinController.get_jenkin_jobs_list(base64string, url)

    @staticmethod
    def get_jenkin_jobs_list(base64string, url):
        """
        To get jenkin jobs list
        :param base64string: user auth base64 string.
        :param url: To access jobs list for the given valid url.
        :return: json with list of job names for the given folder.
        """
        updated_url = "%s/api/python" % (url)
        request = urllib2.Request(updated_url)
        request.add_header("Authorization", "Basic %s" % base64string)
        result = urllib2.urlopen(request)

        # job dict to json
        j=eval(result.read())
        my_dumps_str = json.dumps(j)
        my_json_response = my_dumps_str
        # my_json_response = json.loads(my_dumps_str)
        print my_json_response
        return my_json_response

    @staticmethod
    def get_jenkin_job_test_results_with_auth(base_url, job_name, user_name, password, build="lastCompletedBuild"):
        base64string = JenkinController.get_jenkin_user_auth(user_name, password)
        return JenkinController.get_jenkin_job_test_results(base64string, base_url, job_name, build)

    @staticmethod
    def get_jenkin_job_test_results(base64string, base_url, job_name, build="lastCompletedBuild"):
        """
        To get jenkin test results of the given job
        :param base64string: user auth base64 string.
        :param base_url: base folder url where the jobs are available.
        :param job_name: job name to get test results.
        :param build: build number/name by default with last completed build.
        :return: json response of job test results.
        """
        url="%s/job/%s/lastCompletedBuild/testReport" % (base_url, job_name)
        url = url.replace("lastCompletedBuild", build)

        my_json_response = JenkinController.get_jenkin_jobs_list(base64string, url)
        return my_json_response

if __name__ == '__main__':
    base_url="https://jenkins.prosper.com/job/Investor/job/QA"
    print JenkinController.get_jenkin_job_test_results_with_auth(base_url,
                                                                 "stg2-investor-platform-order-tests",
                                                                 "",
                                                                 "")
    print JenkinController.get_jenkin_jobs_list_with_user_auth(base_url,
                                                               "",
                                                               "")



