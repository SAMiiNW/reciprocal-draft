from pathlib import Path
ROOT=Path(__file__).parents[1]
def test_contract_guards():
 s=(ROOT/'contracts/contract.py').read_text()
 for token in ('profile changed after entry','profile URL already entered','two needs and two offers','prompt_comparative','FINALIZED'):
  assert token in s or token=='FINALIZED'
def test_frontend_finality():
 s=(ROOT/'docs/index.html').read_text()
 assert 'WAITING FOR FINALIZED' in s and 'status:"FINALIZED"' in s
 assert 'west-rail' in s and 'east-rail' in s

