program cli_args;

var
   I : Word;

begin
     {ParamCount has the number of CLI args. 0 if none are provided}
     {ParamStr has the arguments provided}
     Writeln('You provided ', ParamCount, ' parameters.');
     for I := 1 to ParamCount do
         Writeln(ParamStr(I));
end.