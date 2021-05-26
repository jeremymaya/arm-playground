param (
    [string] $keyVaultName,
    [string] $workspaceName
)

# Set KeyVault Access Policy for Synapse Workspace
Write-Host "Setting KeyVault Access Policy for Synapse Workspace"
Set-AzKeyVaultAccessPolicy `
    -VaultName $keyVaultName `
    -ServicePrincipalName  $workspaceName `
    -PermissionsToSecrets get,list