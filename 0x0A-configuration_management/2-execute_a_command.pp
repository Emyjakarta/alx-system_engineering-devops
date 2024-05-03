# Ensure the killmenow process is killed

exec { 'killmenow':
  command => '/usr/bin/pkill killmenow',
    path  => ['/usr/bin', '/bin'], # Specify the path to pkill if needed
  }

