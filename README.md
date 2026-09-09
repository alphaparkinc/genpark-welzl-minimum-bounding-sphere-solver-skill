# genpark-welzl-minimum-bounding-sphere-solver-skill

[![Agentic Skill](https://img.shields.io/badge/GenPark-Agentic__Skill-blue.svg)](https://github.com/alphaparkinc/genpark-welzl-minimum-bounding-sphere-solver-skill)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)](https://python.org)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-0%20Pip-orange.svg)](#)
[![Dual Org Verified](https://img.shields.io/badge/GitHub-Dual__Org-purple.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> Welzl's randomized linear-time algorithm computing the unique exact Minimum Enclosing Ball (MEB) / Smallest Enclosing Disk in 2D and 3D.

## Architecture Overview

```mermaid
flowchart TD
    A[Agentic AI / Spatial Engine] -->|Points / Meshes / Rays| B[MCP Server / Client]
    B --> C[genpark-welzl-minimum-bounding-sphere-solver-skill Spatial Kernel]
    C --> D[Geometric Partitioning / Ray Tests / Convex Solver]
    D --> E[Exact Intersection & Bounds Output]
    E -->|Structured Payload| A
```

## Features
- **0 External Pip Dependencies**: Pure Python standard library implementation.
- **MCP Protocol Ready**: Includes Model Context Protocol server script (`mcp_server.py`).
- **Production Standard**: Comprehensive geometric test cases, sub-millisecond execution.

## Quick Start
```bash
python example_usage.py
```
