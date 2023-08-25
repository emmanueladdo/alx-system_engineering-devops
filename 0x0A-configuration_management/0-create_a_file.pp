#creat a file called school

$filename = 'tmp/school'

file {$filename:
  ensure  => 'present'
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet'
}
