Ansible Collection - rbrightling.database
=========================================

[![Ansible Galaxy](http://img.shields.io/badge/galaxy-rbrightling.database-660198.svg?style=flat)](https://galaxy.ansible.com/rbrightling/database)

Database collection of roles to manage and configure database features and security.

Roles
-----

| Roles                                                                                                         | Build Status                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [postgresql](https://github.com/rbrightling/ansible-collection-database/tree/main/roles/postgresql)           | [![rbrightling.database.postgresql](https://github.com/rbrightling/ansible-collection-database/actions/workflows/postgresql.yml/badge.svg?branch=main)](https://github.com/rbrightling/ansible-collection-database/actions/workflows/postgresql.yml)                |
| [postgresql_repo](https://github.com/rbrightling/ansible-collection-database/tree/main/roles/postgresql_repo) | [![rbrightling.database.postgresql_repo](https://github.com/rbrightling/ansible-collection-database/actions/workflows/postgresql_repo.yml/badge.svg?branch=main)](https://github.com/rbrightling/ansible-collection-database/actions/workflows/postgresql_repo.yml) |

Requirements
------------

Supported OS's:
  - Debian 12

Usage
-----

Install this ansible collection:

```bash
ansible-galaxy collection install rbrightling.database
```

Example Playbook
----------------

```yaml
---
- hosts: localhost
  tasks:
    - include_role:
        name: rbrightling.database.{{ role_name }}
```

License
-------

LGPLv3

Author Information
------------------

- Robert Brightling | [GitLab](https://gitlab.com/brightling) | [GitHub](https://github.com/rbrightling)
