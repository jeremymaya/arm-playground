#!/bin/bash

echo "Running az synpase trigger list command..."
triggers=$(az synapse trigger list --workspace-name synapse-test-actions --query '[].name' -o tsv)

for trigger in "${triggers[@]}"
do
    if [ stage == "build"]; then
    echo "Stopping trigger ${trigger}..."
    az synapse trigger stop --workspace-name synapse-test-actions --name $trigger
    else
    echo "Starting trigger ${trigger}..."
    az synapse trigger start --workspace-name synapse-test-actions --name $trigger
    fi
done