import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_postgresql_repo_file(host):
    postgresql_repo_file_path = "/etc/apt/sources.list.d/pgdg.list"
    postgresql_repo_file = host.file(postgresql_repo_file_path)
    assert postgresql_repo_file.exists
