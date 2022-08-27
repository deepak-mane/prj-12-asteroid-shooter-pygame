param(
    [Parameter()]
    [String]$filename
)

# For windows -- uncomment below
$headercontent = "#!" + $pwd +"\.venv390\Scripts\python.exe"
Add-Content -Path ".\tempmain.py" -Value $headercontent
Add-Content -Path ".\tempmain.py" -Value (Get-Content -Path "..\scripts\my_sample_template390.txt")
# Copy-Item .\scripts\my_sample_template.txt my_sample_template.py
$MyFile = Get-Content ".\tempmain.py" -Raw
$utf8 = New-Object System.Text.UTF8Encoding $false
$MyFile = Get-Content ".\tempmain.py" -Raw
Set-Content -Value $utf8.GetBytes($MyFile) -Encoding Byte -Path ".\tempmain.py"
$TargetFile = ".\main.py"
$TargetPath = Join-Path -Path $pwd -ChildPath ".\main.py"

#If the file does  exist, rename it.
if (Test-Path -Path $TargetPath -PathType Leaf){
  try {
    $datetime = $(Get-Date -Format "MMddyyyy_hhmmss")
    $bkpfile = ".\main_" + $datetime +".py"
    Rename-Item -Path $TargetPath $bkpfile
  }
  catch {
      throw $_.Exception.Message
  }  
}

$orignal_filename = Join-Path -Path $pwd -ChildPath ".\tempmain.py"

#If the filename not provided, create it as main.py.
if ([string]::IsNullOrEmpty($filename)) {
  try {
    Rename-Item -Path $orignal_filename $TargetFile
  }
  catch {
      throw $_.Exception.Message
  }
}
  # If the filename provided, create it with provided name
else {
  try {
    Rename-Item -Path $orignal_filename $filename
  }
  catch {
      throw $_.Exception.Message
  }

} 








