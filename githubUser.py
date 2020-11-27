import requests
import sys
import random
from collections import Counter

token = '53ae75fcf1361d114efc70a39d45d85b50c3a77f'
headers = {'Authorization': 'token ' + token}
login = requests.get('https://api.github.com/user', headers=headers)

class GitHubUser:


    def __init__(self, users):
        #self.users = ['torvalds', 'gvanrossum', 'poettering', 'dhh', 'moxie0', 'fabpot', 'brendangregg', 'bcantrill', 'antirez']
        #self.num_of_users = num
        self.users = users

    def parsing(self):
        self.selected_user = random.choice(self.users)
        max_num_of_repo = 0
        max_num_of_followers = 0
        req = requests.get(f'https://api.github.com/users/{self.selected_user}')
        req_for_repos = requests.get(f'https://api.github.com/users/{self.selected_user}/repos?access_token={token}')
        return self.repositories(req_for_repos), self.used_languages(req_for_repos)

    def repositories(self, req):
        repo = {}
        for i in req.json():
            repo.update({i["name"]: i["description"]})
        print("The repositories of user {0} w/ descriptions: {1}".format(self.selected_user, ''.join(key + ' : ' +
                                                                         value for key, value in repo.items())))

    def used_languages(self, req):
        all_languages = []
        languages = {}
        for i in req.json():
            lang = i["language"]
            all_languages.append(lang)
            languages.update({i["name"]: lang})
        cnt = Counter(languages.values())
        print("User uses languages: {}".format(list(key + ' : ' + value for key, value in cnt.items())))

    
        # for us in users:
        #     repo = {}
        #     languages = {}
        #     req = requests.get(f'https://api.github.com/users/{us}/repos?access_token={token}')
        #     req_for_followers = requests.get(f'https://api.github.com/users/{us}')
        #     print("User's name: ", us)
        #     for i in req.json():
        #         repo.update({i["name"] : i["description"]})
        #         lang = i["language"]
        #         all_languages.append(lang)
        #         languages.update({i["name"] : lang})
        #     print(req_for_followers.json())
        #     followers = req_for_followers.json()['followers']
        #     print("The number of followers: ", followers)
        #     if followers > max_num_of_followers:
        #         max_num_of_followers = followers
        #         most_popular_user = us
        #
        #     cnt = Counter(languages.values())
        #     print("User's repositories w/ descriptions: ", '\n')
        #     for key, value in repo.items():
        #         print(key, " : ", value)
        #     print('\n', "User uses languages: ")
        #     for key, value in cnt.items():
        #         print(key, " : ", value, "repositories")
        #
        #
        #     print("Кол-во репозиториев: ", req_for_followers.json()['public_repos'])
        #     print("----------------------")
        #     if req_for_followers.json()['public_repos'] > max_num_of_repo:
        #         max_num_of_repo = req_for_followers.json()['public_repos']
        #         owner_max_repo = us
        #     else:
        #         continue

        # print('\n', "Owner of the largest number of repositories: ", owner_max_repo)
        # print("The most popular user: ", most_popular_user, '. The number of his followers: ', max_num_of_followers)
        # self.most_popular_lang(all_languages)
        #self.most_popular_user(users)

    # def most_popular_lang(self, languages):
    #     langs = Counter(languages)
    #     print("The most popular language: ", (langs.most_common()[0])[0])

def main(argv):
    myGitHubParser = GitHubUser(argv)
    print(myGitHubParser.parsing())

if __name__ == '__main__':
    main(sys.argv[1:])