#fix the "phpp extens"

exec {'fix-estension':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:bin/'
}
