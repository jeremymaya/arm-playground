#!/bin/bash

# workspaceObjectId=$(az ad sp list --display-name 'synapse-test-actions' --query '[].objectId' -o tsv)

# az role assignment list --assignee 'fdb798ab-987e-4e10-92d0-be511d22dcab'

echo "Running az synpase trigger list command..."
az synapse trigger list --workspace-name synapse-test-actions

az synapse trigger list --workspace-name synapse-test-actions --query 'name' -o json