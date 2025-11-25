# backend/insurance_data.py

INSURANCE_KB = """
National Life Insurance Limited (Bangladesh) – Key Information

1. Policy Types:
   - Endowment Insurance
   - Term Life Insurance
   - Whole Life Policy
   - Child Protection Policy
   - Pension/Retirement Plan
   - Money-Back Plans

2. Common Benefits:
   - Death benefits
   - Maturity benefits
   - Bonus/Profit sharing
   - Loan facilities after policy maturity period
   - Tax benefits (as per Bangladesh government guidelines)

3. Eligibility:
   - Minimum age: 18 years
   - Maximum age: varies by plan (55–65 years)
   - Medical test may be required for high-sum policies

4. Claims Process:
   - Submit claim form + NID + death certificate
   - Provide policy documents
   - Company verification → payout
"""

def get_insurance_info():
    return INSURANCE_KB
