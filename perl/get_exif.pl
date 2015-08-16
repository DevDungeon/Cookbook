# use Image::ExifTool qw(:Public);
# my $info = ImageInfo('123.jpg');
# foreach (keys %$info) {
# 	print "$_ => $$info{$_}\n"
# }
#


use Image::ExifTool;
my $exifTool = new Image::ExifTool;
my $sourceImageFileName = '123.jpg';
my $info = $exifTool->ImageInfo($sourceImageFileName);

# Print all key/value pairs
foreach (keys %$info) {
	print "$_ => $$info{$_}\n";
}

# Get a specific tag value
$value = $exifTool->GetValue('ImageSize');

# Set a new value for a tag
$exifTool->SetNewValue('FileModifyDate', '1992:08:01 06:33:23-04:00');

# Write new meta information to a file
$success = $exifTool->WriteInfo($sourceImageFileName, 'dest.jpg');

my $info = $exifTool->ImageInfo('dest.jpg');
# Print all key/value pairs
foreach (keys %$info) {
	print "$_ => $$info{$_}\n";
}
