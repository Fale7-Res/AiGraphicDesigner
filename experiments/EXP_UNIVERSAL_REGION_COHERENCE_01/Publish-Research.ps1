[CmdletBinding()]
param(
    [switch]$CheckOnly,
    [string]$RepoPath = 'C:\Users\Mohamed\Desktop\AiGraphicDesigner',
    [string]$ExpectedOrigin = 'https://github.com/Fale7-Res/AiGraphicDesigner.git'
)

$ErrorActionPreference = 'Stop'
# Git exit codes are checked explicitly below, including under PowerShell 7.
$PSNativeCommandUseErrorActionPreference = $false

function Invoke-RepoGit {
    param([Parameter(Mandatory = $true)][string[]]$GitArgs)
    $Lines = @(& git -c "safe.directory=$Repo" @GitArgs)
    $Code = $LASTEXITCODE
    if ($Code -ne 0) {
        throw "Git failed (exit $Code): git $($GitArgs -join ' '). See Git's error above."
    }
    return $Lines
}

try {
$Repo = (Resolve-Path -LiteralPath $RepoPath).Path.TrimEnd('\', '/')
$Scope = 'experiments/EXP_UNIVERSAL_REGION_COHERENCE_01'
Set-Location -LiteralPath $Repo
$Top = (Invoke-RepoGit -GitArgs @('rev-parse', '--show-toplevel')).Trim().Replace('/', '\').TrimEnd('\')
if ($Top -ne $Repo.Replace('/', '\')) { throw 'Unexpected repository' }
if ((Invoke-RepoGit -GitArgs @('branch', '--show-current')).Trim() -ne 'main') { throw 'Expected main' }
if ((Invoke-RepoGit -GitArgs @('remote', 'get-url', 'origin')).Trim() -ne $ExpectedOrigin) { throw 'Unexpected origin remote' }
if (-not (Test-Path -LiteralPath $Scope -PathType Container)) { throw "Missing research folder: $Scope" }
$null = Invoke-RepoGit -GitArgs @('var', 'GIT_AUTHOR_IDENT')
$null = Invoke-RepoGit -GitArgs @('var', 'GIT_COMMITTER_IDENT')
$Staged = @(Invoke-RepoGit -GitArgs @('diff', '--cached', '--name-only'))
if (@($Staged | Where-Object { $_ -notlike "$Scope/*" }).Count -gt 0) {
    throw 'Unrelated files are staged. Preserve them and inspect the index before publishing this checkpoint.'
}
Write-Host "Repository: $Repo"
Write-Host "Branch: main; scoped staged files: $($Staged.Count)"
Invoke-RepoGit -GitArgs @('diff', '--cached', '--stat') | ForEach-Object { Write-Host $_ }
if ($CheckOnly) {
    Write-Host 'CHECK ONLY passed. No fetch, staging, commit, or push performed.' -ForegroundColor Green
    return
}

Write-Host '[1/5] Fetching origin/main and checking ancestry...'
Invoke-RepoGit -GitArgs @('-c', 'http.sslBackend=openssl', '-c', 'http.sslVerify=true', 'fetch', 'origin', 'main') | ForEach-Object { Write-Host $_ }
$Counts = ((Invoke-RepoGit -GitArgs @('rev-list', '--left-right', '--count', 'HEAD...origin/main')).Trim() -split '\s+')
if ($Counts.Count -ne 2) { throw 'Cannot parse ancestry check' }
if ([int]$Counts[1] -gt 0) {
    throw 'Remote contains commits missing locally. Stop and inspect: git log --left-right --graph HEAD...origin/main. Do not reset or force-push.'
}

Write-Host '[2/5] Staging only the approved research folder...'
Invoke-RepoGit -GitArgs @('add', '--', $Scope) | ForEach-Object { Write-Host $_ }
$Staged = @(Invoke-RepoGit -GitArgs @('diff', '--cached', '--name-only'))
if (@($Staged | Where-Object { $_ -notlike "$Scope/*" }).Count -gt 0) { throw 'Index contains unrelated files; publication stopped.' }
Invoke-RepoGit -GitArgs @('diff', '--cached', '--stat') | ForEach-Object { Write-Host $_ }
Write-Host '[3/5] Creating research commit if needed...'
# Do not use diff --quiet here: exit 1 means changes, not a failure.
if ($Staged.Count -gt 0) {
    Invoke-RepoGit -GitArgs @('-c', 'gc.auto=0', 'commit', '-m', '[AGD-CODEX-RESEARCH] Evaluate universal contour selection region integration and coherence') | ForEach-Object { Write-Host $_ }
} else {
    Write-Host 'No staged changes; keeping existing commits without creating a duplicate.'
}
Write-Host '[4/5] Pushing main to origin...'
Invoke-RepoGit -GitArgs @('-c', 'http.sslBackend=openssl', '-c', 'http.sslVerify=true', 'push', 'origin', 'main') | ForEach-Object { Write-Host $_ }
Write-Host '[5/5] Independently verifying remote main...'
$LocalHead = (Invoke-RepoGit -GitArgs @('rev-parse', 'HEAD')).Trim()
$RemoteLines = @(Invoke-RepoGit -GitArgs @('-c', 'http.sslBackend=openssl', '-c', 'http.sslVerify=true', 'ls-remote', 'origin', 'refs/heads/main'))
if ($RemoteLines.Count -ne 1) { throw 'Expected exactly one remote main reference' }
$RemoteHead = ($RemoteLines[0] -split '\s+')[0]
if ($LocalHead -ne $RemoteHead) { throw "Remote $RemoteHead differs from local $LocalHead" }
Write-Host "SUCCESS: committed checkpoint is verified on origin/main: $LocalHead" -ForegroundColor Green
} catch {
    Write-Host "PUBLICATION STOPPED: $($_.Exception.Message)" -ForegroundColor Red
    throw
}
