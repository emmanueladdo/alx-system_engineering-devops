#puppet that edits the configuration file 
exec {'Turn off passwd auth':
  comand => 'bash -c "echo PasswordAuthentication no >> /etc/ssh/ssh_config"',
  path   => '/usr/bin:/usr/sbin:/bin'
}
exec {'Assign Identity file':
  command => 'bash -c "echo IdentityFile \'~/.ssh/school\' >> /etc/ssh/ssh_config"',
  path    => '/usr/bin:/usr/sbin:/bin'
}
exec {'Turn on pubkey auth':
  command => 'bash -c "echo PubkeyAuthentication yes >> /etc/ssh/ssh_config"',
  path    => '/usr/bin:/usr/sbin:/bin'
}
