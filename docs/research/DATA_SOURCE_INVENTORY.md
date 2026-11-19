# Corporate Finance & Sales Intelligence Copilot
# Data Source Inventory and Integration Requirements

## 1. Purpose

This document identifies the data sources required to support the Corporate Finance & Sales Intelligence Copilot.

It defines expected data domains, source types, integration methods, business usage, refresh requirements, access considerations, data quality requirements, and unresolved integration assumptions.

This inventory is provisional until validated with the target company's stakeholders and IT team.

---

## 2. Data Source Classification

Sources are classified into the following categories:

| Category | Description |
|---|---|
| Structured | Relational tables, transactional records, APIs returning structured data |
| Semi-structured | JSON, XML, exported reports, structured spreadsheets |
| Unstructured | PDFs, policies, contracts, reports, presentations |
| Analytical | Existing dashboards, semantic models, KPI reports |

---

## 3. Provisional Data Source Inventory

### DS-01: ERP / Financial Management System

**Business domain:** Finance

**Expected data:**
- General ledger
- Chart of accounts
- Journal entries
- Financial transactions
- Accounts payable
- Accounts receivable
- Expenses
- Financial statements
- Cost centers
- Accounting periods

**Primary use cases:**
- Financial performance analysis
- Profitability analysis
- Expense analysis
- Budget variance
- Receivables aging
- Payables analysis

**Potential integration methods:**
- Read-only database views
- Approved APIs
- Scheduled exports
- Data warehouse integration

**Expected refresh frequency:** To be determined; daily or more frequently where business requirements justify it.

**Sensitivity:** High

**Data owner:** Finance / IT

**Outstanding questions:**
- Which ERP is used?
- Can read-only access be provided?
- Are reporting views available?
- How are financial periods defined?
- Are multiple companies or subsidiaries included?
- How are currencies handled?

---

### DS-02: Sales Transaction System

**Business domain:** Sales

**Expected data:**
- Sales orders
- Order lines
- Invoices
- Sales quantities
- Net sales
- Discounts
- Returns
- Product costs
- Sales channels
- Sales representatives
- Transaction dates

**Primary use cases:**
- Sales performance
- Revenue trends
- Product analysis
- Customer analysis
- Regional performance
- Profitability analysis

**Potential integration methods:**
- ERP database
- CRM APIs
- Sales database
- Scheduled CSV/Excel extracts

**Expected refresh frequency:** Daily initially; faster refresh may be considered if justified.

**Sensitivity:** High

**Data owner:** Sales / Finance / IT

**Outstanding questions:**
- Which system is the source of truth for sales?
- Are sales orders and invoices separate?
- How are cancelled orders handled?
- How are returns and credit notes represented?
- Is revenue gross or net of discounts?
- Are costs available at transaction or product level?

---

### DS-03: Customer Master / CRM

**Business domain:** Sales / Customer Intelligence

**Expected data:**
- Customer ID
- Customer name
- Customer classification
- Industry
- Region
- Contact information
- Assigned sales representative
- Credit terms
- Customer status
- Relationship history

**Primary use cases:**
- Customer 360
- Customer segmentation
- Sales performance
- Customer purchasing history
- Customer retention analysis

**Potential integration methods:**
- CRM API
- Read-only database
- Scheduled exports

**Expected refresh frequency:** Daily or based on change frequency.

**Sensitivity:** High; personal and confidential information may be included.

**Data owner:** Sales / CRM administrator

**Outstanding questions:**
- Which CRM is used?
- What is the unique customer key?
- Are duplicate customers present?
- Are customer groups or parent-child relationships maintained?
- Which personal information is necessary for the use cases?

---

### DS-04: Product Master

**Business domain:** Sales / Operations

**Expected data:**
- Product ID
- Product name
- SKU
- Category
- Subcategory
- Brand
- Unit of measure
- Product status
- Standard cost
- Selling price
- Product hierarchy

