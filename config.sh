#!/bin/bash

workspaceObjectId=$(az ad sp list --display-name "synapse-test-actions" --query "objectId" -o json)

echo "$workspaceObjectId"