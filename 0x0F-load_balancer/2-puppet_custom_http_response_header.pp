# Puppet manifest to install and configure nginx server

# Install nginx package
package { 'nginx':
  ensure => installed,
}

# Create directory for HTML files
file { '/etc/nginx/html':
  ensure => directory,
}

# Create index.html with "Hello World!"
file { '/etc/nginx/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

# Create 404.html with custom message
file { '/etc/nginx/html/404.html':
  ensure  => present,
  content => 'Ceci n\'est pas une page',
}

# Modify nginx configuration
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "
    server {
        listen 80;

        root /etc/nginx/html;

        add_header X-Served-By $hostname;

        location /redirect_me {
            return 301 https://www.youtube.com/watch?v=AfIOBLr1NDU;
        }

        error_page 404 /404.html;
        location /404 {
            internal;
            root /etc/nginx/html;
        }
    }
  ",
  require => Package['nginx'],
}

# Ensure nginx service is running and reload configuration if needed
service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  subscribe  => File['/etc/nginx/sites-available/default'],
}
