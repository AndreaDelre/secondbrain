---
name: Data Team Budget Management
applyTo:
  - "**/budget*.md"
  - "**/*-budget.md"
toolAccess:
  - activate_databricks_sql_tools
  - activate_data_retrieval_tools
  - activate_data_update_tools
description: |
  Specialized skill for managing team budget data by integrating Databricks queries
  with Google Sheets analysis and tracking.
---

# Data Team Budget Management Skill

## Overview
This skill enables efficient budget management for the data team by providing integrated access to:
- **Databricks**: `hive_metastore.preprod_digital_analytics_temporary.global_jira_tickets_enriched`
- **Google Sheets**: Budget tracking sheet (ID: `1Ll4oxjix5Z5Aufxk5BUsjEORiBFXMyE6HtceO49VDVE`)
- **Target Sheet Tabs**: `Epics`

## When This Skill Applies
✅ Opening or editing files matching:
- `budget*.md`
- `*-budget.md`

## Available Tools
This skill automatically activates:
1. **Databricks SQL Tools**: Query budget-related data
2. **Google Sheets Data Tools**: Read/write budget data (Epics tab)

---

## Workflow Patterns

### Pattern 1: Fetch Budget Data from Databricks
When you need to query budget information:

```sql
-- Query budget/financial data from the enriched tickets table
SELECT 
  column_name,
  aggregated_value
FROM hive_metastore.preprod_digital_analytics_temporary.global_jira_tickets_enriched
WHERE [your_filter_conditions]
LIMIT 50
```

**When to use**: Analyzing historical budget data, team spending patterns

### Pattern 2: Sync Databricks to Google Sheets
When you need to push analysis results to the Epics sheet:

```json
{
  "spreadsheet_id": "1Ll4oxjix5Z5Aufxk5BUsjEORiBFXMyE6HtceO49VDVE",
  "sheet_name": "Epics",
  "data": [["Column1", "Column2"], ["Value1", "Value2"]]
}
```

**When to use**: Updating budget tracking, syncing calculations

### Pattern 3: Read Budget Data from Sheets
When you need to incorporate spreadsheet data with Databricks analysis:

1. Read current sheet: `Epics` tab
2. Parse budget categories and allocations
3. Cross-reference with Databricks for actual vs budgeted

---

## Best Practices

### Before Querying Databricks
- ✅ Always preview table schema first using `mcp_databricks-mc_get_table_schema`
- ✅ Use reasonable LIMIT (50-100) for exploration
- ✅ Catalog: `hive_metastore` | Schema: `preprod_digital_analytics_temporary`

### When Working with Google Sheets
- ✅ Always read current data first with `mcp_gsheet-mcp_read_data`
- ✅ Use `Epics` tab for budget epics/high-level items
- ✅ For batch updates, use `mcp_gsheet-mcp_batch_update` instead of multiple calls
- ✅ Clear ranges before full overwrites with `mcp_gsheet-mcp_clear_range`

### Data Integrity
- 📋 Always document data sources (Databricks query or Sheet tab)
- 📋 Keep budget data organized by category/epic
- 📋 Maintain audit trail: timestamp data changes

---

## Common Tasks

### Task: "I need to see budget spent by the team"
1. Query Databricks: `SELECT team, SUM(cost) FROM ... GROUP BY team`
2. Optional: Push results to `Epics` sheet for tracking

### Task: "Update the Epics budget allocation"
1. Read current `Epics` sheet data
2. Modify allocations as needed
3. Use batch update to sync changes back

### Task: "Compare budgeted vs actual spend"
1. Pull budgeted amounts from `Epics` sheet
2. Query actual spend from Databricks
3. Create delta analysis in sheet or markdown

---

## Key Information
- **Databricks Table**: `hive_metastore.preprod_digital_analytics_temporary.global_jira_tickets_enriched`
- **Google Sheet ID**: `1Ll4oxjix5Z5Aufxk5BUsjEORiBFXMyE6HtceO49VDVE`
- **Active Tabs**: `Epics`
- **Auto-trigger Patterns**: Files, namely `budget*.md` or `*-budget.md`
