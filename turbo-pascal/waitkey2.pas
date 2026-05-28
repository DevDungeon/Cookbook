program waitkey2;
{ Waits for keypress without using Crt unit.

  Uses BIOS interrupt 16h which is the keyboard interrupt.

  In the high part of AX reg (AH), provide the function code to
  specify what you want to do.

  00h = Read key
  01h = Check key status
  02h = Get shift flags
  10h = Read expanded keyboard buffer
  11h = Obtain status of expanded keyboard buffer
  12h = Get expanded keyboard status
}

var
  keyCode, extKeyCode : Char;

begin
  Writeln('Press any key to continue...');

  Asm
    xor ax, ax {Set AX to 00h. Alternatively use mov AH, 00h}
    int 16h
    mov keyCode, al {Store AL in Pascal variable}
    mov extKeyCode, ah
  end;

  if keyCode = #0 then
  begin
    Writeln('Key was null, so extended key was received.');
    Writeln('Checking AH for second byte.');
    Writeln('Extended ScanCode: ', extKeyCode);
  end
  else
    Writeln('You pressed, "', keyCode, '"');

{ NOTE if the mouse cursor breaks after running this program, include the
  "uses Crt;" and it will properly restore the mouse. }

end.