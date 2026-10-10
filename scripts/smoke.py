import json,re,time
from pathlib import Path
from genlayer_py import create_account,create_client
from genlayer_py.chains import studionet
from genlayer_py.contracts import actions as contract_actions
def calldata_compat(method=None,args=None,kwargs=None):
 out={}
 if method is not None: out['method']=method
 if args: out['args']=args
 if kwargs: out['kwargs']=kwargs
 return out
contract_actions.make_calldata_object=calldata_compat
ROOT=Path(__file__).parents[1]; ENV=(ROOT.parents[3]/'accounts.env').read_text(); ADDRESS=json.loads((ROOT/'deployment.json').read_text())['contractAddress']
KEY=re.search(r'^ACCOUNT_1_GENLAYER_PRIVATE_KEY\s*=\s*"?([^"\r\n]+)',ENV,re.M).group(1).strip(); c=create_client(chain=studionet,account=create_account(account_private_key=KEY))
def wait(tx,expect='SUCCESS'):
 r=c.wait_for_transaction_receipt(transaction_hash=tx,wait_until='finalized',retries=180,interval=5000,full_transaction=True); leaders=r.get('consensus_data',{}).get('leader_receipt') or []; leaders=[leaders] if isinstance(leaders,dict) else leaders; ex=[str(x.get('execution_result','')).upper() for x in leaders]; assert r.get('result_name')=='MAJORITY_AGREE' and expect in ex; return r,ex
def write(name,args,expect='SUCCESS'):
 tx=c.write_contract(address=ADDRESS,function_name=name,args=args); print(name+'_tx='+str(tx),flush=True); wait(tx,expect); return str(tx)
stamp=str(int(time.time())); board='DRAFT-'+stamp; base='https://raw.githubusercontent.com/SAMiiNW/reciprocal-draft/main/fixtures/'; criterion='Pair a need and an offer only when the offer explicitly covers every material requirement in the need, without a stated exclusion that defeats delivery.'; tx={}
tx['open']=write('open_board',[board,'Civic software exchange',criterion])
entries=[('NEED-ACCESS-'+stamp,'NEED','Accessibility review needed','need-access.md'),('NEED-OFFLINE-'+stamp,'NEED','Offline resilience review needed','need-offline.md'),('OFFER-ACCESS-'+stamp,'OFFER','Inclusive interface lab','offer-access.md'),('OFFER-OFFLINE-'+stamp,'OFFER','Resilience bench','offer-offline.md')]
for eid,side,label,file in entries: tx[eid]=write('enter',[board,eid,side,label,base+file])
before=c.read_contract(address=ADDRESS,function_name='get_board',args=[board]); replay=c.write_contract(address=ADDRESS,function_name='enter',args=[board,'COPY-'+stamp,'NEED','Copied need',base+'need-access.md']); tx['replay']=str(replay); rr,rex=wait(replay,'ERROR'); after=c.read_contract(address=ADDRESS,function_name='get_board',args=[board]); assert before==after
tx['draw']=write('draw',[board]); final=c.read_contract(address=ADDRESS,function_name='get_board',args=[board]); assert final['state']=='DRAWN' and len(final['pairs'])==2
proof={'boardId':board,'contract':ADDRESS,'transactions':tx,'final':final,'duplicateProfile':{'consensus':rr.get('result_name'),'execution':rex,'stateUnchanged':before==after},'fixtureDisclosure':'Profiles and wallet are operator-controlled fixtures used to prove digest pinning, complete compatibility-edge consensus, deterministic pairing, and URL replay rejection.'}; (ROOT/'evidence').mkdir(exist_ok=True); (ROOT/'evidence'/'live-run.json').write_text(json.dumps(proof,indent=2)+'\n'); print(json.dumps(proof,indent=2))

