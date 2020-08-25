#!/usr/bin/python3
import os
import github
import json
import logging

g = github.Github(os.environ['GITHUB_ACCESS_TOKEN'])
logging.basicConfig(format='[%(levelname)s]: %(message)s',level=logging.INFO)
stars_backup = {}
index = 1

for starred_repo in g.get_user().get_starred():
    logging.info(starred_repo)
    repo = {}

    try:
        repo_data = g.get_repo(starred_repo.full_name)
        repo['name'] = repo_data.full_name
    except github.UnknownObjectException:
        logging.warning('repo {} does not exist anymore'.format(starred_repo))
        continue
    except github.GithubException as e:
        logging.warning('something went wrong. {}'.format(str(e)))
        continue


    repo['description'] = repo_data.description
    repo['url'] = 'https://github.com/{}'.format(repo_data.full_name)
    repo['homepage'] = repo_data.homepage
    repo['language'] = repo_data.language
    repo['open_issues'] = repo_data.open_issues
    repo['stars'] = repo_data.stargazers_count
    stars_backup[repo_data.full_name] = repo
    index += 1
    stars_json = json.dumps(stars_backup,indent=2)

with open('github-stars-backup.json', 'w+') as outfile:
    outfile.write(stars_json)