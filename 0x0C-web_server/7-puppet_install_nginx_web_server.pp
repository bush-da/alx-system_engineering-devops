# install nginx package
package { 'nginx':
  ensure => installed,
}

# create directory
file { '/etc/nginx/html':
  ensure => directory,
}

# create index.html with content hello world
file { '/etc/nginx/html/index.html':
  ensure  => file,
  content => "Hello World!\n",
}

# create 404.html with custom message
file { '/etc/nginx/html/404.html':
  ensure  => file,
  content => "Ceci n'est pas une page\n",
}

# Config Nginx

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "\
server {
  listen 80;
  listen [::]:80 default_server;

  root /etc/nginx/html;

  index index.html index.htm;

  server_name _;

  location / {
      try_files \$uri \$uri/ =404;
  }

  location /redirect_me {
    return 301 https://www.youtube.com/watch?v=AfIOBLr1NDU;
  }

  error_page 404 /404.html;

  location = /404.html {
      root /etc/nginx/html;
      internal;
  }
}
",
 require => Package['nginx'],
 notify  => Service['nginx'],
}

# define Nginx Service
service { 'nginx':
  ensure  => running,
  enable  => true,
}
