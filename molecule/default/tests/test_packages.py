import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_curl_exists(host):
    ''' Assert curl package was installed'''
    f = host.package('curl')

    assert f.is_installed


def test_tar_exists(host):
    ''' Assert tar package was installed'''
    f = host.package('tar')

    assert f.is_installed


def test_zip_exists(host):
    ''' Assert zip package was installed'''
    f = host.package('zip')

    assert f.is_installed


def test_unzip_exists(host):
    ''' Assert unzip package was installed'''
    f = host.package('unzip')

    assert f.is_installed
