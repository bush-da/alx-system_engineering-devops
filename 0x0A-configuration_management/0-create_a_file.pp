# create a file
file { 'school':
  ensure  => 'present',
  path    => '/tmp/school',
  mode    => '0744',
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
}
