# Web Claim Verifier

A GenLayer Intelligent Contract project for verifying web-based claims against public sources.

## How it works

1. The user enters a claim.
2. The user provides a source URL.
3. The application sends the claim and URL to the GenLayer Intelligent Contract.
4. The contract evaluates the source.
5. The result is classified as:
   - VERIFIED
   - FALSE
   - UNCERTAIN
6. Supporting evidence is returned with the result.

## Project Structure

```text
web-claim-verifier/
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
└── contract/
    └── web_claim_verifier.py
