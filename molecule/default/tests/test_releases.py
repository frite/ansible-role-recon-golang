import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_amass_exists(host):
    ''' Assert amass was installed'''
    f = host.file('/usr/local/bin/amass')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert oct(f.mode) == '0o755'


def test_aquatone_exists(host):
    ''' Assert aquatone was installed'''
    f = host.file('/usr/local/bin/aquatone')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert oct(f.mode) == '0o755'
