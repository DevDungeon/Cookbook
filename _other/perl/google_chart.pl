use Google::Chart;

  my $chart = Google::Chart->new(
    type => "Bar",
    data => [ 1, 2, 3, 4, 5 ]
  );

  print $chart->as_uri, "\n"; # or simply print $chart, "\n"

  $chart->render_to_file( filename => 'filename.png' );
