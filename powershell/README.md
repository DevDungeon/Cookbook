
Windows PowerShell
==================

Network wake on lan packet
http://www.adminarsenal.com/admin-arsenal-blog/powershell-sending-a-wake-on-lan-wol-magic-packet/

create an alias
how to create a function
how to create a script

file manipulation
echo to file
cat a couple files together
ip2kml
sockets/tcp/udp

make http request (GET, POST)

# System.Net.WebRequest - 
$req = [System.Net.WebRequest]::Create('http://www.devdungeon.com')
$req.Method ="GET"
$req.ContentLength = 0
$resp = $req.GetResponse()
$reader = new-object System.IO.StreamReader($resp.GetResponseStream())
$reader.ReadToEnd()

# Invoke-WebRequest - Get details about the response
$url = "http://www.devdungeon.com"
$output = "test.html"
$start_time = Get-Date
# Invoke-WebRequest -Uri $url # Prints out metadata about the response
Invoke-WebRequest -Uri $url -OutFile $output
Write-Output "Time taken: $((Get-Date).Subtract($start_time).Seconds) second(s)"


decode www json


download a file


base64 encode decode
html encode decode














