#!/usr/bin/env python3

import json

# Source: https://hackersandslackers.com/extract-data-from-complex-json-python/
def json_extract(obj, key):
    """
    Recursively fetch values from nested JSON
    """
    reference_names = set()

    def extract(obj, reference_names, key):
        """
        Recursively search for values of key in JSON tree
        """
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, reference_names, key)
                elif k == key:
                    reference_names.add(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, reference_names, key)
        return reference_names

    values = extract(obj, reference_names, key)
    return values

def generate_dependsOn(resource):
    """
    Generate a list of dependsOn for a resource
    """
    key = 'referenceName'
    dependsOn = list()
    for resource_name in json_extract(resource, key):
        if resource_name[0:2] == 'ds':
            resource_path = '/datasets/{}'.format(resource_name)
        elif resource_name[0:2] == 'ls':
            resource_path = '/linkedServices/{}'.format(resource_name)
        elif resource_name[0:2] == 'nb':
            resource_path = '/notebooks/{}'.format(resource_name)
        elif resource_name[0:2] == 'pl':
            resource_path = '/pipelines/{}'.format(resource_name)
        elif resource_name[0:2] == 'tr':
            resource_path = '/triggers/{}'.format(resource_name)
        elif resource_name[0:4] == 'Auto':
            resource_path = '/integrationRuntimes/{}'.format(resource_name)
        elif resource_name[0:7] == 'synapse':
            resource_path = '/linkedServices/{}'.format(resource_name)
        else:
            continue
        dependsOn.append('[concat(variables(\'workspaceId\'), \'{}\')]'.format(resource_path))
    return dependsOn

def generate_resource_type(resource_name):
    if resource_name[0:2] == 'ds':
        return 'Microsoft.Synapse/workspaces/datasets'
    if resource_name[0:2] == 'ls':
        return 'Microsoft.Synapse/workspaces/linkedServices'
    if resource_name[0:2] == 'nb':
        return 'Microsoft.Synapse/workspaces/notebooks'
    if resource_name[0:2] == 'pl':
        return 'Microsoft.Synapse/workspaces/pipelines'
    if resource_name[0:2] == 'tr':
        return 'Microsoft.Synapse/workspaces/triggers'
    elif resource_name[0:7] == 'synapse':
        return 'Microsoft.Synapse/workspaces/linkedServices'
    else:
        return 'Microsoft.Synapse/workspaces/integrationRuntimes'

def build(resource, api_version, resource_name):
    """
    Build resource before it is added to the Template.json
    """
    resource.update({ "apiVersion": api_version })
    resource.update({ "type": generate_resource_type(resource_name) })
    resource.update({ "dependsOn": generate_dependsOn(resource) })
    resource['name'] = ('[concat(parameters(\'workspaceName\'), \'/{}\')]'.format(resource_name))