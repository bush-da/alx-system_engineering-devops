# set up client SSH configuration file so that you can connect to a server without typing a password.

file { '/home/smuca/.ssh/config':
  ensure  => 'present',
  mode    => '0600',
  content => "\
  # connect to server without typing a password
  Host *
     IdentityFile ~/.ssh/school
     PasswordAuthentication no
  ",
}
