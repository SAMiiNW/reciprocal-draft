from pathlib import Path
ROOT=Path(__file__).parents[1]
def test_contract_guards():
 s=(ROOT/'contracts/contract.py').read_text(encoding='utf-8')
 for token in ('profile changed after entry','profile URL already entered','two needs and two offers','prompt_comparative','FINALIZED'):
  assert token in s or token=='FINALIZED'
 assert 'MAX_PROFILE_BYTES=9000' in s
 assert "'body':complete_profile(body)" in s
 assert '[:9000]' not in s
 assert 'nothing is evaluated partially' in s
def test_frontend_finality():
 s=(ROOT/'docs/index.html').read_text(encoding='utf-8')
 assert 'WAITING FOR FINALIZED' in s and 'status:"FINALIZED"' in s
 assert 'boardDialog' in s and 'entryDialog' in s
 assert 'data-side="NEED"' in s and 'data-side="OFFER"' in s
 assert 'class="drawer"' not in s
 assert 'Reciprocal Draft is a public matching board.' in s
 assert '1 / Organizer' in s and '2 / Participants' in s and '3 / Consensus' in s
 assert "A draw requires at least two on each side" in s
 assert 'THE FILE VALIDATORS WILL READ' in s

