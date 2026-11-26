# Agent Architecture

## Core Components

### Email Agent

Classifies incoming requests.

### Task Router

Determines workflow destination.

### Workflow Orchestrator

Coordinates workflow execution.

### Memory Agent

Stores interaction context.

### Tool Manager

Exposes available tools.

### Human Approval Layer

Handles high-risk decisions.

---

## Workflow

Incoming Request

↓

Email Agent

↓

Task Router

↓

Workflow Orchestrator

↓

Specialised Agent

↓

Human Approval (if required)

↓

Action Execution

↓

Audit Logging
