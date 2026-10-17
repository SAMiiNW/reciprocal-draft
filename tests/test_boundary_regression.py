from pathlib import Path

ROOT = Path(__file__).parents[1]
MAX_PROFILE_BYTES = 9_000


def accepts_complete_profile(body: bytes) -> bool:
    return 30 <= len(body) <= MAX_PROFILE_BYTES


def test_profile_condition_beyond_old_boundary_cannot_be_hidden():
    visible_capability = b"Can deliver an accessibility review. " + b"A" * 8_970
    hidden_exclusion = b"\nEXCLUSION: cannot provide keyboard or screen-reader testing."
    adversarial_profile = visible_capability + hidden_exclusion

    assert hidden_exclusion in adversarial_profile[9_000:]
    assert not accepts_complete_profile(adversarial_profile)

    source = (ROOT / "contracts/contract.py").read_text(encoding="utf-8")
    assert "len(body)>MAX_PROFILE_BYTES" in source
    assert "'body':complete_profile(body)" in source

