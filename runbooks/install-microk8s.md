# Install MicroK8s Runbook

## Purpose

This runbook documents the first MicroK8s setup path for Agent Platform.

## Target

Use MicroK8s for the first production-like deployment environment.

Recommended host:

```text
Ubuntu 22.04 LTS or 24.04 LTS
4 vCPU / 8 GB RAM minimum
8 vCPU / 16 GB RAM preferred
100 GB+ SSD
```

## Install MicroK8s

```bash
sudo snap install microk8s --classic
```

## Add Current User to MicroK8s Group

```bash
sudo usermod -a -G microk8s $USER
sudo chown -f -R $USER ~/.kube
newgrp microk8s
```

## Check Status

```bash
microk8s status --wait-ready
```

## Enable Required Add-ons

```bash
microk8s enable dns
microk8s enable hostpath-storage
microk8s enable ingress
microk8s enable registry
microk8s enable metrics-server
```

Optional later:

```bash
microk8s enable observability
```

## Validate Cluster

```bash
microk8s kubectl get nodes
microk8s kubectl get pods -A
```

## Configure Kubectl Alias

```bash
alias kubectl='microk8s kubectl'
```

To persist:

```bash
echo "alias kubectl='microk8s kubectl'" >> ~/.bashrc
```

## Export Kubeconfig

```bash
microk8s config > ~/.kube/config
chmod 600 ~/.kube/config
```

## Namespaces

Initial namespaces:

```bash
microk8s kubectl create namespace agent-platform
microk8s kubectl create namespace agent-observability
microk8s kubectl create namespace agent-secrets
```

## Initial Services To Deploy Later

- Agent-Knowledge API
- Agent-Dashboard
- Agent-Site
- SurrealDB
- MinIO or Cloudflare R2 adapter
- Agent-Runtime
- Langfuse
- SigNoz
- Uptime Kuma
- Infisical

## Security Baseline

Before public exposure:

- SSH key-only access
- firewall enabled
- only required ports open
- ingress TLS configured
- secrets managed through Agent-Secrets / Infisical
- backups configured
- monitoring enabled

## Final Rule

```text
MicroK8s is the first always-on, production-like runtime target.
Do not expose public services until ingress, TLS, secrets, and monitoring are configured.
```
