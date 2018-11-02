#!/usr/bin/env python
# Script to Download a projects summary from Toggl in CSV format
#
# Brainstorm S.n.c - http://brainstorm.it
# author: Mario Orlandi, 2018

import csv
import sys
import json
from toggl.TogglPy import Toggl
from .config_file import read_config_file


def print_title(title):
    print('\n****************************************\n* %s\n****************************************' % title)


def dump_objects(title, objects):
    print_title(title)
    print(json.dumps(objects, indent=2))


def parse_project_name(project_name):
    """
    Examples:
        'MyProject (budget 104)' --> 'MyProject', 104
        'MyProject' --> 'MyProject', None
    """

    closer = ')'
    opener = '(budget'

    name = project_name
    budget = None

    if project_name.endswith(closer):
        n = project_name.find(opener)
        if n >= 0:
            name = project_name[:n].strip()
            data = project_name[n + len(opener):-1 * len(closer)]
            budget = int(data.strip())

    return name, budget


def download_projects(api):

    projects = []
    clients = api.getClients()
    for client in clients:

        client_projects = api.getClientProjects(client['id'], active='both')
        if client_projects:
            #dump_objects('Projects for client %s' % client['name'], client_projects)
            for project in client_projects:
                projects.append({
                    'project': project,
                    'client': client,
                })

    return projects


def dump_projects_as_csv(projects, stream):
    csvwriter = csv.writer(stream)
    csvwriter.writerow([
        'id',
        'name',
        'wid',
        'cid',
        'cname',
        'active',
        'budget',
        'actual_hours',
        'billable',
        'created_at',
        'is_private',
    ])
    for p in projects:
        name, budget = parse_project_name(p['project']['name'])
        csvwriter.writerow([
            p['project']['id'],
            name,
            p['project']['wid'],
            p['client']['id'],
            p['client']['name'],
            p['project']['active'],
            budget,
            p['project'].get('actual_hours', 0),
            p['project']['billable'],
            p['project']['created_at'],
            p['project']['is_private'],
        ])


def main():

    # Read config file
    config = read_config_file()
    api_key = config.get('general', 'api_key').strip()

    api = Toggl()
    api.setAPIKey(api_key)
    projects = download_projects(api)
    dump_projects_as_csv(projects, sys.stdout)


if __name__ == "__main__":
    main()

