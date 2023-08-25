#manifest that kills a process named killmenow
exec{'killprocess':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin', '/usr/sbin', '/bin']
}
