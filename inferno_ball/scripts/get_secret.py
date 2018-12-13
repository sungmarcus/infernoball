import secretsharing as sss
from hashlib import sha256
from passlib.hash import pbkdf2_sha256,argon2,sha512_crypt,sha1_crypt
import sys

def pxor(pwd,share):
    '''
      XOR a hashed password into a Shamir-share

      1st few chars of share are index, then "-" then hexdigits
      we'll return the same index, then "-" then xor(hexdigits,sha256(pwd))
      we truncate the sha256(pwd) to if the hexdigits are shorter
      we left pad the sha256(pwd) with zeros if the hexdigits are longer
      we left pad the output with zeros to the full length we xor'd
    '''
    words=share.split("-")
    hexshare=words[1]
    slen=len(hexshare)
    hashpwd=sha256(pwd).hexdigest()
    hlen=len(hashpwd)
    outlen=0
    if slen<hlen:
        outlen=slen
        hashpwd=hashpwd[0:outlen]
    elif slen>hlen:
        outlen=slen
        hashpwd=hashpwd.zfill(outlen)
    else:
        outlen=hlen
    xorvalue=int(hexshare, 16) ^ int(hashpwd, 16) # convert to integers and xor
    paddedresult='{:x}'.format(xorvalue)          # convert back to hex
    paddedresult=paddedresult.zfill(outlen)       # pad left
    result=words[0]+"-"+paddedresult              # put index back
    return result

def pwds_shares_to_secret(kpwds,kinds,diffs):
    '''
        take k passwords, indices of those, and the "public" shares and 
        recover shamir secret
    '''
    shares=[]
    for i in range(0,len(kpwds)):
        shares.append(pxor(kpwds[i],diffs[kinds[i]]))
    secret=sss.SecretSharer.recover_secret(shares)
    return secret

'''check k-1 passwords to confirm if k of n  is found'''

def pwds_shares_to_secret_verify(kpwds,kinds,diffs):
    '''
        take k passwords, indices of those, and the "public" shares and
        recover shamir secret
    '''
    shares=[]
    for i in range(0,len(kpwds)):
        shares.append(pxor(kpwds[i],diffs[kinds[i]]))
    secret=sss.SecretSharer.recover_secret(shares[:-1])
    return secret


kpwds = []
kinds = []
diffs = []

input_hashes = sys.argv[1]
input_cracked = sys.argv[2]
input_shares = sys.argv[3]

with open(input_cracked, "r") as cracked_file:
    cracked = cracked_file.read().splitlines()
with open(input_shares,"r") as shares:
    diffs = shares.read().splitlines()
with open(input_hashes,"r") as hashes_file:
    hashes = hashes_file.read().splitlines()

for line in cracked:
    head, sep, tail = line.partition(":")
    kpwds.append(tail)
    kinds.append(hashes.index(head))
print(pwds_shares_to_secret(kpwds,kinds,diffs))
print(pwds_shares_to_secret_verify(kpwds,kinds,diffs))

with open("layer.secrets","w") as layer:
    layer.write(pwds_shares_to_secret(kpwds,kinds,diffs))
