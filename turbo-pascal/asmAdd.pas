{ Example of using inline assembly. You can directly reference Pascal variables in the assembly.}
program asmAdd;

var
  x, y, sum : Integer;

begin
  x := 10;
  y := 5;

  Asm
    mov ax, x
    add ax, y
    mov sum, ax
  end;

  Writeln('x + y = ', sum);
end.