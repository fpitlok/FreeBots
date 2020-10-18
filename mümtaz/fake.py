# FAKE LOGIN
from linepy  import *
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from akad.ttypes import TalkException
#=====================================================================
try:
    with open('token1.txt','r') as tokens:
        token = tokens.read()
    print(str(token))
except Exception as e:
    noobcoder = LINE()
noobcoder = LINE(token,appName="IOSIPAD\t11.2.5\tiPhone X\t11.2.5")

p = noobcoder.getProfile()
p.displayName = "GW HOMO"
p.statusMessage = "LGBT FANS CLUB"
noobcoder.updateProfile(p)
groups = noobcoder.getGroupIdsJoined()
for g in groups:
    G = noobcoder.getGroup(g)
    G.name = "NOOB CODER?"
    noobcoder.sendMessage(g,"Just a nolep who <3 the </>")
    noobcoder.updateGroup(G)
while True:
    noobcoder.updateProfile(p)

noobcoderProfile = noobcoder.getProfile()
noobcoderSettings = noobcoder.getSettings()
noobcoderPoll = OEPoll(noobcoder)
noobcoderStart = time.time()
noobcoderMID = noobcoder.getProfile().mid
   
def run():
    while True:
        try:
            ops = noobcoderPoll.singleTrace(count=50)
            if ops != None:
                for op in ops:
                   noobcoderBot(op)
                   noobcoderPoll.setRevision(op.revision)
        except Exception as e:
            logError(e)
            
if __name__ == "__main__":
    run()