import json
from openai import OpenAI
from dotenv import load_dotenv
from standards import STANDARDS

load_dotenv()
client = OpenAI()

SYSTEM_PROMPT = """
You are a professional contract compliance reviewer specializing in renovation contracts.

You will be given a list of compliance clauses and a contract to review.

For each clause, return a JSON array. Each item must follow this exact structure:
{
  "clause": "clause name",
  "status": "pass" | "fail" | "unclear",
  "confidence_score": integer between 0 and 100,
  "explanation": "brief explanation of your finding",
  "evidence": "direct quote from the contract, or null if not found",
  "recommendation": "what should be added or clarified, or null if status is pass",
  "assessed_risk": "high" | "medium" | "low" | "none"
}

Rules:
- Use "pass" when the clause is clearly and sufficiently addressed.
- Use "fail" when the clause is entirely missing.
- Use "unclear" when the concept is mentioned but not sufficiently defined to be enforceable.
- "assessed_risk" should reflect your judgment based on context, not just the default risk.
- "evidence" must be a direct quote from the contract text when evidence_required is true.
- Return ONLY the JSON array. No extra text, no markdown, no explanation outside the array.
"""

def build_standards_text(standards: list) -> str:
    lines = []
    for s in standards:
        line = (
            f"- Clause: {s['clause']}\n"
            f"  Description: {s['description']}\n"
            f"  Risk if missing: {s['risk_if_missing']}\n"
            f"  Default risk: {s['default_risk']}\n"
            f"  Evidence required: {s['evidence_required']}\n"
            f"  Category: {s['category']}"
        )
        lines.append(line)
    return "\n\n".join(lines)

def validate_contract(contract_text: str, standards: list = STANDARDS) -> list:
    standards_text = build_standards_text(standards)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"COMPLIANCE CLAUSES:\n{standards_text}\n\nCONTRACT TEXT:\n{contract_text}"}
        ],
        temperature=0.1  # low temp for consistent, deterministic output
    )

    raw = response.choices[0].message.content.strip()

    # Safety: strip accidental markdown fences
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]

    return json.loads(raw)