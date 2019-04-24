
Windows PowerShell  
==================  
Powershell commands are case insensitive!  
  
#### Index of all basic Powershell Commands
  * https://ss64.com/ps/
  
Network wake on lan packet  
  * http://www.adminarsenal.com/admin-arsenal-blog/powershell-sending-a-wake-on-lan-wol-magic-packet/  
  
#### create an alias  
Set-alias &lt;alias> &lt;command>  
Command and alias arguments cannot contain any spaces. All user aliases will be lost on exit unless added to profile.ps1  
  * Example: PS C:\> function func32 {set-location c:\windows\system32}  
    * PS C:\> set-alias cd32 func32  
#### remove an alias 
PS C:\> Remove-Item alias:&lt;alias>  
  
#### how to create a function  
function &lt;name of function> {&lt;Powershell code>}  
  * Example: PS C:\> function func32 {set-location c:\windows\system32}  
  
how to create a script  
  
file manipulation  
#### echo from file
PS C:\> Get-Content &lt;\path\to\file>
#### echo to file  
PS C:\> &lt;command generating stdout> | Out-File &lt;path\to\file>  
You can also use unix-like redirection  
  * Example:
  * Append if file exists:  
    * PS C:\> &lt;command generating stdout> >> &lt;path\to\file>  
  * Overwrite if file exists:  
    * PS C:\> &lt;command generating stdout> > &lt;path\to\file>  
  * Redirect errors and output to a file
      * PS C:\> &lt;command generating stdout> 2>&1 &lt;path\to\file>  
  * Stream Numbers:  
    * 1 = Success (Default)  
    * 2 = Error  
    * 3 = Warning  
  
cat a couple files together  
ip2kml  
sockets/tcp/udp  

make http request (GET, POST)  
  
#### System.Net.WebRequest -   
$req = [System.Net.WebRequest]::Create('http://www.devdungeon.com')  
$req.Method ="GET"  
$req.ContentLength = 0  
$resp = $req.GetResponse()  
$reader = new-object System.IO.StreamReader($resp.GetResponseStream())  
$reader.ReadToEnd()  
  
#### Invoke-WebRequest - Get details about the response  
$url = "http://www.devdungeon.com"  
$output = "test.html"  
$start_time = Get-Date 
  
#### Invoke-WebRequest -Uri $url # Prints out metadata about the response  
Invoke-WebRequest -Uri $url -OutFile $output  
Write-Output "Time taken: $((Get-Date).Subtract($start_time).Seconds) second(s)"  
  
  
decode www json  
  
  
download a file  
  
  
#### Base64  
  * #### Encode  
$Text = ‘&lt;text to encode>’  
$Bytes = [System.Text.Encoding]::Unicode.GetBytes($Text)  
$EncodedText =[Convert]::ToBase64String($Bytes)  
$EncodedText  
  * One-liner:
    * PS C:\> [Convert]::ToBase64String([System.Text.Encoding]::Unicode.GetBytes("&lt;text to encode>"))  
    
  * #### Decode  
$EncodedText = “&lt;text to decode>”  
$DecodedText = [System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String($EncodedText))  
$DecodedText  
  * One-liner:
    * PS C:\> [System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String("&lt;text to decode>"))
    
html encode decode  
