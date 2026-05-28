program getname;

Uses Crt;

var
   myString : String;

begin
   Write('Enter your name: ');
   Readln(myString);
   Writeln('Hello, ', myString, '!');
end.