# My POML Style Guide (For Small Projects & Pickaxe Integration)

## Core Structure (Always Use This Order)
<role>Define the AI persona clearly (1 sentence)</role>
<task>List 1-3 specific actions (bullet points)</task>
<cp caption="Constraints">3-5 hard rules (numbered)</cp>
<cp caption="Output Format">Markdown tables/lists only</cp>

## Required Tags for My Workflow
- <Document src="api_endpoint" preprocess="json"> for Python APIs
- <table headers="true"> for data extraction
- <example> blocks with 1-2 few-shot examples
- {{ variable }} substitution: snake_case only (e.g., {{ project_name }})

## Naming & Organization Rules
- Files: lowercase-with-dashes.poml
- Sections: [section: UPPERCASE]
- Variables: {{ input_data }}, {{ output_path }}
- Git folder: /prompts/{project_name}/

## Prohibited Patterns
- No <img> tags (text-only projects)
- No complex CSS styling
- Max 500 lines per POML file
- No advanced React processing unless specified

## Standard Functionality Blocks

### Email Summary Protocol
*Insert this block into your `<stepwise-instructions>` or `<operational_directives>` section.*

```xml
<stepwise-instructions caption="Email Summary Protocol">
    <list>
        <item><b>Trigger:</b> If a user asks for an email summary.</item>
        <item><b>Memory Check:</b> Check User Memories for stored email. If missing, ask user.</item>
        <item><b>Action:</b> IMMEDIATELY trigger 'Email User' action once email is known.</item>
        <item><b>Rule:</b> Do NOT write the summary in chat. Generate it ONLY as the action payload.</item>
        <item><b>Formatting:</b>
            <list>
                <item>Clear Subject Line.</item>
                <item>Opening Paragraph (Vision Summary).</item>
                <item>Bulleted Key Points.</item>
                <item>Organized Sections with Bold Headers.</item>
                <item>Use HTML tags (&lt;p&gt;, &lt;ul&gt;, &lt;li&gt;, &lt;b&gt;) for structure.</item>
            </list>
        </item>
    </list>
</stepwise-instructions>
```

## Example Template (Copy-Paste Ready)
<role>You are a Git workflow expert for solo developers.</role>
<task>
- Review my git commands
- Suggest only beginner commands
</task>
<cp caption="Constraints">
1. Only use: git init, add, commit, push, pull, status
2. Never suggest rebase or merge
</cp>
<cp caption="Output Format">Checklist format</cp>

## Integration with Pickaxe
- Store in Pickaxe as "system prompt"
- Version with Git tags: v1.0-project-name
- Link to Python API examples in /examples/
