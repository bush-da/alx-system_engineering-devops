# install nginx package
package { 'nginx':
  ensure => installed,
}

# create a directory
file { '/etc/nginx/html':
  ensure => directory,
}

# create a file index.html with content Hello World!
file { '/etc/nginx/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

# create a file 404.html with a content
file { '/etc/nginx/html/404.html':
  ensure  => file,
  content => "Ceci n'est pas une page",
}

# config nginx
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "\
  server {
     listen 80;
     listen [::]:80;

     root /etc/nginx/html;
     index index.html index.htm;

     server_name _;

     location / {
         try_files \${uri} \${uri}/ =404;
     }

     location /redirect_me {
       return 301 https://www.youtube.com/watch?v=AfIOBLr1NDU;
     }

     error_page 404 /404.html;

     location = /404.html {
       root /etc/nginx/html;
       internal;
     }
}",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# define nginx service
Service { 'nginx':
  ensure  => running,
  enable  => true,
}
