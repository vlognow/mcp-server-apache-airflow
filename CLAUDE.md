# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

A forked MCP server for Apache Airflow. Exposes Airflow REST API operations (DAGs, DAG runs, tasks, pools, variables, connections, datasets, event logs) as MCP tools. Published to PyPI and consumed by `machinify-airflow`/`machinify-airflow3` deployments, accessible at:

- Dev: `https://airflow-mcp.dev.machinify.net/sse`
- Staging: `https://airflow-mcp.stg.machinify.net/sse`
- Prod: `https://airflow-mcp.machinify.net/sse`

## Development

```bash
uv sync          # install dependencies
make test        # run tests
make lint        # ruff format + check
```

## Deployment

### Publishing to PyPI

Create a GitHub Release to trigger `publish.yml`:

```bash
gh release create vX.Y.Z --title "vX.Y.Z" --notes "..."
```

This builds the wheel/sdist and publishes to PyPI via `PYPI_API_TOKEN`.

### Updating the K8s service

The MCP server runs alongside the Airflow deployments. To roll out a new version to dev/staging/prod, bump the package version in the `machinify-airflow` or `machinify-airflow3` Helm chart values and follow those repos' standard deployment flows.
