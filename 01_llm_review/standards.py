# standards.py

STANDARDS = [
    {
        "clause": "Parties Identified",
        "description": "Both parties (client and contractor) must be clearly named.",
        "risk_if_missing": "The contract may be unenforceable without identified parties.",
        "default_risk": "high",
        "evidence_required": True,
        "category": "legal"
    },
    {
        "clause": "Signatures",
        "description": "The contract should contain signature blocks for all parties.",
        "risk_if_missing": "The agreement may not be legally enforceable.",
        "default_risk": "high",
        "evidence_required": True,
        "category": "legal"
    },
    {
        "clause": "Scope of Work",
        "description": "The contract should clearly describe the renovation work to be completed.",
        "risk_if_missing": "Disputes may occur if project responsibilities are unclear.",
        "default_risk": "high",
        "evidence_required": True,
        "category": "operational"
    },
    {
        "clause": "Payment Schedule",
        "description": "The contract should define deposit, progress payments, final payment, and due dates.",
        "risk_if_missing": "Payment disputes or cash flow issues may occur.",
        "default_risk": "high",
        "evidence_required": True,
        "category": "financial"
    },
    {
        "clause": "Insurance",
        "description": "The contract should state insurance requirements and coverage for both parties.",
        "risk_if_missing": "Liability exposure may increase significantly for both parties.",
        "default_risk": "high",
        "evidence_required": True,
        "category": "legal"
    },
    {
        "clause": "Change Orders",
        "description": "The contract should explain how extra work or changes are approved and priced.",
        "risk_if_missing": "Unapproved scope changes may lead to disputes.",
        "default_risk": "medium",
        "evidence_required": True,
        "category": "operational"
    },
    {
        "clause": "Project Schedule",
        "description": "The contract should include start date, completion date, or milestone schedule.",
        "risk_if_missing": "Delays may create disputes without agreed timelines.",
        "default_risk": "medium",
        "evidence_required": True,
        "category": "operational"
    },
    {
        "clause": "Permits and Inspections",
        "description": "The contract should specify who is responsible for obtaining permits and inspections.",
        "risk_if_missing": "Permit-related disputes and project delays may occur.",
        "default_risk": "medium",
        "evidence_required": True,
        "category": "legal"
    },
    {
        "clause": "Liability Cap",
        "description": "A maximum liability amount or limitation should be stated.",
        "risk_if_missing": "Contractor may be exposed to unlimited financial liability.",
        "default_risk": "medium",
        "evidence_required": True,
        "category": "financial"
    },
    {
        "clause": "Warranty",
        "description": "The contract should state whether workmanship or materials are covered after completion.",
        "risk_if_missing": "Client and contractor expectations may be unclear after project completion.",
        "default_risk": "medium",
        "evidence_required": True,
        "category": "operational"
    },
    {
        "clause": "Termination",
        "description": "The contract should explain when either party can end the agreement.",
        "risk_if_missing": "The parties may not know their rights if the project breaks down.",
        "default_risk": "medium",
        "evidence_required": True,
        "category": "legal"
    },
    {
        "clause": "Governing Law",
        "description": "A legal jurisdiction must be specified (e.g. Province of Ontario).",
        "risk_if_missing": "Unclear which laws apply in a dispute.",
        "default_risk": "low",
        "evidence_required": False,
        "category": "legal"
    },
    {
        "clause": "Dispute Resolution",
        "description": "The contract should explain how disputes will be handled (mediation, arbitration, courts).",
        "risk_if_missing": "Disputes may escalate without a defined process.",
        "default_risk": "low",
        "evidence_required": False,
        "category": "legal"
    },
]

# Future rule sets — not yet implemented
# EMPLOYMENT_RULES = []
# LEASE_RULES = []
# VENDOR_RULES = []

CONTRACT_TYPES = {
    "renovation": STANDARDS,
    # "employment": EMPLOYMENT_RULES,
    # "lease": LEASE_RULES,
}