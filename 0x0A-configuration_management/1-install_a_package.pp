# install flask from pip3
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# install werkzeug version 2.1.0
package { 'werkzeug':
  ensure   => '2.1.0',
  provider => 'pip3',
}
