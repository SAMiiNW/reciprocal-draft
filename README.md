# Reciprocal Draft

A shortlist is not a match. Reciprocal Draft collects public need and offer profiles, freezes each profile digest, asks GenLayer validators for the complete compatibility graph, then performs a deterministic one-to-one draft on-chain.

## Who does what
- **Organizer:** opens a named matching table and freezes one detailed mutual-fit rule.
- **Participants:** add public HTTPS profiles to either the NEED side or the OFFER side.
- **GenLayer validators:** fetch every frozen profile and agree on all compatible need-offer edges.
- **Contract:** deterministically selects non-overlapping pairs from that agreed graph and stores the final result.

The public app now starts with this explanation, separates the organizer and participant paths, labels every input by what validators will read, and always shows the next required step.

## Why consensus belongs here
Compatibility is semantic and bilateral. Validators must fetch every frozen profile and agree on the exact edge set under one frozen criterion. Pair selection itself is deterministic and does not trust model prose.

## Lifecycle
OPEN BOARD -> ENTER NEEDS AND OFFERS -> DRAW -> DRAWN.

Duplicate IDs and profile URLs are rejected. Profiles must be 30 to 9,000 bytes, and validators inspect every accepted byte without prefix slicing. Profiles that change after entry invalidate the draw. At least two entries per side are required.

## Public app
The two-rail interface connects a wallet, submits writes, waits for FINALIZED, and reads the authoritative board from StudioNet.

## Tests
Run `python -m pytest tests -q` and `genvm-lint contracts/contract.py`.

