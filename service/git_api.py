import requests

class GetRequest(object):

    """
    to get the repository
    """
    @staticmethod
    def create_get_request(uname,passw):
        print "test start"
        response = requests.get('https://api.github.com/orgs/prosperllc/repos', auth=(uname, passw))
        print "create_get_request", response.json()
        response_json = response.json()
        print response_json[0]["full_name"]
        for i in range(0 ,25):
            print response_json[i]["full_name"]

    """
    to get the no of commites
    """
    @staticmethod
    def get_list_commites(repo_name,uname,passw):
        response = requests.get('https://api.github.com/repos/prosperllc/'+repo_name+'/stats/commit_activity',auth=(uname, passw))
        response_json = response.json()
        print response.url, response.status_code, response_json


if __name__ == "__main__":
    reponame = "platform-prospect"
    uname = "rajpalc"
    passw = "Welcome123@"
    GetRequest().create_get_request(uname,passw)
    GetRequest().get_list_commites(reponame,uname,passw)