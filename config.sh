#!/bin/bash

workspaceObjectId=$(az ad sp list --display-name 'synapse-test-actions' --query '[].objectId' -o tsv)

az role assignment list --assignee 'f629d07b-8c93-49d6-9dc7-e5e79a39e3a4'