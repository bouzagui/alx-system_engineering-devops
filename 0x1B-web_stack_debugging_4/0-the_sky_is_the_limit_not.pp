exec { 'fix--for-nginx':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  path    => 'shell',
}

exec { 'nginx-restart':
  command => 'service nginx restart',
  path    => 'shell',
}
