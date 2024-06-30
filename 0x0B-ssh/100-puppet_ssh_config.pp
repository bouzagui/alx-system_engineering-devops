#!/usr/bin/env bash
# change to config file

file ('/etc/ssh/ssh_config:
  ensure  => 'present',
)
file_line ('Turn off passwd auth':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  match   => 'PasswordAuthentication yes',
  replace => 'true',
)

file_line ('Use a Identity_File':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/config',
  match   => '^IdentityFile',
  ensure  => 'present',
)
