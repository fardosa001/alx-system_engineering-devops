# fix an error in "phpp" extension to "php"
# automate it using puppet

exec { 'fix-wordpress':
   command => "sed -i 's/.phpp/.php/' /var/www/html/wp-settings.php",
   path    => "/usr/local/bin/:/bin/"
}
