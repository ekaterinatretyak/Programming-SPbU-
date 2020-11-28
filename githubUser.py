import requests
import sys
import random
from collections import Counter

token = '53ae75fcf1361d114efc70a39d45d85b50c3a77f'
headers = {'Authorization': 'token ' + token}
login = requests.get('https://api.github.com/user', headers=headers)

class GitHubUser:


    def __init__(self, users):
        self.users = users

    def parsing(self, user):
        #self.selected_user = random.choice(self.users)
        #req = requests.get(f'https://api.github.com/users/{self.selected_user}')
        req = requests.get(f'https://api.github.com/users/{user}?access_token={token}')
        req_for_repos = requests.get(f'https://api.github.com/users/{user}/repos?access_token={token}')
        return req, req_for_repos
        #return req_for_repos
        #return self.repositories(req_for_repos), self.used_languages(req_for_repos), self.max_num_repo(),\
               #self.most_popular_lang(), self.most_popular_user()

    def repositories(self):
        self.selected_user = input()
        req, req_for_repos = self.parsing(self.selected_user)
        repo = {}
        # for i in req_for_repos.json():
        #     print(i['name'])
        for i in req_for_repos.json():
            repo.update({i["name"] : i["description"]})
        return "The repositories of user {0} w/ descriptions: \n {1}".format(self.selected_user, repo.items())

    def used_languages(self):
        req, req_for_repos = self.parsing(self.selected_user)
        languages = {}
        for i in req_for_repos.json():
            lang = i["language"]
            languages.update({i["name"]: lang})
        cnt = Counter(languages.values())
        return "User {0} uses languages: {1}".format(self.selected_user, cnt.items())

    def max_num_repo(self):
        max_num_of_repo = 0
        for us in self.users:
            req, req_for_repos = self.parsing(us)
            num_of_repo = req.json()['public_repos']
            if num_of_repo > max_num_of_repo:
               max_num_of_repo = num_of_repo
               owner_max_repo = us
        return "Owner of the largest number of repositories: {0}. {1} of his repositories are available".\
            format(owner_max_repo, max_num_of_repo)

    def most_popular_lang(self):
        all_languages = []
        for us in self.users:
            req, req_for_repos = self.parsing(us)
            for i in req_for_repos.json():
                all_languages.append(i['language'])

        langs = Counter(all_languages)
        return ("The most popular language: {}.".format(langs.most_common()[0][0]))

    def most_popular_user(self):
        max_num_of_followers = 0
        for us in self.users:
            req, req_for_repos = self.parsing(us)
            followers = req.json()['followers']
            if followers > max_num_of_followers:
                max_num_of_followers = followers
                most_popular_user = us
        return "The most popular user: {0}. The number of his followers: {1}.".format(most_popular_user, max_num_of_followers)

def main(argv):
    myGitHubParser = GitHubUser(argv)
    print(myGitHubParser.repositories())
    print(myGitHubParser.used_languages())
    print(myGitHubParser.max_num_repo())
    print(myGitHubParser.most_popular_lang())
    print(myGitHubParser.most_popular_user())

if __name__ == '__main__':
    main(sys.argv[1:])