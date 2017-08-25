import requests


class GitHubController(object):
    """
    to get the repository
    """

    @staticmethod
    def get_list_repos(uname, passw):
        """
        :param uname: required username
        :param passw: password of the user
        :return: list of the github repositories
        """
        print "test start"
        response = requests.get('https://api.github.com/orgs/prosperllc/repos', auth=(uname, passw))
        print "create_get_request", response
        response_json = response.json()
        print response_json[0]["full_name"]
        for i in range(0, 25):
            respo = response_json[i]["full_name"].split("/")[-1]
            print respo

    """
    to get the no of commites
    """

    @staticmethod
    def get_list_commits(repo_name, uname, passw):
        """
        :param repo_name: name of the github repo
        :param uname: required username
        :param passw: password of the user
        :return: list of the commits for the repo
        """
        response = requests.get('https://api.github.com/repos/prosperllc/' + repo_name + '/commits',
                                auth=(uname, passw))
        response_json = response.json()
        print response.url, response.status_code, response_json


if __name__ == "__main__":
    reponame = "svc-loans"
    uname = "rajpalc"
    passw = "Welcome123@"
    GitHubController().get_list_repos(uname, passw)
    GitHubController().get_list_commits(reponame, uname, passw)
