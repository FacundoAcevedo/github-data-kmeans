#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Facundo Acevedo <facevedo[AT]openmailbox[DOT]org>
#
# Distributed under terms of the GPLv3+ license.

"""
get data from gtihub

"""


#all repos must NOT be forks
#Data that i will get:
#    repo_name, repo_creation_date, commit_date, commit_addtions. commit_deletes


from github import Github
import csv

user = ""
password = ""
g = Github(user, password)
repos = g.get_user().get_repos()
repo_id = 0
commit_id = 0

print("Working on....")
with open(user + "-gh.csv", 'w', newline='') as csvfile:
    csv_writer = csv.writer(
        csvfile, delimiter=' ', quotechar='|',
        quoting=csv.QUOTE_MINIMAL)

    for repo in repos:

        if not repo.fork:
            rate_limit_remaining = int(
                repo.raw_headers['x-ratelimit-remaining'])
            print('Rate limit remaining = ', rate_limit_remaining)
            rate_limit_date_reset = int(
                repo.raw_headers[
                    'X-RateLimit-Reset'.lower()])
            if rate_limit_remaining < 100:  # Dangerous zone. Let's not go over the limits.
                time_to_sleep = int(rate_limit_date_reset - time() + 10)
                sleep(time_to_sleep)

            repo_name = repo.full_name.replace('/', '-')
            print(repo_name)
            #*
            repo_creation_date = repo.created_at
            for commit in repo.get_commits():
                commit_date = commit.stats.last_modified
                commit_additions = commit.stats.additions
                commit_deletions = commit.stats.deletions

                csv_writer.writerow(
                    [repo_id, repo_name, repo_creation_date, commit_id,
                     commit_date, commit_additions, commit_deletions])

                commit_id += 1

            repo_id += 1

            # except:
            # print("Error")
            # pass
