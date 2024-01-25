# Modify OS configuration to allow holberton user to login and open file without error message.

exec { 'increase hard file limit for holberton' :
  command => 'sed -i "/^holberton hard/s/5/5000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}

exec { 'increase soft fle limit' :
  command => 'sed -i "/^holberton soft/s/4/5000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}
