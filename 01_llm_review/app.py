import streamlit as st
from extractor import extract_text
from validator import validate_contract
from standards import STANDARDS

# ── Page config ───────────────────────────────────────────────
st.set_page_config(page_title="Contract Compliance Agent", page_icon="📄", layout="wide")
st.title("📄 AI Contract Compliance Agent")
st.caption("Upload a renovation contract and validate it against compliance standards.")

# ── Sidebar ───────────────────────────────────────────────────
with st.sidebar:
    st.header("Settings")
    contract_type = st.selectbox("Contract Type", ["Renovation"])
    st.markdown("---")
    st.markdown(f"**Clauses checked:** {len(STANDARDS)}")
    st.markdown("**Model:** GPT-4o")

# ── File Upload ───────────────────────────────────────────────
uploaded_file = st.file_uploader("Upload a contract (PDF)", type=["pdf"])

if uploaded_file and st.button("Analyze Contract", type="primary"):
    with st.spinner("Extracting text from contract..."):
        contract_text = extract_text(uploaded_file)

    if not contract_text.strip():
        st.error("Could not extract text from this PDF. Try a different file.")
        st.stop()

    with st.spinner("Analyzing compliance with GPT-4o..."):
        results = validate_contract(contract_text)

    # ── Summary metrics ───────────────────────────────────────
    total = len(results)
    passed = sum(1 for r in results if r["status"] == "pass")
    failed = sum(1 for r in results if r["status"] == "fail")
    unclear = sum(1 for r in results if r["status"] == "unclear")
    score = round((passed / total) * 100) if total else 0

    st.markdown("---")
    st.subheader("Compliance Summary")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Compliance Score", f"{score}%")
    col2.metric("✅ Pass", passed)
    col3.metric("❌ Fail", failed)
    col4.metric("⚠️ Unclear", unclear)

    # ── Findings ──────────────────────────────────────────────
    st.markdown("---")
    st.subheader("Findings")

    for r in results:
        status = r.get("status", "fail")
        icon = {"pass": "✅", "fail": "❌", "unclear": "⚠️"}.get(status, "❓")
        risk = r.get("assessed_risk", "unknown")
        confidence = r.get("confidence_score", 0)
        risk_color = {"high": "🔴", "medium": "🟡", "low": "🟢", "none": "⚪"}.get(risk, "⚪")

        with st.expander(f"{icon} {r['clause']}  —  Risk: {risk_color} {risk.capitalize()}  |  Confidence: {confidence}%"):
            st.write(r.get("explanation", ""))

            if r.get("evidence"):
                st.info(f"📎 **Evidence found:**\n> {r['evidence']}")

            if r.get("recommendation"):
                st.warning(f"💡 **Recommendation:** {r['recommendation']}")