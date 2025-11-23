import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_postgresql_installed(host):
    postgresql_package_name = "postgresql-17"
    postgresql_package = host.package(postgresql_package_name)
    assert postgresql_package.is_installed


def test_postgresql_service(host):
    service_name = "postgresql"
    service = host.service(service_name)
    assert service.is_running
    assert service.is_enabled