**Primary use cases:**
- Product performance
- Product profitability
- Product mix analysis
- Product knowledge retrieval

**Potential integration methods:**
- ERP database
- Product APIs
- Scheduled exports

**Expected refresh frequency:** Daily or when master data changes.

**Sensitivity:** Internal / confidential

**Data owner:** Sales / Operations / IT

**Outstanding questions:**
- How are products categorized?
- Are product hierarchies maintained?
- Are historical product mappings available?
- Are costs and prices restricted?

---

### DS-05: Accounts Receivable and Payment Data

**Business domain:** Finance / Credit Control

**Expected data:**
- Invoice number
- Customer ID
- Invoice date
- Due date
- Invoice amount
- Outstanding amount
- Payment date
- Payment amount
- Credit notes
- Credit terms
- Credit limits

**Primary use cases:**
- Receivables aging
- Overdue customer identification
- Credit exposure
- Collection prioritization
- Customer financial risk analysis

**Potential integration methods:**
- ERP reporting views
- Finance APIs
- Scheduled extracts

**Expected refresh frequency:** Daily, subject to source-system capability.

**Sensitivity:** Highly confidential

**Data owner:** Finance / Credit Control

**Outstanding questions:**
- How are partial payments represented?
- How are disputes handled?
- How are credit notes applied?
- How is aging calculated?
- What is the agreed as-of date?
- How is customer credit exposure defined?

---

### DS-06: Budget and Planning Data

**Business domain:** Finance

**Expected data:**
- Budget period
- Account
- Department
- Cost center
- Budget amount
- Approved budget
- Revised budget
- Forecast amount
- Version

**Primary use cases:**
- Budget versus actual
- Expense variance analysis
- Departmental reporting
- Financial planning

**Potential integration methods:**
- Finance database
- Excel/CSV
- Planning system API

**Expected refresh frequency:** Monthly or when budgets are revised.

**Sensitivity:** Highly confidential

**Data owner:** Finance

**Outstanding questions:**
- Are budgets stored centrally?
- How many budget versions exist?
- Are revisions approved?
- What is the granularity of the budget?
- Are monthly budgets available?

---

### DS-07: Sales Targets and Quotas

**Business domain:** Sales

**Expected data:**
- Target period
- Sales representative
- Region
- Product/category
- Target amount
- Target quantity
- Target version

**Primary use cases:**
- Target attainment
- Sales performance gaps
- Sales forecasting
- Management reporting

**Potential integration methods:**
- CRM
- Sales planning system
- Excel/CSV

**Expected refresh frequency:** Monthly or when targets change.

**Sensitivity:** Confidential

**Data owner:** Sales Management

**Outstanding questions:**
- How are targets allocated?
- Can targets change during the period?
- Are targets available by representative, region, and product?
- What is the official target version?

---

### DS-08: Finance and Sales Policies

**Business domain:** Knowledge Management

**Expected documents:**
- Credit policies
- Payment terms
- Expense policies
- Pricing policies
- Discount approval procedures
- Sales procedures
- Customer onboarding procedures
- Finance SOPs

**Primary use cases:**
- Policy Q&A
- Procedure guidance
- Sales knowledge assistant
- Finance knowledge assistant

**Potential integration methods:**
- SharePoint
- Document management systems
- PDF ingestion
- Office document ingestion
- Approved file repositories

**Expected refresh frequency:** Event-driven or scheduled document synchronization.

**Sensitivity:** Mixed; document-level access restrictions may apply.

**Data owner:** Finance / Sales / HR / Legal / Document owners

**Outstanding questions:**
- Which version is authoritative?
- Are policies approved?
- Are documents superseded?
- Are permissions inherited?
- Are archived policies accessible?
- Can source links be preserved?

---

### DS-09: Management Reports

**Business domain:** Finance / Sales / Management

**Expected documents:**
- Monthly reports
- Quarterly reports
- Sales performance reviews
- Finance commentary
- Executive summaries
- Operational reports
- Management presentations

