# fix an error in "phpp" extension to "php"and automate it using puppet

exec { 'fix-wordpress':
   command => "sed -i 's/.phpp/.php/' /var/www/html/wp-settings.php",
   path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
