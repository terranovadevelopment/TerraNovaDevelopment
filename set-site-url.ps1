# Run from this website folder: .\set-site-url.ps1 -SiteUrl "https://YOUR-ACTUAL-SITE.onrender.com"
param([Parameter(Mandatory=$true)][string]$SiteUrl)
$SiteUrl = $SiteUrl.TrimEnd('/')
Get-ChildItem -Path $PSScriptRoot -Filter *.html -Recurse | ForEach-Object {
  $content = [System.IO.File]::ReadAllText($_.FullName)
  $content = $content.Replace('https://REPLACE-WITH-YOUR-LIVE-SITE-URL', $SiteUrl)
  [System.IO.File]::WriteAllText($_.FullName, $content)
}
Write-Host "Social preview URLs updated to $SiteUrl"
