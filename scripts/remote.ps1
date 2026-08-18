# Run a bash command on lab-wsl inside the `nnfer` conda env from the repo root.
# Usage:  .\scripts\remote.ps1 -Cmd "pytest -q"        (pulls latest main first)
#         .\scripts\remote.ps1 -Cmd "..." -NoPull
param(
    [Parameter(Mandatory = $true)][string]$Cmd,
    [switch]$NoPull,
    [string]$SshHost = "lab-wsl",
    [string]$Repo = "~/haesung/near-neutral-fer"
)
$pull = if ($NoPull) { "" } else { "git pull -q --ff-only`n" }
$script = @"
set -eo pipefail
source ~/miniconda3/etc/profile.d/conda.sh
conda activate nnfer
cd $Repo
$pull$Cmd
"@
# Command is streamed over stdin so no shell-quoting gymnastics are needed.
$script | ssh -o BatchMode=yes $SshHost "tr -d '\r' | bash -l"
exit $LASTEXITCODE
