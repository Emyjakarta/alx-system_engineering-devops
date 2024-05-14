# Install the puppetlabs-stdlib module
# class { 'stdlib': }

# Update package information
exec { 'apt-update':
  command => '/usr/bin/apt-get -y update',
    path  => ['/usr/bin', '/bin'],
#   before => Package['nginx'],
}

# Install Nginx package
    package { 'nginx':
      ensure => installed,
}

# Configure Nginx to add the custom HTTP header
#      file_line { 'add custom header':
#        ensure => present,
#    path       => '/etc/nginx/sites-available/default',
#      line     => "\tadd_header X-Served-By ${hostname};",
#        after  => 'server_name _;',
#}

# Configure Nginx to add the custom HTTP header
# file { '/etc/nginx/sites-available/default':
file { '/etc/nginx/conf.d/2-custom_response_headers.conf':
  ensure => present,
#  content => template('/home/emyjakarta273/alx-system_engineering-devops/0x0F-load_balancer/templates/nginx_default.erb'),
#  require => Package['nginx'],
content  => "add_header X-Served-By ${hostname};\n",
  notify => Service['nginx'],
}

# Ensure Nginx is running
        service { 'nginx':
          ensure => running,
#    enable       => true,
}
