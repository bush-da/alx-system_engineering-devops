# Increase the limit of traffic Nginx server can handle

exec { 'fix-nginx':
    command => 'sed -i "s/15/65535/" /etc/default/nginx',
    path    => '/usr/local/bin/:/bin/'
}

# Restart Nginx
exec { 'restart-nginx':
    command => 'nginx restart',
    path    => '/etc/init.d/'
}