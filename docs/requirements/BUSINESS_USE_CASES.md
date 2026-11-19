# Corporate Finance & Sales Intelligence Copilot
# Business Use Cases Specification

## 1. Purpose

This document defines the principal business workflows supported by the Corporate Finance & Sales Intelligence Copilot.

The system supports internal Finance and Sales operations using authorized corporate information sources. It combines structured analytics, document intelligence, deterministic calculations, and AI-assisted explanations.

## 2. Finance Use Cases

### FIN-UC-01: Financial Performance Analysis

**Primary actor:** Finance Manager

**Objective:** Analyze financial performance over a selected period.

**Inputs:**
- Reporting period
- Financial reporting dimensions
- Comparison period (optional)

**Workflow:**
1. Interpret the user's question.
2. Verify access to required financial data.
3. Retrieve relevant financial records.
4. Calculate required KPIs deterministically.
5. Compare results against previous periods or targets.
6. Validate calculations and source data.
7. Generate a summary with tables, visualizations, and evidence.

**Outputs:**
- Revenue
- Expenses
- Profit
- Profit margins
- Growth rates
- Comparisons
- Supporting sources and calculation details

**Exception handling:**
- Missing reporting periods
- Incomplete financial data
- Conflicting financial sources
- Unauthorized data access

### FIN-UC-02: Budget vs. Actual Analysis

**Primary actor:** Finance Manager / Finance Executive

**Objective:** Identify budget deviations and understand their drivers.

**Workflow:**
1. Select the reporting period and organizational dimensions.
2. Retrieve budget and actual values.
3. Align account classifications, periods, and currencies.
4. Calculate absolute and percentage variances.
5. Identify significant deviations.
6. Investigate contributing accounts or departments.
7. Retrieve relevant supporting commentary.
8. Generate a variance analysis report.

**Calculations:**

Variance = Actual - Budget

Variance % = (Actual - Budget) / Budget × 100

**Outputs:**
- Budget
- Actual
- Variance
- Variance percentage
- Significant deviations
- Drill-down analysis
- Supporting evidence

**Exception handling:**
- Missing budget
- Budget equals zero
- Inconsistent account mappings
- Incomplete actuals

### FIN-UC-03: Receivables Aging and Credit Exposure

**Primary actor:** Finance Manager / Credit Controller

**Objective:** Identify overdue balances and collection priorities.

**Workflow:**
1. Select an as-of date.
2. Retrieve customer, invoice, payment, and credit information.
3. Calculate outstanding balances.
4. Determine invoice aging.
5. Group receivables into aging buckets.
6. Calculate customer exposure.
7. Rank collection priorities.
8. Present results with supporting records.

**Suggested aging buckets:**
- Not yet due
- 1–30 days overdue
- 31–60 days overdue
- 61–90 days overdue
- More than 90 days overdue

**Outputs:**
- Customer outstanding balances
- Invoice details
- Aging buckets
- Total overdue
- Credit exposure
- Collection priority indicators

### FIN-UC-04: Finance Policy Intelligence

**Primary actor:** Finance Employee

**Objective:** Obtain reliable answers about company finance policies and procedures.

**Workflow:**
1. Interpret the question.
2. Retrieve authorized policy documents.
3. Apply metadata and permission filters.
4. Retrieve relevant passages using hybrid search.
5. Rerank evidence.
6. Verify evidence sufficiency.
7. Generate an answer with citations.

**Outputs:**
- Answer
- Relevant policy clauses
- Document name
- Page or section
- Source link where available

**Exception handling:**
- No supporting policy found
- Outdated policy
- Conflicting policies
- Restricted documents

## 3. Sales Use Cases

### SAL-UC-01: Sales Performance Analysis

**Primary actor:** Sales Manager

**Objective:** Analyze sales performance across business dimensions.

**Workflow:**
1. Identify reporting period and requested dimensions.
2. Retrieve sales transactions and relevant master data.
3. Validate data and aggregation rules.
4. Calculate revenue, quantities, growth, and other required KPIs.
5. Compare performance across dimensions.
6. Identify top and underperforming segments.
7. Generate an evidence-backed analytical response.

**Dimensions:**
- Customer
- Product
- Region
- Sales representative
- Channel
- Period

### SAL-UC-02: Customer 360 Intelligence

**Primary actor:** Sales Manager / Authorized Sales Executive

**Objective:** Build a consolidated customer view.

**Workflow:**
1. Identify the customer.
2. Retrieve customer master information.
3. Retrieve purchase history.
4. Analyze product preferences and purchasing patterns.
5. Calculate revenue trends.
6. Retrieve related customer information and documents.
7. Include authorized payment or credit information.
8. Present a consolidated customer profile.

