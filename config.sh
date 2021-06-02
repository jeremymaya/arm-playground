#!/bin/bash

echo "Running az synpase trigger list command..."
triggers=$(az synapse trigger list --workspace-name synapse-test-actions --query '[].name' -o tsv)

echo "stage: $1"

for trigger in "${triggers[@]}"
do
    if [[ $1 == "build" ]]; then
    echo "Stopping trigger ${trigger}..."
    az synapse trigger stop --workspace-name synapse-test-actions --name $trigger
    else
    echo "Starting trigger ${trigger}..."
    az synapse trigger start --workspace-name synapse-test-actions --name $trigger
    fi
done