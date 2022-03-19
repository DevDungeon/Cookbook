// https://wiki.lazarus.freepascal.org/Command_line_parameters_and_environment_variables
program cli_args(input, output, stdErr);

{$mode objFPC}

var

	i: integer;

begin

	writeLn({$ifDef Darwin}
			// on Mac OS X return value depends on invocation method
			'This program was invoked via: ',
		{$else}
			// Turbo Pascal-compliant paramStr(0) returns location
			'This program is/was stored at: ',
		{$endIf}
		paramStr(0));

	for i := 1 to paramCount() do
	begin
    	writeLn(i:2, '. argument: ', paramStr(i));
	end;

end.
