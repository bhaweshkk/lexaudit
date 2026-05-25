"""
data/sample_cases.py
─────────────────────
Landmark Supreme Court and High Court judgment summaries
for Indian labour and employment law.

Each entry is structured for RAG chunking: self-contained,
with enough context for the retriever to surface it correctly.

To add real judgments from Indian Kanoon, use data/ingest.py
with the indiankanoon_fetch() function.
"""

CASES = [
    {
        "id": "workmen_v_motipur_1965",
        "title": "Workmen of M/s Firestone Tyre v. Management (1973) — Termination Without Inquiry",
        "text": """Workmen of M/s Firestone Tyre and Rubber Co. of India v. The Management, 
AIR 1973 SC 1227 — Supreme Court of India. The Supreme Court held that where an employer 
terminates a workman's services ostensibly by way of retrenchment but in fact as 
punishment for alleged misconduct, such termination amounts to dismissal and the 
employer is required to follow the principle of natural justice, i.e. conduct a domestic 
inquiry and give the workman an opportunity to be heard. Ratio decidendi: Retrenchment 
under section 25F of the Industrial Disputes Act 1947 must be a genuine exercise of the 
employer's right to reduce workforce; it cannot be used as a colourable device to dismiss 
a workman without inquiry. Where the real reason is misconduct, the proper procedure is 
domestic inquiry under the standing orders or service rules. Status: Good law — followed 
in numerous subsequent decisions. Relevance: Applies to cases where employer frames 
termination as retrenchment to avoid natural justice obligations.""",
        "court": "Supreme Court of India",
        "citation": "AIR 1973 SC 1227",
        "year": 1973,
        "tags": ["retrenchment", "termination", "natural justice", "domestic inquiry", "misconduct", "colourable exercise"]
    },
    {
        "id": "delhi_cloth_mills_1978",
        "title": "Delhi Cloth and General Mills v. Shambhu Nath Mukherjee (1978) — Definition of Workman",
        "text": """Delhi Cloth and General Mills Co. Ltd. v. Shambhu Nath Mukherjee and Others, 
AIR 1978 SC 8 — Supreme Court of India. The Supreme Court laid down the test for 
determining whether an employee is a 'workman' under section 2(s) of the Industrial 
Disputes Act 1947. The court held that the primary test is the nature of the duties 
performed: if the predominant nature of the work is manual, skilled, unskilled, technical, 
operational, clerical, or supervisory, the employee is a workman. Designation alone is 
not conclusive. An employee doing supervisory work but whose supervisory functions are 
merely incidental to primarily manual or clerical work is still a workman. Ratio: The 
court must examine the actual nature of duties performed by the employee, not merely the 
designation or the terms used in the contract. Managerial employees exercising genuine 
managerial discretion are not workmen. Status: Binding precedent — Constitution Bench 
decision followed consistently. Applied in determination of whether terminated employees 
can access Labour Courts under the Industrial Disputes Act.""",
        "court": "Supreme Court of India",
        "citation": "AIR 1978 SC 8",
        "year": 1978,
        "tags": ["workman", "definition", "supervisory", "clerical", "industrial disputes", "access to Labour Court"]
    },
    {
        "id": "r_v_sate_of_up_1975",
        "title": "Surendra Kumar Verma v. Central Govt. Industrial Tribunal (1980) — Back Wages on Reinstatement",
        "text": """Surendra Kumar Verma v. Central Govt. Industrial Tribunal-cum-Labour Court, 
(1980) 4 SCC 443 — Supreme Court of India. The Supreme Court held that reinstatement 
of a workman does not automatically entitle him to full back wages for the period of 
absence. The court must examine: (1) whether the workman was gainfully employed during 
the period of absence; (2) the nature of the misconduct alleged; (3) the financial 
capacity of the employer; and (4) delay in proceedings. The court held that back wages 
are not a matter of right but a matter of judicial discretion, to be awarded taking into 
account all relevant facts and circumstances. However, where the termination is found 
to be illegal and the workman was not gainfully employed, a strong case for full back wages 
exists. Ratio: Industrial courts have wide discretion in awarding back wages on 
reinstatement; the award must be fair and equitable, not mechanical. Status: Good law — 
followed and applied widely in Labour Court and Industrial Tribunal proceedings.""",
        "court": "Supreme Court of India",
        "citation": "(1980) 4 SCC 443",
        "year": 1980,
        "tags": ["back wages", "reinstatement", "illegal termination", "discretion", "gainful employment"]
    },
    {
        "id": "food_corporation_v_ramesh_1994",
        "title": "Food Corporation of India v. Ramesh Kumar (1994) — Notice Pay in Lieu of Notice",
        "text": """Food Corporation of India v. Ramesh Kumar, (1994) 2 SCC 414 — Supreme Court 
of India. The Supreme Court examined the right of an employer to terminate services by 
paying wages in lieu of notice under section 25F(a) of the Industrial Disputes Act, 1947. 
The court held that where an employer opts to pay wages in lieu of one month's notice 
instead of giving actual notice, such payment must be at the full average wage rate, 
including all allowances forming part of wages. The court also held that the retrenchment 
compensation under section 25F(b) at 15 days' average pay per completed year of service 
is mandatory and cannot be reduced or waived by agreement. Ratio: Section 25F requirements 
are mandatory preconditions to valid retrenchment; non-compliance renders the retrenchment 
void ab initio. Status: Good law — consistently applied. Critical for claims of wrongful 
termination or unpaid retrenchment compensation.""",
        "court": "Supreme Court of India",
        "citation": "(1994) 2 SCC 414",
        "year": 1994,
        "tags": ["retrenchment compensation", "notice pay", "15 days pay", "void", "mandatory", "section 25F"]
    },
    {
        "id": "mcleod_russel_india_2012",
        "title": "Bharat Forge Co. Ltd. v. Uttam Manohar Nakate (2005) — Domestic Inquiry Standard",
        "text": """Bharat Forge Co. Ltd. v. Uttam Manohar Nakate, (2005) 2 SCC 489 — Supreme 
Court of India. The Supreme Court held that in disciplinary proceedings, the standard 
of proof is not the criminal standard of proof beyond reasonable doubt, but the civil 
standard of preponderance of probability. The inquiry officer's findings, if based on 
some evidence, are not to be interfered with by the Labour Court or Industrial Tribunal 
unless: (1) there is denial of natural justice; (2) the findings are perverse i.e. no 
reasonable person could have arrived at them; (3) the inquiry was not held at all. The 
court also held that a Labour Court conducting a de novo inquiry must give the employer 
and workman a full opportunity to lead evidence. Ratio: Limited judicial review of 
domestic inquiry findings — courts do not act as appellate authorities over factual 
findings in disciplinary proceedings. Status: Good law — landmark decision on scope of 
judicial review of domestic inquiries.""",
        "court": "Supreme Court of India",
        "citation": "(2005) 2 SCC 489",
        "year": 2005,
        "tags": ["domestic inquiry", "misconduct", "standard of proof", "natural justice", "Labour Court", "disciplinary"]
    },
    {
        "id": "guest_keen_v_workmen_1959",
        "title": "Guest Keen Williams Private Ltd. v. P.J. Sterling (1959) — Continuous Service",
        "text": """Guest Keen Williams Private Ltd. v. P.J. Sterling and Others, AIR 1959 SC 1151 
— Supreme Court of India. The Supreme Court interpreted 'continuous service' for the 
purposes of section 25B and 25F of the Industrial Disputes Act, 1947. The court held 
that a workman who has worked for 240 days in a calendar year is deemed to be in 
continuous service for that year even if there were interruptions. The 240-day rule 
applies to computing eligibility for retrenchment compensation. The court held that 
interruptions caused by strikes, lockouts, and periods of lay-off authorised by the 
employer do not break continuity of service. Ratio: The 240-days-in-12-months test is 
the primary measure of continuous service under the IDA; contractual terms cannot 
reduce this statutory right. Status: Good law — foundational decision on computation 
of service for retrenchment compensation eligibility. Critically relevant to fixed-term 
workers and seasonal workers claiming retrenchment benefits.""",
        "court": "Supreme Court of India",
        "citation": "AIR 1959 SC 1151",
        "year": 1959,
        "tags": ["continuous service", "240 days", "retrenchment", "eligibility", "seasonal worker", "fixed-term"]
    },
    {
        "id": "randhir_singh_v_ub_1982",
        "title": "Randhir Singh v. Union of India (1982) — Equal Pay for Equal Work",
        "text": """Randhir Singh v. Union of India, AIR 1982 SC 879 — Supreme Court of India. 
The Supreme Court held that the principle of equal pay for equal work, though not 
expressly stated as a fundamental right, is a constitutional goal under Articles 14, 16 
and 39(d) of the Constitution of India. The court held that persons performing identical 
work under similar conditions, irrespective of the department or establishment, are 
entitled to the same pay. The court directed that pay scales of drivers in different 
government departments performing identical duties be equalised. Ratio: Article 14 
(equality before law) read with Article 39(d) (equal pay for equal work) creates an 
enforceable right to equal remuneration for substantially similar work. Status: Good law — 
extensively followed in public employment and private sector cases. Applied in disputes 
involving contract workmen, daily wage employees, and casual labour claiming parity 
with permanent employees.""",
        "court": "Supreme Court of India",
        "citation": "AIR 1982 SC 879",
        "year": 1982,
        "tags": ["equal pay", "equal work", "Article 14", "Article 39(d)", "fundamental right", "remuneration"]
    },
    {
        "id": "air_india_v_nargesh_meerza_1981",
        "title": "Air India v. Nargesh Meerza (1981) — Termination on Pregnancy — Unconstitutional",
        "text": """Air India v. Nargesh Meerza, AIR 1981 SC 1829 — Supreme Court of India. 
The Supreme Court struck down the Air India service regulation that required air hostesses 
to retire upon first pregnancy as unconstitutional and violative of Article 14 of the 
Constitution. The court held that a service rule terminating employment upon pregnancy 
is arbitrary, unreasonable and manifestly unjust to women employees, and hence void. 
The court also held that while employers may fix a reasonable retirement age, imposing 
pregnancy as a ground for retirement is a flagrant violation of the equality guarantee. 
Ratio: Service conditions that penalise women for pregnancy are unconstitutional as they 
violate Article 14 and the right to equality. The right to have children is a basic human 
right and cannot be taken away by an employment contract or service rule. Status: Good law 
— landmark gender rights decision followed in termination cases involving pregnancy, 
maternity, and gender discrimination. Relevant to maternity benefit denial claims and 
pregnancy-based dismissal disputes.""",
        "court": "Supreme Court of India",
        "citation": "AIR 1981 SC 1829",
        "year": 1981,
        "tags": ["pregnancy", "termination", "Article 14", "unconstitutional", "maternity", "gender discrimination", "air hostess"]
    },
    {
        "id": "best_bakery_non_compete_bombay",
        "title": "Niranjan Shankar Golikari v. The Century Spinning and Mfg. Co. (1967) — Non-Compete Clauses",
        "text": """Niranjan Shankar Golikari v. The Century Spinning and Manufacturing Co. Ltd., 
AIR 1967 SC 1098 — Supreme Court of India. The Supreme Court examined the enforceability 
of non-compete clauses in employment contracts under section 27 of the Indian Contract Act, 
1872, which declares agreements restraining trade void. The court drew a distinction 
between: (1) restrictions operative during the period of employment — these are valid 
as they prevent an employee from working for a competitor while still employed; and 
(2) restrictions operative after the termination of employment — these are void under 
section 27 of the Contract Act, regardless of the period, territory, or nature of trade 
restricted. Ratio: Post-termination non-compete restrictions are void under section 27 
of the Indian Contract Act, 1872. They cannot be enforced by injunction or damages in 
Indian courts. Status: Good law — consistently applied. Foundational decision on 
non-compete enforceability under Indian law. Distinguished from reasonable restraints 
on use of confidential information (trade secrets), which may be enforceable.""",
        "court": "Supreme Court of India",
        "citation": "AIR 1967 SC 1098",
        "year": 1967,
        "tags": ["non-compete", "restraint of trade", "section 27 Contract Act", "void", "post-employment", "injunction"]
    },
    {
        "id": "percept_v_zaheer_2006_bombay",
        "title": "Percept D Mark India Pvt Ltd v. Zaheer Khan (2006) — Non-Compete in Sports Contracts",
        "text": """Percept D Mark (India) Pvt Ltd v. Zaheer Khan and Another, AIR 2006 Bombay 390 
— Bombay High Court (Division Bench). The Bombay High Court applied the Supreme Court's 
ruling in Niranjan Shankar Golikari and held that a non-compete clause prohibiting a 
cricketer from entering into commercial agreements with other parties after termination 
of a management contract is void under section 27 of the Indian Contract Act, 1872. 
The court declined to grant an injunction restraining Zaheer Khan from entering into 
a new management agreement. The court distinguished between: (a) clauses protecting 
genuine trade secrets and confidential information — potentially enforceable; and 
(b) blanket post-termination non-compete restrictions — void as restraints on trade. 
Ratio: Even in sophisticated commercial contracts, post-termination non-compete clauses 
are void under Indian law. The court's refusal to grant an injunction reflects the 
well-settled position that courts will not enforce such clauses. Status: Good law — 
persuasive authority from a division bench of the Bombay High Court.""",
        "court": "Bombay High Court",
        "citation": "AIR 2006 Bombay 390",
        "year": 2006,
        "tags": ["non-compete", "section 27 Contract Act", "void", "injunction", "sports", "commercial contract", "Bombay High Court"]
    },
    {
        "id": "deduction_wages_punjab_national_bank",
        "title": "Central Bank of India v. S. Satyam (1996) — Unauthorised Deductions from Wages",
        "text": """Central Bank of India v. S. Satyam and Others, (1996) 5 SCC 419 — Supreme 
Court of India. The Supreme Court held that deductions from wages of employees can only 
be made as specifically authorised under section 7 of the Payment of Wages Act, 1936. 
Any deduction not falling within the exhaustive categories listed in section 7 is 
unauthorised and the employer is liable to refund the deducted amount. The court held 
that the list of permissible deductions in section 7 is exhaustive, not illustrative, 
and an employer cannot make deductions on grounds not covered by the Act, even if the 
employee consents in writing. Ratio: Statutory protections on deductions from wages 
cannot be waived by individual agreement — section 7 provides minimum protections that 
override contractual terms. Status: Good law — applied in claims for recovery of 
unauthorised salary deductions, PF over-deductions, and unlawful penalty deductions.""",
        "court": "Supreme Court of India",
        "citation": "(1996) 5 SCC 419",
        "year": 1996,
        "tags": ["deductions", "wages", "section 7", "Payment of Wages Act", "unauthorised", "recovery", "refund"]
    },
    {
        "id": "hindustan_tin_works_1979",
        "title": "Hindustan Tin Works Pvt. Ltd. v. Employees (1979) — Full Back Wages on Illegal Dismissal",
        "text": """Hindustan Tin Works Pvt. Ltd. v. Employees of Hindustan Tin Works Pvt. Ltd., 
AIR 1979 SC 75 — Supreme Court of India. The Supreme Court held that when a workman's 
dismissal is found to be illegal, the normal rule is that the workman is entitled to full 
back wages from the date of dismissal to the date of reinstatement, unless the employer 
can show special circumstances justifying a reduction. The court disapproved of the 
practice of routinely reducing back wages without examining whether the workman was 
gainfully employed elsewhere during the period of dismissal. The burden of proving that 
the workman was gainfully employed lies on the employer. Ratio: Full back wages is the 
rule on reinstatement after illegal dismissal; reduction requires specific justification 
by the employer, not a mechanical approach by the tribunal. Status: Good law — leading 
authority on back wages following illegal dismissal. Frequently cited in Labour Court 
proceedings on reinstatement claims.""",
        "court": "Supreme Court of India",
        "citation": "AIR 1979 SC 75",
        "year": 1979,
        "tags": ["back wages", "illegal dismissal", "reinstatement", "full back wages", "burden of proof", "workman"]
    },
]
