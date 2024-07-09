#!/usr/bin/env bash
# 2-puppet_custom_http_response_header.pp

# Ensure Nginx is installed and running
class { 'nginx':
  ensure => 'installed',
  enable => true,
  before => File['/etc/nginx/sites-available/default'],
}

# Custom fact to retrieve the hostname
$hostname_fact = $facts['hostname']

# Define the Nginx configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

# Configure Nginx service
service { 'nginx':
  ensure => running,
  enable => true,
}
