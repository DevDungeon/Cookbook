{ Loops and handles key presses }
program iskeydown;

Uses Crt;

var
  key : Char;

begin
  clrscr;
  Writeln('Press any key to continue. Press "q" to quit.');
  repeat
    if KeyPressed then
    begin
      Writeln('Key pressed!');
      key := ReadKey; { KeyPressed will continue to be true until ReadKey }
      if key = #0 then { If key is null, 2-byte keycode }
        Writeln('Extended key: 00 + ', ReadKey)
      else
        Writeln('Key: ', key);
    end;
    delay(100); { reduce CPU load a little }

  until key = 'q';
  Writeln('Quitting.');
end.