```sh
ansible-playbook -i server_hosts playbooks/dev.yml --extra-vars "project_root=/Users/zkan/Projects/simplezat" --private-key=~/.ssh/simplezat_id_rsa
```

```sh
ansible-playbook -i server_hosts playbooks/admin.yml --extra-vars "host=dev username='zkan' password='Pronto123'" --private-key=~/.ssh/simplezat_id_rsa
```
