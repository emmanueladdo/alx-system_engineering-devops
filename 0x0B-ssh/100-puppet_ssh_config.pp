#!/usr/bin/env bash
#puppet that edits the configuration file

file { '/etc/ssh/ssh_config':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  content => "
		#SSH client\n 
		Host*\n
		IdentityFile ~/.ssh/school\n
		passwordAuthenication no\n",
}
