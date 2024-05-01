# Puppet manifest to install and configure Nginx web server

# Run apt-get update
exec { 'apt-update':
  command => '/usr/bin/apt-get update'
}

# Install nginx
package { 'nginx':
  ensure  => installed,
  require => Exec['apt-update'],
}

# Create a new index.html
file { 'Create index.html':
  require => Package['nginx'],
  path    => '/etc/nginx/html/index.html',
  content => 'Hello World!\n'
}

file { '/etc/nginx/html':
  ensure => directory,
}

# Create a new error page
file { 'Create 404.html':
  require => Package['nginx'],
  path    => '/etc/nginx/html/404.html',
  content => 'Ceci n\'est pas une page\n'
}

file { '/etc/nginx/sites-available/default':
  content => "server {
		listen 80;
                listen [::]:80;

		server_name _;
		root /etc/nginx/html;
		location / {
			index index.html;
			add_header X-Served-By $hostname;
		}
                location /redirect_me {
                         return 301 https://www.youtube.com/watch?v=AfIOBLr1NDU;
                }
                error_page 404 /404.html;
                location /404.html {
                         root /etc/nginx/html;
                         internal;
                }
	}",
  require => Package['nginx'],
}

exec { 'run':
  command  => 'sudo service nginx restart',
  provider => shell,
  require  => [
    File['/etc/nginx/sites-available/default'],
    Package['nginx'],
  ],
}
