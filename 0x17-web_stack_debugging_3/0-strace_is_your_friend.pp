# Puppet manifest to fix incorrect file extensions in WordPress configuration

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin:/bin:/usr/bin'
}
