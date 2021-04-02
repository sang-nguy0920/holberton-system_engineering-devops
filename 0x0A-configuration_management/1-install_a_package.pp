# install a package with gem

package {'puppet-lint':
    ensure   => '2.1.1',
    provider => 'gem',
}