**Primary use cases:**
- Explanation of business trends
- Cross-domain analysis
- Historical commentary
- Management reporting

**Potential integration methods:**
- SharePoint
- PDFs
- Excel
- PowerPoint
- Reporting system exports

**Expected refresh frequency:** Monthly or when reports are published.

**Sensitivity:** Highly confidential

**Data owner:** Finance / Sales / Senior Management

**Outstanding questions:**
- Which reports are official?
- Are reports available in machine-readable formats?
- Are reported metrics consistent with source databases?
- Are historical reports retained?

---

### DS-10: Power BI Reports and Semantic Models

**Business domain:** Business Intelligence

**Expected data:**
- KPI definitions
- Measures
- Aggregated datasets
- Dashboard outputs
- Historical business metrics
- Report metadata

**Primary use cases:**
- Existing KPI reuse
- Business metric consistency
- Report comparison
- Analytical reference

**Potential integration methods:**
- Approved Power BI REST APIs
- Semantic model access
- Exported datasets
- Excel exports
- Approved report exports

**Expected refresh frequency:** Depends on source dataset refresh schedules.

**Sensitivity:** Depends on report and model permissions.

**Data owner:** BI team / IT / Business owners

**Outstanding questions:**
- Which workspaces are available?
- Is semantic model access permitted?
- Which licensing requirements apply?
- Are APIs enabled?
- Are export restrictions configured?
- Are row-level security rules applied?
- Can the copilot respect existing permissions?

**Important:** Power BI is not automatically assumed to be an accessible integration. Its capabilities must be verified with the company's administrators.

---

### DS-11: SharePoint and Corporate Document Libraries

**Business domain:** Enterprise Knowledge

**Expected data:**
- Documents
- Document metadata
- Folder structures
- Permissions
- Version information
- Created/modified timestamps

**Primary use cases:**
- Enterprise document search
- Policy retrieval
- Management report retrieval
- Evidence citations

**Potential integration methods:**
- Microsoft Graph API
- Approved SharePoint APIs
- Scheduled synchronization

**Expected refresh frequency:** Incremental synchronization where supported.

**Sensitivity:** Varies by document.

**Data owner:** IT / Document owners

**Outstanding questions:**
- Is Microsoft 365 used?
- Which SharePoint sites are in scope?
- How are permissions managed?
- Are document versions accessible?
- Are incremental updates supported?
- Are deleted documents tracked?

---

### DS-12: External or Supporting Business Data

**Business domain:** Supporting analytics

**Potential data:**
- Exchange rates
- Business calendars
- Holiday calendars
- Approved external economic indicators

**Primary use cases:**
- Currency conversion
- Time-period normalization
- Forecasting
- Contextual business analysis

**Potential integration methods:**
- Approved APIs
- Scheduled data feeds
- Controlled reference datasets

**Sensitivity:** Generally low, subject to source terms and company policy.

**Data owner:** Finance / IT

**Outstanding questions:**
- Which external data is necessary?
- Which sources are approved?
- Which exchange-rate methodology is used?
- What data licensing restrictions apply?

---

## 4. Integration Requirements

### INT-REQ-01: Read-only source access

Initial integrations must not modify source-system business records.

### INT-REQ-02: Approved integration methods

All integrations must use methods approved by the company's IT and security teams.

### INT-REQ-03: Source system identification

Every ingested dataset must identify its originating system.

### INT-REQ-04: Data freshness

The system must track:
- Last successful extraction
- Last source update where available
- Extraction timestamp
- Data coverage period
- Refresh status

### INT-REQ-05: Incremental extraction

Where supported, integrations should extract changed records instead of repeatedly processing all data.

### INT-REQ-06: Failure handling

Failed integrations must:
- Record errors
- Support retry
- Avoid duplicate ingestion
- Preserve the last valid dataset
- Clearly communicate stale data

### INT-REQ-07: Data validation

