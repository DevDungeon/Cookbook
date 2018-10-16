package main

import ("encoding/xml"
        "fmt"
        )

type Member struct {
    Name string `xml:"name"`
    Value string `xml:"value>string"`
}

type Result struct {
        XMLName xml.Name `xml:"methodResponse"`
        FirstValue string `xml:"params>param>value>array>data>value>string"`
        Members []Member `xml:"params>param>value>array>data>value>struct>member"`
}
func main() {
data := `
    <methodResponse>
    <params>
    <param>
    <value><array><data>
    <value><string>12345abcde12345abcde12345</string></value>
    <value><struct>
    <member>
      <name>username</name>
      <value><string>trex</string></value>
    </member>
    <member>
      <name>home</name>
      <value><string>/home</string></value>
    </member>
    <member>
      <name>mail_server</name>
      <value><string>Mailbox1</string></value>
    </member>
    <member>
      <name>web_server</name>
      <value><string>Web12</string></value>
    </member>
    <member>
      <name>id</name>
      <value><int>1234</int></value>
    </member>
    </struct></value>
    </data></array></value>
    </param>
    </params>
    </methodResponse>`

v := Result{}
err := xml.Unmarshal([]byte(data), &v)
if err != nil {
fmt.Printf("error: %v", err)
        return
}
fmt.Printf("XMLName: %#v\n", v.XMLName)
fmt.Printf("Values: %#v\n", v.FirstValue)

}