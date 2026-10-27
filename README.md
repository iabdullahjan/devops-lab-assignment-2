# DevOps Lab Assignment 2

Mian Abdullah Jan (FA23-BSE-019), CSC418 DevOps

Builds the Lab Assignment 1 Python app (port 8080) with GitHub Actions and publishes it to Docker Hub in two ways:

- `.github/workflows/docker-commands.yml` uses `docker login`, `docker build` and `docker push` shell commands and publishes `abdullahjan019/bse_19_commands:latest`
- `.github/workflows/docker-actions.yml` uses `docker/login-action`, `docker/setup-buildx-action` and `docker/build-push-action` and publishes `abdullahjan019/bse_19_actions:latest`

Run the image locally:

```
docker run -p 8080:8080 abdullahjan019/bse_19_commands:latest
```
