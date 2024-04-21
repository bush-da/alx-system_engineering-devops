#!/usr/bin/env bash
# connect without password to sever
file { '/etc/ssh/ssh_config':
  ensure  => 'present',
  mode    => '0600',
  content => "\
  Host *
       IdentifyFile ~/.ssh/school
       PasswordAutentication no
  ",
}