Extracted data must be validated for:
- Required fields
- Data types
- Duplicate records
- Missing identifiers
- Invalid dates
- Currency consistency
- Referential integrity
- Unexpected record counts

### INT-REQ-08: Data lineage

Every dataset and analytical result must preserve source traceability.

### INT-REQ-09: Permission enforcement

Data access must respect user roles and applicable source-system permissions.

### INT-REQ-10: Configuration

Integrations must be configurable without hardcoding credentials or business-specific connection details.

---

## 5. Data Quality Requirements

The system must evaluate:

### Completeness
Are required records and fields present?

### Accuracy
Do values match the authoritative source?

### Consistency
Are customer IDs, product IDs, currencies, dates, and definitions consistent?

### Timeliness
Is the dataset sufficiently recent for the requested analysis?

### Uniqueness
Are duplicate records or duplicated transactions present?

### Validity
Do values conform to expected data types, ranges, and business rules?

### Referential Integrity
Do transactions reference valid customers, products, accounts, and organizational dimensions?

Data quality problems must be visible and must not silently contaminate analytical outputs.

---

## 6. Data Ownership and Governance

Each source must have:
- Business owner
- Technical owner
- Approved access method
- Sensitivity classification
- Retention requirements
- Refresh schedule
- Data quality responsibility
- Access approval status

The copilot must not become the authoritative system of record for operational transactions.

---

## 7. Real Company Discovery Questionnaire

### Systems
1. Which ERP is used?
2. Which CRM is used?
3. Where are Finance and Sales transactions stored?
4. Is there an existing data warehouse?
5. Which BI tools are used?
6. Is SharePoint or another document management system available?

### Access
7. Are APIs available?
8. Can read-only database views be provided?
9. Are scheduled exports permitted?
10. Who approves access?
11. Are there restrictions on cloud AI processing?

### Finance
12. How are budgets maintained?
13. How are receivables aging reports generated?
14. Which financial KPIs are officially defined?
15. How are currencies and reporting periods handled?

### Sales
16. How are sales targets maintained?
17. What are the main sales reporting dimensions?
18. Is product cost or margin data available?
19. How are customer identities reconciled across systems?

### Documents
20. Where are approved policies stored?
21. How are document versions and permissions managed?
22. Which reports are authoritative?

### Security
23. What user roles exist?
24. Are row-level restrictions required?
25. What data classifications and retention rules apply?
26. Is on-premise or private-cloud deployment required?

---

## 8. Integration Risks

| Risk | Mitigation |
|---|---|
| No API availability | Evaluate approved exports, views, or alternate integrations |
| Inconsistent customer IDs | Develop controlled identity mapping |
| Incorrect financial definitions | Validate KPI definitions with Finance |
| Stale information | Display freshness and ingestion status |
| Missing product costs | Clearly limit profitability analysis |
| Restricted documents | Preserve permissions and filter retrieval |
| Power BI access limitations | Validate API, licensing, workspace and model access |
| Data quality issues | Establish validation and exception reports |
| Source system disruption | Use controlled extraction and minimize source load |
| Unauthorized data exposure | Enforce permissions and audit access |

---

## 9. Initial Assumptions

These assumptions are provisional and must be validated:

1. The company has at least one authoritative source for sales transactions.
2. Finance data is available through an approved extraction method.
3. Customer and product master data exists.
4. Budget and target data may be maintained separately from transactions.
5. Some business knowledge is maintained in documents.
6. Existing BI reports may provide useful KPI definitions.
7. Real company data will only be used after authorization.
8. The first implementation will prioritize controlled, read-only access.

---

## 10. Deliverable and Acceptance Criteria

This inventory is accepted when:

1. Required business data domains are identified.
2. Each data domain is mapped to relevant use cases.
3. Expected data elements are documented.
4. Potential integration methods are identified.
5. Sensitivity and ownership considerations are documented.
6. Refresh and data-quality requirements are defined.
7. Unknowns and assumptions are clearly documented.
8. The company discovery questionnaire is ready for stakeholder validation.
