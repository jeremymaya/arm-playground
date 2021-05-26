#!/bin/bash

workspaceObjectId=az ad sp list --display-name "synapse-test-actions"

echo "$workspaceObjectId.objectId"