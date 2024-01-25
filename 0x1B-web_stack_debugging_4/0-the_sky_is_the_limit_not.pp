# Fix nginx by modifying the amouunt of trafic it can handle

exec { 'modify max limit':
  command => 'sed -i "s/15/10000/" /etc/default/nginx',
  path   => '/usr/local/bin/:/bin/',
}

# Restart Nginx
exec { 'nginx-restart' :
  command => '/etc/init.d/nginx restart',
  path    => 'etc/init.d/',
}
