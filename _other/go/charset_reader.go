package main

import (
    "bytes"
    "fmt"
    "io"
    "os"
    "strings"
    "utf8"
    "xml"
)

type CharsetISO88591er struct {
    r   io.ByteReader
    buf *bytes.Buffer
}

func NewCharsetISO88591(r io.Reader) *CharsetISO88591er {
    buf := bytes.NewBuffer(make([]byte, 0, utf8.UTFMax))
    return &CharsetISO88591er{r.(io.ByteReader), buf}
}

func (cs *CharsetISO88591er) ReadByte() (b byte, err os.Error) {
    // http://unicode.org/Public/MAPPINGS/ISO8859/8859-1.TXT
    // Date: 1999 July 27; Last modified: 27-Feb-2001 05:08
    if cs.buf.Len() <= 0 {
        r, err := cs.r.ReadByte()
        if err != nil {
            return 0, err
        }
        if r < utf8.RuneSelf {
            return r, nil
        }
        cs.buf.WriteRune(int(r))
    }
    return cs.buf.ReadByte()
}

func (cs *CharsetISO88591er) Read(p []byte) (int, os.Error) {
    // Use ReadByte method.
    return 0, os.EINVAL
}

func isCharset(charset string, names []string) bool {
    charset = strings.ToLower(charset)
    for _, n := range names {
        if charset == strings.ToLower(n) {
            return true
        }
    }
    return false
}

func IsCharsetISO88591(charset string) bool {
    // http://www.iana.org/assignments/character-sets
    // (last updated 2010-11-04)
    names := []string{
        // Name
        "ISO_8859-1:1987",
        // Alias (preferred MIME name)
        "ISO-8859-1",
        // Aliases
        "iso-ir-100",
        "ISO_8859-1",
        "latin1",
        "l1",
        "IBM819",
        "CP819",
        "csISOLatin1",
    }
    return isCharset(charset, names)
}

func IsCharsetUTF8(charset string) bool {
    names := []string{
        "UTF-8",
        // Default
        "",
    }
    return isCharset(charset, names)
}

func CharsetReader(charset string, input io.Reader) (io.Reader, os.Error) {
    switch {
    case IsCharsetUTF8(charset):
        return input, nil
    case IsCharsetISO88591(charset):
        return NewCharsetISO88591(input), nil
    }
    return nil, os.NewError("CharsetReader: unexpected charset: " + charset)
}

func main() {
    // Print the XML comments from the test file, which should
    // contain most of the printable ISO-8859-1 characters.
    r, err := os.Open("ISO88591.xml")
    if err != nil {
        fmt.Println(err)
        return
    }
    defer r.Close()
    fmt.Println("file:", r.Name())
    p := xml.NewParser(r)
    p.CharsetReader = CharsetReader
    for t, err := p.Token(); t != nil && err == nil; t, err = p.Token() {
        switch t := t.(type) {
        case xml.ProcInst:
            fmt.Println(t.Target, string(t.Inst))
        case xml.Comment:
            fmt.Println(string([]byte(t)))
        }
    }
}