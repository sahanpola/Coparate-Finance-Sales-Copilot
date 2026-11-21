# KPI Semantic Layer and Business Metric Definitions

## 1. Purpose

The KPI semantic layer establishes consistent, approved definitions for Finance and Sales metrics used by the Corporate Finance & Sales Intelligence Copilot.

It ensures that the same business question produces consistent calculations regardless of how a user phrases the question.

The semantic layer is the authoritative application-level definition of analytical metrics, subject to validation and approval by business owners.

## 2. Semantic Layer Responsibilities

- Define approved KPI names and descriptions.
- Define formulas and calculation rules.
- Identify authoritative source tables and columns.
- Define aggregation behaviour and grain.
- Define date fields and reporting-period rules.
- Define currency and unit handling.
- Define supported dimensions and filters.
- Define null, missing-data and edge-case behaviour.
- Record KPI ownership, approval status and version.
- Support traceability and calculation evidence.
- Enforce compatible analytical comparisons.

## 3. Initial KPI Catalogue

### Sales KPIs

| KPI ID | KPI | Provisional Formula | Dimensions |
|---|---|---|---|
| KPI-SALES-001 | Gross Sales | SUM(Gross Amount) | Date, Customer, Product, Region, Rep |
| KPI-SALES-002 | Net Sales | Gross Sales − Discounts − Returns | Date, Customer, Product, Region, Rep |
| KPI-SALES-003 | Sales Growth % | (Current − Previous) / Previous × 100 | Date, Region, Product |
| KPI-SALES-004 | Target Achievement % | Actual Sales / Sales Target × 100 | Date, Region, Product, Rep |
| KPI-SALES-005 | Target Gap | Sales Target − Actual Sales | Date, Region, Product, Rep |
| KPI-SALES-006 | Average Order Value | Sales Value / Number of Orders | Date, Customer, Region |
| KPI-SALES-007 | Quantity Sold | SUM(Sales Quantity) | Date, Product, Customer, Region |

### Finance KPIs

| KPI ID | KPI | Provisional Formula | Dimensions |
|---|---|---|---|
| KPI-FIN-001 | Gross Profit | Net Sales − COGS | Date, Product, Customer, Region |
| KPI-FIN-002 | Gross Margin % | Gross Profit / Net Sales × 100 | Date, Product, Customer, Region |
| KPI-FIN-003 | Budget Variance | Actual − Budget | Period, Account, Department |
| KPI-FIN-004 | Budget Variance % | Variance / Budget × 100 | Period, Account, Department |
| KPI-FIN-005 | Outstanding Receivables | Sum Outstanding Balances | Customer, Period, Company |
| KPI-FIN-006 | Overdue Receivables | Sum Overdue Outstanding Balances | Customer, Aging Bucket, Period |
| KPI-FIN-007 | Overdue % | Overdue AR / Total AR × 100 | Period, Customer, Company |
| KPI-FIN-008 | Collection Rate | Collections / Defined Collection Base × 100 | Period, Customer, Region |

All formulas and definitions require business validation before production use.

## 4. KPI Definition Metadata

Every KPI definition must include:

- KPI identifier.
- Name.
- Description.
- Business domain.
- Formula.
- Source table and columns.
- Fact table grain.
- Aggregation method.
- Date field and period rules.
- Currency and unit.
- Supported dimensions.
- Required filters.
- Null and missing-data rules.
- Business interpretation.
- KPI owner.
- Approval status.
- Definition version.
- Effective date.
- Known limitations.

## 5. Reporting Period Rules

The analytics engine must support:

- Calendar day, week, month, quarter and year.
- Explicit date ranges.
- Current and previous periods.
- Year-over-year comparisons.
- Month-to-date and year-to-date where appropriate.
- Fiscal calendars when required.
- Reporting cutoff dates.
- Time zone and date-boundary handling.

Date comparisons must use compatible periods and clearly identify the selected period.

## 6. Currency and Unit Rules

- Identify transaction currency.
- Identify reporting currency.
- Use approved exchange rates and conversion dates.
- Preserve original amounts where required.
- Do not combine incompatible currencies without conversion.
- Identify units for quantities and other measurements.
- Display currency and units with analytical results.

## 7. KPI Calculation and Edge-Case Rules

- Prevent division by zero.
- Distinguish missing values from zero.
- Handle duplicate records according to validated source rules.
- Exclude cancelled transactions according to approved definitions.
- Apply credit notes, returns and adjustments consistently.
- Flag missing cost information.
- Handle late-arriving transactions.
- Validate dimensions before comparing targets and actuals.
- Report incomplete or stale data.
- Preserve authorization filters.

## 8. KPI Interpretation Rules

Metric interpretation depends on business context.

Examples:

- Positive revenue variance is generally favourable.
- Positive expense variance is generally unfavourable.
- Gross margin is undefined when net sales are zero.
- Sales growth is undefined when the previous period is zero.
- Target achievement greater than 100% indicates exceeding the target.
- Higher overdue receivables may indicate increased collection risk.

The system must not label financial variances favourable or unfavourable without considering KPI classification and the approved business rules.

## 9. Semantic Query Resolution

For each analytical question, the system should resolve:

1. Metric.
2. Business domain.
3. Date period.
4. Comparison period.
5. Aggregation.
6. Dimensions.
7. Filters.
8. Currency and units.
9. User permissions.
10. Required evidence and calculation trace.

Ambiguous metric definitions or periods should trigger clarification when they materially affect the result.

## 10. Evidence and Calculation Traceability

Every analytical answer should identify where applicable:

- KPI definition and version.
- Source dataset and table.
- Selected period.
- Filters applied.
- Grouping dimensions.
- Query or calculation reference.
- Input values.
- Formula.
- Output value.
- Refresh timestamp.
- Data quality warnings.

The AI explanation must be based on the verified analytical result.

## 11. Governance and Ownership

- Finance owns or approves financial KPI definitions.
- Sales owns or approves commercial KPI definitions.
- Data and IT teams maintain technical implementation.
- Definition changes must be version-controlled.
- KPI changes must be reviewed and tested.
- Historical comparisons must account for definition changes.

## 12. Open Decisions

1. Official definition of revenue and net sales.
2. Treatment of discounts, returns and credit notes.
3. Authoritative cost and gross profit calculation.
4. Fiscal calendar.
5. Reporting currency and conversion methodology.
6. Budget versions and approval rules.
7. Sales target allocation methodology.
8. Collection rate definition.
9. AR aging methodology.
10. KPI owners and approval workflow.
11. Existing Power BI measures to reuse or validate.
12. Required KPI history and definition-version behaviour.

## 13. Acceptance Criteria

- Core Finance and Sales KPIs are catalogued.
- Formulas are explicitly documented.
- KPI metadata is defined.
- Dimensions and date logic are identified.
- Currency and unit handling are addressed.
- Edge cases are documented.
- Metric interpretation is addressed.
- Evidence and traceability requirements are included.
- KPI governance and versioning are documented.
- Unresolved business definitions remain clearly marked pending approval.