**Outputs:**
- Customer profile
- Purchase history
- Revenue trends
- Frequently purchased products
- Purchase frequency
- Last purchase date
- Payment information where authorized
- Relevant customer documents

### SAL-UC-03: Sales Target Attainment

**Primary actor:** Sales Manager

**Objective:** Monitor progress toward sales targets.

**Workflow:**
1. Retrieve targets and actual sales.
2. Align reporting periods and organizational dimensions.
3. Calculate target achievement.
4. Calculate remaining target.
5. Identify underperforming segments.
6. Analyze historical performance.
7. Estimate required sales pace.
8. Generate a performance-gap report.

**Calculations:**

Achievement % = Actual Sales / Target × 100

Remaining Target = Target - Actual Sales

### SAL-UC-04: Sales Knowledge Assistant

**Primary actor:** Sales Executive

**Objective:** Retrieve authorized product and sales knowledge.

**Sources:**
- Product catalogs
- Product specifications
- Pricing policies
- Discount policies
- Sales procedures
- Customer onboarding documents

**Workflow:**
1. Interpret the question.
2. Retrieve relevant authorized documents.
3. Apply metadata filters.
4. Perform hybrid retrieval.
5. Rerank candidate evidence.
6. Verify evidence.
7. Generate an answer with citations.

## 4. Cross-Domain Use Cases

### CD-UC-01: Revenue Growth but Declining Profitability

**Objective:** Investigate why revenue increased while profit or margins declined.

**Required data:**
- Sales transactions
- Product costs
- Discounts
- Expenses
- Product/customer dimensions
- Historical comparison periods

**Workflow:**
1. Retrieve financial and sales data.
2. Calculate revenue and profitability metrics.
3. Compare periods.
4. Decompose changes by relevant dimensions.
5. Identify supported contributing factors.
6. Retrieve supporting management commentary.
7. Verify evidence.
8. Generate an explanation distinguishing facts from hypotheses.

### CD-UC-02: High-Revenue Customers with Overdue Balances

**Objective:** Identify customers with significant sales and overdue receivables.

**Required data:**
- Sales transactions
- Customer master
- Invoices
- Payments
- Credit terms

**Workflow:**
1. Calculate customer revenue over the requested period.
2. Calculate outstanding balances as of a defined date.
3. Calculate overdue balances and aging.
4. Combine sales and receivables.
5. Rank customers using requested criteria.
6. Present the results with source details.

### CD-UC-03: Regional Sales Target Risk

**Objective:** Identify regions likely to miss sales targets.

**Workflow:**
1. Retrieve targets and sales history.
2. Calculate current achievement.
3. Analyze historical trends.
4. Investigate regional product and customer performance.
5. Apply forecasting only if justified by sufficient data.
6. Identify possible performance risks.
7. Explain assumptions and uncertainty.
8. Generate a regional comparison.

### CD-UC-04: Monthly Management Report

**Objective:** Generate an evidence-backed business performance report.

**Report sections:**
- Executive summary
- Sales performance
- Target attainment
- Finance KPIs
- Budget variances
- Product performance
- Regional performance
- Customer performance
- Receivables and credit exposure
- Key risks
- Significant changes
- Recommendations
- Evidence and citations
- Data limitations

**Workflow:**
1. Establish reporting period.
2. Retrieve relevant datasets.
3. Calculate KPIs.
4. Compare against targets and prior periods.
5. Identify significant changes.
6. Investigate relevant drivers.
7. Retrieve supporting reports and commentary.
8. Verify metrics and evidence.
9. Generate the report.
10. Allow authorized users to review and export.

## 5. Evidence and Citation Requirements

All factual claims must be traceable to supporting evidence.

Document evidence should include:
- Document title
- Page or section
- Relevant passage
- Version where available
- Source link where available

Structured analytical evidence should include:
- Data source
- Relevant table or dataset
- Reporting period
- Applied filters
- Calculation method
- Supporting figures
- Data freshness

The system must distinguish verified findings, interpretations, assumptions, and unsupported hypotheses.

## 6. General Exception Handling

All workflows must handle:
- Missing data
- Incomplete records
- Conflicting sources
- Stale data
- Invalid reporting periods
- Unauthorized access
- Source-system failures
- Calculation errors
- Insufficient evidence

The system must not fabricate missing information or silently hide data-quality issues.

## 7. General Acceptance Criteria

A workflow is accepted when:

1. It produces the correct output for validated test data.
2. It uses authorized sources only.
3. Numerical calculations are independently verified.
4. Relevant citations or data provenance are provided.
5. Missing and conflicting information is clearly identified.
6. Unauthorized information is not exposed.
7. The workflow can be tested reproducibly.
8. Errors are handled without misleading the user.
