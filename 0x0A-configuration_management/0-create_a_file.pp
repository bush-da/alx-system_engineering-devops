# create a file
file { '/tmp':
  ensure  => 'present',
  path    => '/tmp/school',
  mode    => '0744',
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
}
