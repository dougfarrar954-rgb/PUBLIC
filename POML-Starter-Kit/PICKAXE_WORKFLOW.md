# Pickaxe Studio Workflow & Architecture

> **Best Practice**: Centralized Knowledge, Distributed Intelligence.

## 1. Studio Architecture Overview

The JP Manna Studio uses a **Hub-and-Spoke** model for knowledge management:

- **Hub**: The `knowledge-base/` folder and Studio-Level Knowledge Base.
- **Spokes**: Individual Pickaxes (Coach Lori, EventPRO, etc.) that consume specific knowledge files.

### The "Why"
- **Efficiency**: Upload once, use everywhere.
- **Consistency**: All agents quote the same source of truth.
- **Version Control**: Git tracks the history of your business logic.

---

## 2. Directory Structure

```text
JP-Manna/
├── knowledge-base/           <-- SINGLE SOURCE OF TRUTH
│   ├── business-strategy.pdf
│   ├── brand-voice.pdf
│   └── compliance-guide.docx
│
├── pickaxes/
│   ├── coach-lori-pickaxe/   <-- Agent Definition
│   │   ├── README.md         <-- Agent Manifest (Dependencies)
│   │   └── coach-lori.poml
│   │
│   ├── event-pro-pickaxe/    <-- Agent Definition
│   │   ├── README.md         <-- Agent Manifest (Dependencies)
│   │   ├── event-pro.poml
│   │   └── event-pro-toon.txt
│   │
│   └── ...
└── PICKAXE_WORKFLOW.md       <-- This Document
```

---

## 3. The Implementation Workflow

Follow this loop to update your AI Studio:

### Step 1: Edit Local Source
Modify your master documents inside the `knowledge-base/` folder.
- *Example*: Update Q3 goals in `business-strategy.pdf`.

### Step 2: Version Control (Git)
Commit your changes to lock in the version.
```bash
git add knowledge-base/
git commit -m "Updated Q3 Business Strategy docs"
git push
```

### Step 3: Platform Sync
1. Go to **Pickaxe Studio Dashboard**.
2. Navigate to **Studio Knowledge Base**.
3. **Re-upload** the modified file(s) from your local `knowledge-base/` folder.
    - *Note*: This replaces the old version for ALL agents using it.

### Step 4: Verification
Test a dependent Pickaxe (e.g., Business Strategist) to ensure it cites the new information correctly.

---

## 4. Pickaxe "Manifest" Maintenance
Every Pickaxe folder must contain a `README.md` that acts as a manifest.
**Purpose**: To track exactly which Studio Knowledge Base files are enabled for that specific agent.

### When to Update the Manifest
- **New Agent**: Create the `README.md` immediately using the standard template.
- **Changing Dependencies**: If you toggle a file ON/OFF in Pickaxe Studio builder, update the `README.md` table to match.
- **Why?** It prevents "drift" where we forget which PDF powers which agent.

---

## 5. Pickaxe Configuration

When building a new Pickaxe:
1. Go to the **Knowledge Tab** in the builder.
2. Select **"Studio Knowledge Base"**.
3. Toggle **ON** only the specific files relevant to that agent's role.

### Configuration Examples
| Agent | Enabled Files |
|-------|---------------|
| **Business Strategist** | `business-strategy.pdf`, `comp-plan.pdf` |
| **Content Creator** | `business-strategy.pdf`, `brand-voice.pdf`, `social-scripts.docx` |
| **EventPRO** | `event-playbook.pdf`, `compliance-guide.docx` |

---

## 6. Action Triggers

**Rule:** All action trigger prompts text **MUST** be stored in the central `actions/triggers.md` file.

- **Do NOT** save trigger text files inside individual Pickaxe folders (e.g., `manna-startpoint-action-trigger.txt`).
- **Do NOT** rely on memory or copy-pasting from old prompts.
- **Why?** Pickaxe Actions often share identical triggers (e.g., "Email Summary"), and editing them in one centralized place ensures valid JSON payloads and consistent behavior across all agents.
