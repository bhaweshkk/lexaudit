"""
data/sample_statutes.py
────────────────────────
Real excerpts from key Indian labour and employment statutes.
These are the documents ingested into ChromaDB for RAG retrieval.

Sources: India Code (indiacode.nic.in) — public domain government texts.
To add more statutes, follow the same structure and call ingest.py.
"""

STATUTES = [
    {
        "id": "pwa_1936_s1",
        "title": "Payment of Wages Act 1936 — Scope and Definitions",
        "text": """The Payment of Wages Act, 1936 applies to persons employed in any factory, 
and to persons employed (otherwise than in a factory) upon any railway by a railway 
administration or, either directly or through a sub-contractor, by a person fulfilling 
a contract with a railway administration. Section 1(4): The State Government may, by 
notification in the Official Gazette, extend the provisions of this Act or any of them 
to the payment of wages to any class of persons employed in any establishment or class 
of establishments. Section 2(vi) defines 'wages' as all remuneration (whether by way 
of salary, allowances, or otherwise) expressed in terms of money or capable of being 
so expressed which would, if the terms of employment, express or implied, were fulfilled, 
be payable to a person employed in respect of his employment or of work done in such 
employment, including house rent allowance.""",
        "act": "Payment of Wages Act, 1936",
        "sections": "S.1, S.2",
        "status": "in_force",
        "tags": ["wages", "salary", "employment", "factory", "railway"]
    },
    {
        "id": "pwa_1936_s3_s4",
        "title": "Payment of Wages Act 1936 — Responsibility for payment and time of payment",
        "text": """Section 3 — Responsibility for payment of wages: Every employer shall be 
responsible for the payment to persons employed by him of all wages required to be paid 
under this Act. In the case of persons employed in factories, every person responsible 
to the owner for the supervision and control of the factory. Section 4 — Fixation of 
wage-periods: Every person responsible for the payment of wages under section 3 shall 
fix periods (in this Act referred to as wage-periods) in respect of which such wages 
shall be payable. No wage-period shall exceed one month. Section 5 — Time of payment 
of wages: The wages of every person employed upon or in any railway, factory or 
industrial or other establishment upon or in which less than 1000 persons are employed 
shall be paid before the expiry of the 7th day after the last day of the wage-period 
in respect of which the wages are payable. Where 1000 or more persons are employed, 
wages shall be paid before the expiry of the 10th day.""",
        "act": "Payment of Wages Act, 1936",
        "sections": "S.3, S.4, S.5",
        "status": "in_force",
        "tags": ["wages", "payment", "wage-period", "employer", "responsibility"]
    },
    {
        "id": "pwa_1936_s7_s8",
        "title": "Payment of Wages Act 1936 — Deductions from wages",
        "text": """Section 7 — Deductions which may be made from wages: Notwithstanding the 
provisions of the Railways Act, 1890, the wages of an employed person shall be paid 
to him without deductions of any kind except those authorised by or under this Act. 
Deductions from the wages of an employed person shall be made only in accordance with 
the provisions of this Act, and may be of the following kinds only: (a) fines; (b) 
deductions for absence from duty; (c) deductions for damage to or loss of goods expressly 
entrusted to the employed person for custody, or for loss of money; (d) deductions for 
house-accommodation supplied by the employer; (e) deductions for such amenities and 
services supplied by the employer as the State Government may authorise; (f) deductions 
for recovery of advances or for adjustment of over-payments of wages. Section 8: No fine 
shall be imposed on any employed person unless the acts or omissions in respect of which 
the fine is imposed are those specified in a list approved and exhibited by the employer.""",
        "act": "Payment of Wages Act, 1936",
        "sections": "S.7, S.8",
        "status": "in_force",
        "tags": ["deductions", "wages", "fines", "absence", "salary deduction"]
    },
    {
        "id": "pwa_1936_s15_s16",
        "title": "Payment of Wages Act 1936 — Claims and penalties for delayed/unpaid wages",
        "text": """Section 15 — Claims arising out of deductions from wages or delay in payment 
of wages and penalty for malicious or vexatious claims: The appropriate Government may 
by notification in the Official Gazette, appoint any Commissioner for Workmen's 
Compensation or any officer of the Central Government exercising functions as a Labour 
Commissioner for any region, to be the authority to hear and decide for any specified 
area all claims arising out of deductions from the wages, or delay in payment of the wages, 
of persons employed or paid in that area. The authority may try the claim. Where contrary 
to the provisions of this Act, any deduction has been made from the wages of an employed 
person, or any payment of wages has been delayed, the authority shall: (a) direct the 
refund to the employed person of the amount deducted; or (b) the payment of the delayed 
wages together with the payment of such compensation as the authority may think fit but 
not exceeding ten times the amount so deducted or delayed. Section 20 — Penalty for 
offences: Any employer who contravenes any of the provisions of sections 5, 7, 8, 9, 10, 
11, 12 or 13 or of any rule made thereunder shall be punishable with fine which shall 
not be less than one thousand five hundred rupees but which may extend to seven thousand 
five hundred rupees.""",
        "act": "Payment of Wages Act, 1936",
        "sections": "S.15, S.16, S.20",
        "status": "in_force",
        "tags": ["claims", "delayed wages", "penalty", "unpaid wages", "compensation", "remedy"]
    },
    {
        "id": "ida_1947_s2_definitions",
        "title": "Industrial Disputes Act 1947 — Key Definitions",
        "text": """The Industrial Disputes Act, 1947 makes provision for the investigation and 
settlement of industrial disputes and for certain other purposes. Section 2(k) defines 
'industrial dispute' as any dispute or difference between employers and employers, or 
between employers and workmen, or between workmen and workmen, which is connected with 
the employment or non-employment or the terms of employment or with the conditions of 
labour, of any person. Section 2(s) defines 'workman' as any person (including an 
apprentice) employed in any industry to do any manual, unskilled, skilled, technical, 
operational, clerical or supervisory work for hire or reward. Section 2(oo) defines 
'retrenchment' as the termination by the employer of the service of a workman for any 
reason whatsoever, otherwise than as a punishment inflicted by way of disciplinary action, 
but does not include: (a) voluntary retirement of the workman; (b) retirement of the 
workman on reaching the age of superannuation; (c) termination of the service of the 
workman as a result of the non-renewal of the contract of employment.""",
        "act": "Industrial Disputes Act, 1947",
        "sections": "S.2(k), S.2(s), S.2(oo)",
        "status": "in_force",
        "tags": ["industrial dispute", "workman", "retrenchment", "termination", "employment"]
    },
    {
        "id": "ida_1947_s25_retrenchment",
        "title": "Industrial Disputes Act 1947 — Retrenchment Compensation",
        "text": """Section 25F — Conditions precedent to retrenchment of workmen: No workman 
employed in any industry who has been in continuous service for not less than one year 
under an employer shall be retrenched by that employer until: (a) the workman has been 
given one month's notice in writing indicating the reasons for retrenchment and the 
period of notice has expired, or the workman has been paid in lieu of such notice wages 
for the period of the notice; (b) the workman has been paid, at the time of retrenchment, 
compensation which shall be equivalent to fifteen days' average pay for every completed 
year of continuous service or any part thereof in excess of six months. Section 25G — 
Procedure for retrenchment: Where any workman in an establishment belonging to a 
particular category is to be retrenched, the employer shall ordinarily retrench the 
workman who was the last person to be employed in that category, unless for reasons to 
be recorded the employer retrenches any other workman. Section 25H — Re-employment of 
retrenched workmen: Where any workmen are retrenched, and the employer proposes to take 
into his employ any persons, he shall, in such manner as may be prescribed, give an 
opportunity to the retrenched workmen or ex-workmen to offer themselves for re-employment.""",
        "act": "Industrial Disputes Act, 1947",
        "sections": "S.25F, S.25G, S.25H",
        "status": "in_force",
        "tags": ["retrenchment", "notice", "compensation", "termination", "one month notice", "15 days pay"]
    },
    {
        "id": "ida_1947_s25n_25o",
        "title": "Industrial Disputes Act 1947 — Closure and Layoff in Large Establishments",
        "text": """Section 25N — Conditions precedent to retrenchment of workmen in certain 
establishments: No workman employed in any industrial establishment to which this Chapter 
applies, who has been in continuous service for not less than one year under an employer, 
shall be retrenched by that employer until: (a) the workman has been given three months' 
notice in writing indicating the reasons for retrenchment or the workman has been paid 
in lieu of such notice wages for the period of the notice; and (b) the prior permission 
of the appropriate Government has been obtained on an application made in this behalf. 
This applies to establishments employing 100 or more workers on an average working day. 
Section 25O — Procedure for closing down an undertaking: An employer who intends to close 
down an undertaking of an industrial establishment to which this Chapter applies shall, 
in the prescribed manner, apply, for prior permission at least ninety days before the 
date on which the intended closure is to become effective, to the appropriate Government, 
stating clearly the reasons for the intended closure of the undertaking.""",
        "act": "Industrial Disputes Act, 1947",
        "sections": "S.25N, S.25O",
        "status": "in_force",
        "tags": ["closure", "layoff", "100 workers", "government permission", "large establishment"]
    },
    {
        "id": "mwa_1948_s3_s4",
        "title": "Minimum Wages Act 1948 — Fixation and Revision of Minimum Wages",
        "text": """The Minimum Wages Act, 1948 provides for fixing minimum rates of wages in 
certain employments. Section 3 — Fixing of minimum rates of wages: The appropriate 
Government shall fix the minimum rates of wages payable to employees employed in an 
employment specified in Part I or Part II of the Schedule and in an employment added 
to either Part by notification under section 27. The appropriate Government shall review 
at such intervals as it may think fit, such intervals not exceeding five years, the 
minimum rates of wages so fixed and revise the minimum rates, if necessary. Section 4 — 
Minimum rate of wages: Any minimum rate of wages fixed or revised by the appropriate 
Government may consist of: (a) a basic rate of wages and a special allowance at a rate 
to be adjusted, at such intervals and in such manner as the appropriate Government may 
direct, to accord as nearly as practicable with the variation in the cost of living index 
number applicable to such workers; or (b) a basic rate of wages with or without the cost 
of living allowance, and the cash value of the concessions in respect of supplies of 
essential commodities at concession rates.""",
        "act": "Minimum Wages Act, 1948",
        "sections": "S.3, S.4",
        "status": "in_force",
        "tags": ["minimum wages", "wages", "cost of living", "allowance", "revision"]
    },
    {
        "id": "mwa_1948_s20_claims",
        "title": "Minimum Wages Act 1948 — Claims for Less Than Minimum Wages",
        "text": """Section 20 — Claims: The appropriate Government may, by notification in the 
Official Gazette, appoint any Commissioner for Workmen's Compensation or any officer of 
the Central Government exercising functions as a Labour Commissioner for any region, or 
any officer of the State Government not below the rank of Labour Commissioner or any 
other officer with experience as a Judge of a Civil Court or as a stipendiary Magistrate 
to be the Authority to hear and decide for any specified area all claims arising out of 
payment of less than the minimum rates of wages or in respect of the payment of remuneration 
for days of rest or for work done on such days under clause (b) or clause (c) of sub-section 
(1) of section 13 or of contravention of any term of the contract of service express or 
implied. Where an employee claims payment of an amount due to him under this Act, he may 
present his claim in the prescribed manner before the authority. The authority may direct 
payment of the amount found due to the employee together with such compensation as the 
authority may think fit, not exceeding ten times the amount.""",
        "act": "Minimum Wages Act, 1948",
        "sections": "S.20",
        "status": "in_force",
        "tags": ["minimum wages claims", "less than minimum", "compensation", "remedy", "authority"]
    },
    {
        "id": "mba_1961_s5_s6",
        "title": "Maternity Benefit Act 1961 — Right to Maternity Benefit",
        "text": """The Maternity Benefit Act, 1961 regulates the employment of women in certain 
establishments for certain periods before and after child-birth and provides for maternity 
benefit and certain other benefits. Section 5 — Right to payment of maternity benefit: 
Subject to the provisions of this Act, every woman shall be entitled to, and her employer 
shall be liable for, the payment of maternity benefit at the rate of the average daily 
wage for the period of her actual absence immediately preceding and including the day of 
her delivery and for the six weeks immediately following that day. The maximum period for 
which any woman shall be entitled to maternity benefit shall be twenty-six weeks of which 
not more than eight weeks shall precede the date of her expected delivery. Section 6 — 
Notice of claim for maternity benefit and payment thereof: Any woman employed in an 
establishment and entitled to maternity benefit under the provisions of this Act may give 
notice in writing in such form as may be prescribed, to her employer, stating that her 
maternity benefit and any other amount to which she may be entitled under this Act may be 
paid to her or to such person as she may nominate in the notice.""",
        "act": "Maternity Benefit Act, 1961",
        "sections": "S.5, S.6",
        "status": "in_force",
        "tags": ["maternity", "maternity benefit", "26 weeks", "pregnancy", "woman employee", "leave"]
    },
    {
        "id": "mba_1961_s12_dismissal",
        "title": "Maternity Benefit Act 1961 — Dismissal During Maternity",
        "text": """Section 12 — Dismissal during absence or pregnancy: (1) When a woman absents 
herself from work in accordance with the provisions of this Act, it shall be unlawful for 
her employer to discharge or dismiss her during or on account of such absence or to give 
notice of discharge or dismissal on such a day that the notice will expire during such 
absence, or to vary to her disadvantage any of the conditions of her service. (2) The 
discharge or dismissal of a woman at any time during her pregnancy, if the woman but for 
such discharge or dismissal would have been entitled to maternity benefit or medical bonus 
referred to in section 8, shall not have the effect of depriving her of the maternity 
benefit or medical bonus: Provided that where the discharge or dismissal is for any 
prescribed gross misconduct, the employer may, by order in writing communicated to the 
woman, deprive her of the maternity benefit or medical bonus or both. Section 21 — 
Penalty for contravention of Act by employer: If any employer fails to pay any amount of 
maternity benefit to a woman entitled under this Act or discharges or dismisses such a 
woman during or on account of her absence from work in contravention of the provisions 
of this Act, he shall be punishable with imprisonment for a term which shall not be less 
than three months but which may extend to one year and with fine which shall not be less 
than two thousand rupees but which may extend to five thousand rupees.""",
        "act": "Maternity Benefit Act, 1961",
        "sections": "S.12, S.21",
        "status": "in_force",
        "tags": ["maternity dismissal", "pregnancy dismissal", "unlawful termination", "penalty", "gross misconduct"]
    },
    {
        "id": "clra_1970_s7_s10",
        "title": "Contract Labour (Regulation and Abolition) Act 1970 — Registration and Licensing",
        "text": """The Contract Labour (Regulation and Abolition) Act, 1970 regulates the employment 
of contract labour in certain establishments and provides for its abolition in certain 
circumstances. Section 7 — Registration of certain establishments: Every principal employer 
of an establishment to which this Act applies shall, within such period as the appropriate 
Government may, by notification in the Official Gazette, fix in this behalf, make an 
application to the registering officer for registration of the establishment. Section 10 — 
Prohibition of employment of contract labour: The appropriate Government may, after 
consultation with the Central Board or a State Board, as the case may be, prohibit by 
notification in the Official Gazette, employment of contract labour in any process, 
operation or other work in any establishment. Section 21 — Responsibility for payment 
of wages: A contractor shall be responsible for payment of wages to each worker employed 
by him as contract labour and such wages shall be paid before the expiry of such period 
as may be prescribed. Every principal employer shall nominate a representative duly 
authorised by him to be present at the time of disbursement of wages by the contractor 
and it shall be the duty of such representative to certify the amounts paid as wages.""",
        "act": "Contract Labour (Regulation and Abolition) Act, 1970",
        "sections": "S.7, S.10, S.21",
        "status": "in_force",
        "tags": ["contract labour", "contractor", "principal employer", "wages", "licensing", "registration"]
    },
    {
        "id": "labour_code_wages_2019",
        "title": "Code on Wages 2019 — Status and Overview",
        "text": """The Code on Wages, 2019 received Presidential assent on 8 August 2019 and was 
published in the Official Gazette. It consolidates and amends the laws relating to wages 
and bonus and for connected matters, amalgamating four laws: the Payment of Wages Act 1936, 
the Minimum Wages Act 1948, the Payment of Bonus Act 1965, and the Equal Remuneration 
Act 1976. The Code on Wages defines 'worker' broadly to include any person employed on 
wages in any industry, trade, business, manufacture or occupation and includes managerial, 
supervisory, and administrative persons drawing wages not exceeding fifteen thousand rupees 
per month or such amount as notified. IMPORTANT STATUS NOTE: As of 2025, the Central 
Government has NOT notified the commencement date for the Code on Wages, 2019 at the 
national level. The four constituent Acts — Payment of Wages Act 1936, Minimum Wages Act 
1948, Payment of Bonus Act 1965, and Equal Remuneration Act 1976 — therefore REMAIN IN 
FORCE. The Code on Wages will only become operative for workers in a state after both the 
Central Government and the relevant State Government issue commencement notifications. 
Practitioners must continue to advise clients under the existing four Acts until commencement 
is notified.""",
        "act": "Code on Wages, 2019",
        "sections": "S.1, S.2",
        "status": "pending_commencement",
        "tags": ["code on wages", "labour code", "Payment of Wages Act", "Minimum Wages Act", "pending commencement", "consolidation"]
    },
    {
        "id": "irc_2020_status",
        "title": "Industrial Relations Code 2020 — Status and Overview",
        "text": """The Industrial Relations Code, 2020 received Presidential assent on 28 September 2020. 
It consolidates and amends the laws relating to trade unions, conditions of employment 
in industrial establishment or undertaking, investigation and settlement of industrial 
disputes, amalgamating three Acts: the Trade Unions Act 1926, the Industrial Employment 
(Standing Orders) Act 1946, and the Industrial Disputes Act 1947. The Code raises the 
threshold for prior government permission for retrenchment and closure from 100 workers 
to 300 workers in establishments. It introduces the concept of a 'fixed-term employment' 
workman. IMPORTANT STATUS NOTE: As of 2025, the Central Government has NOT notified 
the commencement date for the Industrial Relations Code, 2020. The Industrial Disputes 
Act 1947, Trade Unions Act 1926, and Industrial Employment (Standing Orders) Act 1946 
REMAIN IN FORCE. Practitioners must continue to advise clients on retrenchment, notice 
periods, and industrial disputes under the Industrial Disputes Act 1947 until the 
commencement of the Industrial Relations Code is notified.""",
        "act": "Industrial Relations Code, 2020",
        "sections": "S.1, S.2",
        "status": "pending_commencement",
        "tags": ["industrial relations code", "labour code", "IDA", "industrial disputes", "300 workers", "pending commencement"]
    },
]
