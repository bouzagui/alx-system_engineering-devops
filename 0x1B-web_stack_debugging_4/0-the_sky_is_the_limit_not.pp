exec { 'fix--for-nginx':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
}

exec { 'nginx-restart':
  command => 'service nginx restart',
  path    => '/usr/sbin/:/sbin/:/usr/local/bin/:/bin/',
}
