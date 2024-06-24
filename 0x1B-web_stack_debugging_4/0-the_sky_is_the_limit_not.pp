# This Puppet manifest configures Nginx to handle high concurrency loads

exec { 'install_nginx':
  command => '/usr/sbin/apt-get install -y nginx',
  unless  => 'dpkg -l | grep nginx',
}

file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => template('nginx/nginx.conf.erb'),
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure => running,
  enable => true,
  require => Exec['install_nginx'],
}

