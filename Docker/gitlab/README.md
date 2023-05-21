# Манифест для развертывания Gitlab

Для регистрации gitlab-runner в контейнере запускаем команду

```bash
gitlab-runner register \
     --name docker-runner \
     --registration-token <TOKEN> \
     --config /etc/gitlab-runner/config.toml \
     --template-config /srv/config.template.toml \
     --non-interactive \
     --tag-list docker,linux 
```
