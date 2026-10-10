# Reciprocal Draft

A shortlist is not a match. Reciprocal Draft collects public need and offer profiles, freezes each profile digest, asks GenLayer validators for the complete compatibility graph, then performs a deterministic one-to-one draft on-chain.

## Why consensus belongs here
Compatibility is semantic and bilateral. Validators must fetch every frozen profile and agree on the exact edge set under one frozen criterion. Pair selection itself is deterministic and does not trust model prose.

## Lifecycle
OPEN BOARD -> ENTER NEEDS AND OFFERS -> DRAW -> DRAWN.

Duplicate IDs and profile URLs are rejected. Profiles that change after entry invalidate the draw. At least two entries per side are required.

## Public app
The two-rail interface connects a wallet, submits writes, waits for FINALIZED, and reads the authoritative board from StudioNet.

## Tests
Run `python -m pytest tests -q` and `genvm-lint contracts/contract.py`.

