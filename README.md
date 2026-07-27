# Web Claim Verifier

A GenLayer Intelligent Contract for verifying web-based claims using decentralized web access, LLM evaluation, and GenLayer consensus.

## Overview

Web Claim Verifier allows a user to submit:

- A claim
- A public web source URL

The contract retrieves the source content, evaluates whether the source supports the claim, and stores the resulting verdict and evidence.

## How It Works

1. The user submits a claim and source URL.
2. The contract retrieves the web page using GenLayer's web access.
3. The source content is provided to an LLM for evaluation.
4. The evaluator returns one of three outcomes:
   - VERIFIED
   - FALSE
   - UNCERTAIN
5. GenLayer's equivalence principle is used to reach a deterministic result.
6. The contract stores the claim, URL, verdict, and evidence.
7. The stored result can be retrieved through `get_result`.

## Contract Interface

### verify_claim

```text
verify_claim(claim, url)
