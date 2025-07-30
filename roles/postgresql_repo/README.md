POSTGRESQL_REPO
===============

Install and manage postgresql repository

Requirements
------------

Supported OS's:
 - Debian 12

Role Variables
--------------



Dependencies
------------

None

Example Playbook
----------------

```
- hosts: servers
  tasks:
    - name: "Include rbrightling.database.postgresql_repo"
      ansible.builtin.include_role:
        name: "rbrightling.database.postgresql_repo"
```

License
-------

LGPLv3

Author Information
------------------

- Robert Brightling | [GitLab](https://gitlab.com/brightling) | [GitHub](https://github.com/rbrightling)
