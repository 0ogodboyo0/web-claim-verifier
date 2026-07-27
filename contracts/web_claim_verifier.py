# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }
# Web Claim Verifier - GenLayer proof-of-concept
from genlayer import *
import json


class WebClaimVerifier(gl.Contract):

    last_claim: str
    last_url: str
    last_verdict: str
    last_evidence: str

    def __init__(self):
        self.last_claim = ""
        self.last_url = ""
        self.last_verdict = ""
        self.last_evidence = ""

    @gl.public.write
    def verify_claim(self, claim: str, url: str):

        def evaluate_claim():

            response = gl.nondet.web.get(url)

            if response.status_code >= 400:
                return json.dumps({
                    "verdict": "UNCERTAIN",
                    "evidence": "Unable to access source."
                })

            source = response.body.decode("utf-8")

            prompt = f"""
You are a careful web claim verifier.

CLAIM:
{claim}

SOURCE:
{source[:12000]}

Determine whether the source supports the claim.

Return ONLY valid JSON:
{{
  "verdict": "VERIFIED" or "FALSE" or "UNCERTAIN",
  "evidence": "one short sentence from the source"
}}

Rules:
- VERIFIED = source clearly supports the claim.
- FALSE = source clearly contradicts the claim.
- UNCERTAIN = insufficient evidence.
- Never invent facts.
- Evidence must come from the supplied source.
"""

            result = gl.nondet.exec_prompt(prompt)

            data = json.loads(result)

            return json.dumps({
                "verdict": data["verdict"],
                "evidence": data["evidence"]
            }, sort_keys=True)

        result = gl.eq_principle.strict_eq(evaluate_claim)

        data = json.loads(result)

        self.last_claim = claim
        self.last_url = url
        self.last_verdict = data["verdict"]
        self.last_evidence = data["evidence"]

    @gl.public.view
    def get_result(self) -> dict:
        return {
            "claim": self.last_claim,
            "url": self.last_url,
            "verdict": self.last_verdict,
            "evidence": self.last_evidence
        }
