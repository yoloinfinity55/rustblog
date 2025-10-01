+++
title = "Syncing Local and CI Environments"
date = 2025-09-30
[taxonomies]
tags = ["devops", "ci-cd", "github-actions"]
categories = ["technical"]
+++

# Keeping Local Development and GitHub Actions in Sync

Ensuring that your local development environment perfectly mirrors the environment used in your Continuous Integration (CI) pipeline is crucial for avoiding the classic "it works on my machine" problem. When these environments drift apart, you can face unexpected build failures, subtle bugs, and a lot of wasted time.

This post summarizes the process of checking and aligning the versions of key tools—Zola and Node.js—between a local machine and a GitHub Actions workflow.

### 1. How to Check Your Versions

Before you can sync your environments, you need to know what versions you're running in each.

#### Local Environment

To check your local versions, you can use the following commands in your terminal:

- **Check Zola version:**
  ```bash
  zola --version
  ```
- **Check Node.js version:**
  ```bash
  node --version
  ```

#### GitHub Actions Environment

To check the versions used in your CI pipeline, you need to inspect your workflow file, typically located at `.github/workflows/deploy.yml`.

- **Zola Version:** Look for the step that downloads Zola. The version number is usually right in the URL.
  ```yaml
  - run: |
      curl -L https://github.com/getzola/zola/releases/download/v0.21.0/zola-v0.21.0-x86_64-unknown-linux-gnu.tar.gz | tar -xz
      sudo mv zola /usr/local/bin/
  ```

- **Node.js Version:** Look for the `actions/setup-node` step, which specifies the version to use.
  ```yaml
  - uses: actions/setup-node@v3
    with:
      node-version: '22'
  ```

### 2. The Problem: Environment Drift

In our case, the checks revealed a version mismatch:

| Tool      | Local Version | GitHub Actions Version |
|-----------|---------------|------------------------|
| **Zola**  | `0.21.0`      | `v0.19.1`              |
| **Node.js** | `v22.19.0`    | `18`                   |

This drift can cause builds to fail if your code relies on features from a newer version or if a dependency requires a different Node.js environment.

### 3. The Solution: Synchronizing the Workflow

The solution is to update the `.github/workflows/deploy.yml` file to use the same versions that are confirmed to work locally.

The following changes were made:

1.  **Updated the Zola download URL** to point to version `v0.21.0`.
2.  **Updated the `node-version`** in the `setup-node` action to `22`.

By making these adjustments, we ensure that the code that runs successfully on the local machine will build and deploy reliably through the GitHub Actions pipeline.
