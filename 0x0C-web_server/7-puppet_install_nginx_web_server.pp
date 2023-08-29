# Nginx server setup and configuration
# Define class to install and configure Nginx

class nginx_server {
  package { 'nginx':
    ensure => 'installed',
  }

  file { '/var/www/html/index.html':
    content => 'Hello World!',
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => 'file',
    content => "
      server {
        listen 80;
        server_name _;
        location / {
          root   /var/www/html;
          index  index.html;
        }
        location /redirect_me {
          return 301 https://github.com/emmanueladdo;
        }i
      }
    ",
  }

  service { 'nginx':
    ensure  => 'running',
    enable  => true,
    require => Package['nginx'],
  }
}

# Apply the class to the node
node 'default' {
  class { 'nginx_server': }
}
