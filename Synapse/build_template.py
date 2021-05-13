#!/usr/bin/env python3

import os
import json
import build_resource

def get_list_of_resource_files(path):
    """
    List resource files that needs to be appended to Template.json
    """
    files = dict()
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_dir():
                for (dirpath, dirnames, filenames) in os.walk(entry):
                    for file in filenames:
                        file_name = file.split('.')[0]
                        file_path = os.path.join(dirpath, file)
                        files[file_name] = file_path
    return files

def update_template_with_resources(path, files, api_version):
    """
    Append resources to Template.json
    """
    with open(path + '/TemplateEmpty.json') as f:
        template = json.load(f)
    for file_name, file_path in files.items():
        with open(file_path) as f:
            resource = json.load(f)
            build_resource.build(resource, api_version, file_name)
        template['resources'].append(resource)
    with open(path + '/Template.json', mode='w') as artifact:
        artifact.seek(0)
        json.dump(template, artifact, indent = 4, sort_keys=True)
        artifact.truncate()

def main():
    path = 'Synapse/Resources'
    api_version = '2019-06-01-preview'
    files = get_list_of_resource_files(path)
    update_template_with_resources(path, files, api_version)

if __name__ == "__main__":
    main()