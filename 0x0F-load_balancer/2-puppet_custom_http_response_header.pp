# Install nginx package
package { 'nginx':
  ensure => installed,
}

# Create a directory for HTML files
file { '/etc/nginx/html':
  ensure => directory,
}

# Create index.html with default content
file { '/etc/nginx/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

# Create 404.html with custom content
file { '/etc/nginx/html/404.html':
  ensure  => file,
  content => "Ceci n'est pas une page",
}

# Configure nginx server
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "\
# Default server configuration
server {
	listen 80;
	listen [::]:80;

	# Add custom header X-Served-By
	add_header X-Served-By $hostname;

	# Set root directory
	root /etc/nginx/html;

	index index.html index.htm index.nginx-debian.html;

	server_name _;

	# Error handling
	error_page 404 /404.html;
	location = /404.html {
		root /etc/nginx/html;
		internal;
	}

	# Redirection
	location /redirect_me {
		return 301 https://www.youtube.com/watch?v=AfIOBLr1NDU;
	}

	# Serve files
	location / {
		try_files \${uri} \${uri}/ =404;
	}
}
",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Ensure nginx service is running
service { 'nginx':
  ensure  => running,
  enable  => true,
}
