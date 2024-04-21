# Connect to server without password Config
file { '/etc/ssh/ssh_config':
  ensure  => 'present',
  mode    => '0600',
  content => "
Host *
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
",
}
