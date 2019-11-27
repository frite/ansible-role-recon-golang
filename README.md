recon_gotools
=========

Role to install go and go tools.

Requirements
------------

None.

Role Variables
--------------

The only thing you are probably interested in is
```
Go_home_dir: /home/user
go_version: 1.13.1

```.
By default, it's set as the ansible user. 

Dependencies
------------
None.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: ansible-role-recon-gotools }

License
-------

BSD

