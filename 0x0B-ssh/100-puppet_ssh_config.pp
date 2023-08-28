#!/usr/bin/env bash
#puppet that edits the configuration file

file_line { 'Turn off passwd authentication':
  ensure        => present,
    path        => '/etc/ssh/ssh_config',
      line      => '    PasswordAuthentication no',
        replace => true,
}

file_line { 'set identity file':
  ensure        => present,
    path        => '/etc/ssh/ssh_config',
      line      => '     IdentityFile ~/.ssh/school',
        replace => true,
}
