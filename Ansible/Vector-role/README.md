Vector-role
=========

Роль для Ansible 2.10 и новее для установки Vector на ОС CentOS7 или Fedora34.

Requirements
------------

Роль работает только на дистрибутиве CentOS, Fedora. 
В файле конфигурации vector (vector.toml) необходимо указать адрес сервера базы данных clickhouse. 
Для тестирования роли может использоваться связка molecule + tox.

Role Variables
--------------

vector_version - Версия Vector

Dependencies
------------

Для работы автотеста необходимо установить molecule и vagrant.  

Example Playbook
----------------

Пример использования:

---
- name: Install vector
  hosts: all
  roles:
    - vector-role

License
-------

MIT

Author Information
------------------

[Git](https://github.com/zMaAlz/vector-role)

