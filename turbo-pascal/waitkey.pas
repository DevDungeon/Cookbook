{ Wait for a key press, using the Crt unit. }
program waitkey;

Uses Crt;

var
   c : Char;

begin
  {Note if you press a function key like F2, or an arrow key,
   it sends two key codes
   so it will trigger BOTH ReadKey calls even though you pressed 1 key.}
  Writeln('Press any key to continue...');

  c := ReadKey;
  if c = #0 then { Check if char received was null }
     { keycode recieved was null, meaning it's an extended keycode sent in
      two bytes, like a function key F1 or an arrow. }
    Writeln('Extended keycode received. Getting second code.');
    c := ReadKey;
  Writeln('You pressed: ', c);

end.