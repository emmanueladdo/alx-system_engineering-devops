#fix the "phpp extens"

exec {'fix-estension':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/bin:/usr/sbin:/bin',
  require => Exec['restart-apache']
}

exec {'restart-apache':
  command => 'sudo service apache2 restart',
}
