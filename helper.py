# HELPER
# BATU WAS HERE
# </> LUX-STORE 2K17
from linepy import *
from akad.ttypes import Message
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from akad.ttypes import ContentType as Type
from akad.ttypes import TalkException
from EnesKing.thrift.protocol import TCompactProtocol
from EnesKing.thrift.transport import THttpClient
from EnesKing.ttypes import LoginRequest
from Naked.toolshed.shell import execute_js
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
from gtts import gTTS
from threading import Thread
from io import StringIO
from multiprocessing import Pool
from googletrans import Translator
from urllib.parse import urlencode
from wikiapi import WikiApi
from tmp.MySplit import *
from random import randint
from shutil import copyfile
from youtube_dl import YoutubeDL
from threading import Thread, activeCount
import LineService
import subprocess, youtube_dl, humanize, traceback
import subprocess as cmd
import time, random, sys, json, null, codecs, html5lib ,shutil ,threading, glob, re, base64, string, os, requests, six, ast, pytz, wikipedia, urllib, urllib.parse, atexit, asyncio, traceback
_session = requests.session()
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
#=====================================================================
#enesbyrk = LINE("u0b7c5725707efe9cdaea771f1bfbbd02:aWF0OiAxNTkwNzk0OTU4MDg3Cg==..bZ/ReeMQmcGnxYoZruEyz74vX4k=",appName="IOS\t10.1.1\tiPhone_OS\t12.4.1")
#enesbyrk = LINE("u9e06431f822b382d1c09db3885e96856:aWF0OiAxNTkyMzQ4Mzg0MTIyCg==..4MVuHvk83mlSSeAGsLRFAlic6JM=",appName="IOS\t10.1.1\tiPhone_OS\t12.4.1")
enesbyrk= LINE()
#Channel(enesbyrk, "1597127494").getChannelResult().channelAccessToken
#=======================================================
waitOpen = codecs.open("enesbyrk/wait.json","r","utf-8")
settingsOpen = codecs.open("enesbyrk/temp.json","r","utf-8")
premiumOpen = codecs.open("enesbyrk/user.json","r","utf-8")
javaOpen = codecs.open("enesbyrk/java.json","r","utf-8")
#=====================================================================
#=====================================================================
enesbyrkProfile = enesbyrk.getProfile()
enesbyrkSettings = enesbyrk.getSettings()
enesbyrkPoll = OEPoll(enesbyrk)
enesbyrkMID = enesbyrk.getProfile().mid
#=====================================================================
loop = asyncio.get_event_loop()
myAdmin = ["u0a2394509afc4f92b88b4ab598f0cf05"]
botStart = time.time()
msg_dict = {}
temp_flood = {}
wait = json.load(waitOpen)
settings = json.load(settingsOpen)
premium = json.load(premiumOpen)
java = json.load(javaOpen)

hoho = {
    "savefile": False,
    "namefile": "",
}

chatbot = {
    "admin": [],
    "botMute": [],
    "botOff": [],
}

read = { 
    "readMember": {},
    "readPoint": {}
}

wmin = {
    "wMessage": False,
    "textnya": "Enjoying in this group",
}

lvin = {
    "lMessage": False,
    "textnya": "See u next time",
}

tailah = {
    "siderTemp": {},
    "siderPesan": "You can join chat?",
}

setbot = {
    "background": "#000000",
    "text": "#ffffff",
    "separator": "#ffffff",
    "helptext": "#00FFFF",
    "helpseparator": "#00FFFF"
}

gwcool = {
    "squad": "LUX-STORE™",
}

javascript = {
    "jskick": "bypass",
    "jskick1": "cleanse",
    "cancels": "cancel",
}
#=====================================================================
def QRV2(to):
    apiKey = "KGAdZcw6zAIO"
    headers = {
        "apiKey":apiKey, ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
        "appName": "DESKTOPWIN\t6.2.2\tDESKTOPWIN\t10.0",
        "cert" : None, ## IF YOU WANT LOGIN WITH CERT
        "server": random.choice(["pool-1","pool-2"]), ## IP POOL SELECTION: pool-1 / pool-2 / vip(COMING SOON)
        "sysname": "LUXTeam" ## SYSTEM NAME, YOU CAN CUSTOMIZE IT
        }
    main = json.loads(requests.get("https://api.be-team.me/qrv2",headers=headers).text)
    enesbyrk.sendMessage(to,"Lütfen 2 dakika içinde linke giriş yapın:-\n " + main["result"]["qr_link"])
    #print("Login IP: " + main["result"]["login_ip"])
    if not headers["cert"]:
        enesbyrk.sendMessage(to,main["result"]["cb_pincode"])
        enesbyrk.sendMessage(to, "Önce şu linki kopyala 👆👆👆 Tokene giriş yaptıktan sonra internet tarayıcına yapıştırıp pinkodunu görebilirsin..")
        result = json.loads(requests.get(main["result"]["cb_pincode"],headers=headers).text)
        enesbyrk.sendMessage(to,"Pin Kodu: " + result["result"])
    result = json.loads(requests.get(main["result"]["cb_token"],headers=headers).text)
    if result["status"] != 200:
        print("[ Error ] "+ result["reason"])
    else:
      #  print("Your Cert: " + result["result"]["cert"])
        return result["result"]["token"]
#=====================================================================
settings["myProfile"]["displayName"] = enesbyrkProfile.displayName
settings["myProfile"]["statusMessage"] = enesbyrkProfile.statusMessage
settings["myProfile"]["pictureStatus"] = enesbyrkProfile.pictureStatus
cont = enesbyrk.getContact(enesbyrkMID)
settings["myProfile"]["videoProfile"] = cont.videoProfile
coverId = enesbyrk.getProfileDetail()["result"]["objectId"]
settings["myProfile"]["coverId"] = coverId
#=====================================================================
#=====================================================================
with open("enesbyrk/temp.json", "r", encoding="utf_8_sig") as f:
    anu = json.loads(f.read())
    anu.update(settings)
    settings = anu
with open("enesbyrk/wait.json", "r", encoding="utf_8_sig") as f:
    itu = json.loads(f.read())
    itu.update(wait)
    wait = itu
with open('by.json', 'r') as fp:
    wait = json.load(fp)
def sendFooter(to, isi):
    data = {
        "type": "text",
        "text": isi,
        "sentBy": {
            "label": "LUX-STORE™",
            "iconUrl": "https://obs.line-scdn.net/{}".format(enesbyrk.getContact('u8894217061510fa60bf2592338441704').pictureStatus),
            "linkUrl": "line://ti/p/~parazit0nline"
        }
    }
    sendTemplate(to, data)
def sendTemplate(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1609119464-PAkYKJ7J', xyzz)
    token = enesbyrk.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
def bcTemplate(gr, data):
    xyz = LiffChatContext(gr)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1609119464-PAkYKJ7J', xyzz)
    token = client.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
def sendTemplate(group, data):
    xyz = LiffChatContext(group)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1609119464-PAkYKJ7J', xyzz)
    token = enesbyrk.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

def helppss(to):
    data={"type":"flex","altText":"LUX-STORE™","contents":{
  "type": "carousel",
  "contents": [
    {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://i.ibb.co/PGJt3qP/Pics-Art-12-07-05-41-20.png"
                  }
                ],
                "cornerRadius": "100px",
                "borderColor": "#ffffff",
                "borderWidth": "2px",
                "width": "40px",
                "height": "40px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "LUX-STORE™",
                    "size": "xl",
                    "color": "#ffffff",
                    "weight": "bold"
                  }
                ],
                "margin": "lg"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://i.ibb.co/PGJt3qP/Pics-Art-12-07-05-41-20.png"
                  }
                ],
                "cornerRadius": "100px",
                "borderColor": "#ffffff",
                "borderWidth": "2px",
                "width": "40px",
                "height": "40px"
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "spacer",
                "size": "xxl"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Chatbot",
                            "size": "sm",
                            "color": "#ffffff",
                            "align": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=chatbot"
                            }
                          }
                        ]
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Feature",
                            "align": "center",
                            "size": "sm",
                            "color": "#ffffff",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=feature"
                            }
                          }
                        ]
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Images",
                            "size": "xs",
                            "color": "#ffffff",
                            "align": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=images"
                            }
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "type": "separator"
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Profile",
                            "size": "xs",
                            "color": "#ffffff",
                            "align": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=profile"
                            }
                          }
                        ]
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Protect",
                            "align": "center",
                            "color": "#ffffff",
                            "size": "xs",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=protect"
                            }
                          }
                        ]
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Social",
                            "size": "xs",
                            "color": "#ffffff",
                            "align": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=social"
                            }
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "type": "separator"
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "text",
                        "text": "Timeline",
                        "size": "sm",
                        "color": "#ffffff",
                        "align": "center",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=timeline"
                        }
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Translate",
                            "size": "sm",
                            "color": "#ffffff",
                            "align": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=translate"
                            }
                          }
                        ]
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Settings",
                            "size": "xs",
                            "color": "#ffffff",
                            "align": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=settings"
                            }
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ],
            "borderColor": "#ffffff",
            "borderWidth": "2px"
          }
        ]
      }
    ],
    "cornerRadius": "xl",
    "borderColor": "#ffffff",
    "borderWidth": "4px"
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    }
  }},{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://i.ibb.co/PGJt3qP/Pics-Art-12-07-05-41-20.png"
                  }
                ],
                "cornerRadius": "100px",
                "borderColor": "#ffffff",
                "borderWidth": "2px",
                "width": "40px",
                "height": "40px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "LUX-STORE™",
                    "size": "xl",
                    "color": "#ffffff",
                    "weight": "bold"
                  }
                ],
                "margin": "lg"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://i.ibb.co/PGJt3qP/Pics-Art-12-07-05-41-20.png"
                  }
                ],
                "cornerRadius": "100px",
                "borderColor": "#ffffff",
                "borderWidth": "2px",
                "width": "40px",
                "height": "40px"
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "spacer",
                "size": "xxl"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Banning",
                            "size": "sm",
                            "color": "#ffffff",
                            "align": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=banning"
                            }
                          }
                        ]
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Wordban",
                            "align": "center",
                            "size": "sm",
                            "color": "#ffffff",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=wordban"
                            }
                          }
                        ]
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Friend",
                            "size": "xs",
                            "color": "#ffffff",
                            "align": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=friend"
                            }
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "type": "separator"
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Self",
                            "size": "xs",
                            "color": "#ffffff",
                            "align": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=self"
                            }
                          }
                        ]
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Memegen",
                            "align": "center",
                            "color": "#ffffff",
                            "size": "xs",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=memegen"
                            }
                          }
                        ]
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Kick",
                            "size": "xs",
                            "color": "#ffffff",
                            "align": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=kick"
                            }
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "type": "separator"
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "text",
                        "text": "Utility",
                        "size": "sm",
                        "color": "#ffffff",
                        "align": "center",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=utility"
                        }
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Github",
                            "size": "sm",
                            "color": "#ffffff",
                            "align": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=github"
                            }
                          }
                        ]
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "About",
                            "size": "xs",
                            "color": "#ffffff",
                            "align": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=about"
                            }
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ],
            "borderColor": "#ffffff",
            "borderWidth": "2px"
          }
        ]
      }
    ],
    "cornerRadius": "xl",
    "borderColor": "#ffffff",
    "borderWidth": "4px"
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    }
  }},{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://i.ibb.co/PGJt3qP/Pics-Art-12-07-05-41-20.png"
                  }
                ],
                "cornerRadius": "100px",
                "borderColor": "#ffffff",
                "borderWidth": "2px",
                "width": "40px",
                "height": "40px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "LUX-STORE™",
                    "size": "xl",
                    "color": "#ffffff",
                    "weight": "bold"
                  }
                ],
                "margin": "lg"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://i.ibb.co/PGJt3qP/Pics-Art-12-07-05-41-20.png"
                  }
                ],
                "cornerRadius": "100px",
                "borderColor": "#ffffff",
                "borderWidth": "2px",
                "width": "40px",
                "height": "40px"
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "spacer",
                "size": "xxl"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Group",
                            "size": "sm",
                            "color": "#ffffff",
                            "align": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=group"
                            }
                          }
                        ]
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Mention",
                            "align": "center",
                            "size": "sm",
                            "color": "#ffffff",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=mention"
                            }
                          }
                        ]
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Steal",
                            "size": "xs",
                            "color": "#ffffff",
                            "align": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=steal"
                            }
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "type": "separator"
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "List",
                            "size": "xs",
                            "color": "#ffffff",
                            "align": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=list"
                            }
                          }
                        ]
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Bcast",
                            "align": "center",
                            "color": "#ffffff",
                            "size": "xs",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=bcast"
                            }
                          }
                        ]
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Leave",
                            "size": "xs",
                            "color": "#ffffff",
                            "align": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text="
                            }
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "type": "separator"
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "text",
                        "text": "Reboot",
                        "size": "sm",
                        "color": "#ffffff",
                        "align": "center",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=reboot"
                        }
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Timeleft",
                            "size": "sm",
                            "color": "#ffffff",
                            "align": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=timeleft"
                            }
                          }
                        ]
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Logout",
                            "size": "xs",
                            "color": "#ffffff",
                            "align": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=logout"
                            }
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ],
            "borderColor": "#ffffff",
            "borderWidth": "2px"
          }
        ]
      }
    ],
    "cornerRadius": "xl",
    "borderColor": "#ffffff",
    "borderWidth": "4px"
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    }}}]}}
    sendTemplate(to,data)

def helpalay(to):
    data={"type":"flex","altText":"LUX-STORE™","contents":{
  "type": "carousel",
  "contents": [
    {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "borderWidth": "4px",
    "borderColor": "{}".format(setbot["helpseparator"]),
    "cornerRadius": "xl",
    "contents": [
      {
        "type": "image",
        "url": "https://i.imgyukle.com/2020/08/29/ufH3d8.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "1:1",
        "gravity": "center"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "LUX-STORE™",
                    "size": "lg",
                    "color": "{}".format(setbot["text"]),
                    "weight": "bold",
                    "align": "center",
                    "offsetStart": "15px"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Selfbots Edition",
                    "size": "sm",
                    "color": "{}".format(setbot["text"]),
                    "weight": "bold",
                    "align": "center"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "spacer"
                  }
                ],
                "margin": "xs"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "Login",
                        "size": "sm",
                        "color": "{}".format(setbot["helptext"]),
                        "align": "center",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=Login"
                        }
                      }
                    ],
                    "offsetStart": "0px"
                  },
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "Logout",
                        "size": "sm",
                        "color": "{}".format(setbot["helptext"]),
                        "align": "center",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=Logout"
                        }
                      }
                    ],
                    "offsetStart": "10px"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "margin": "md"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "Giriş",
                        "size": "sm",
                        "color": "{}".format(setbot["helptext"]),
                        "align": "center",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=Giriş"
                        }
                      },
                      {
                        "type": "spacer"
                      }
                    ],
                    "offsetStart": "0px"
                  },
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "Çıkış",
                        "size": "sm",
                        "color": "{}".format(setbot["helptext"]),
                        "align": "center",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=Çıkış"
                        }
                      }
                    ],
                    "offsetStart": "10px"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "margin": "xl"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "Reader",
                        "size": "sm",
                        "color": "{}".format(setbot["helptext"]),
                        "align": "center",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=Reader"
                        }
                      }
                    ],
                    "offsetStart": "0px"
                  },
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "Mentions",
                        "size": "sm",
                        "color": "{}".format(setbot["helptext"]),
                        "align": "center",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=Mentions"
                        }
                      }
                    ],
                    "offsetStart": "10px"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "margin": "sm"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "spacer",
                    "size": "xxl"
                  },
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "Addservice @",
                        "color": "{}".format(setbot["helptext"]),
                        "align": "center",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=Addservice"
                        }
                      }
                    ],
                    "margin": "lg",
                    "offsetEnd": "20px"
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Helper2",
                            "size": "sm",
                            "color": "{}".format(setbot["helptext"]),
                            "align": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=Helper2"
                            }
                          }
                        ],
                        "offsetEnd": "20px"
                      },
                      {
                        "type": "filler"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Helper3",
                            "size": "sm",
                            "color": "{}".format(setbot["helptext"]),
                            "align": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=Helper3"
                            }
                          }
                        ],
                        "offsetEnd": "40px"
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "margin": "md"
                  }
                ],
                "margin": "md"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  }
                ],
                "margin": "sm"
              }
            ],
            "spacing": "xs"
          }
        ],
        "position": "absolute",
        "offsetBottom": "0px",
        "offsetStart": "0px",
        "offsetEnd": "0px",
        "paddingAll": "20px"
      }
    ],
    "paddingAll": "0px"
  }
}]}}
    sendTemplate(to, data)
def foro(to, text):
    data = {
    "type": "flex",
    "altText": text,
    "contents": {
    "type": "bubble",
    "styles": {
    "footer": {
    "backgroundColor": "{}".format(setbot["background"])
    }
    },
    "footer": {
    "type": "box",
    "layout": "vertical",
     "cornerRadius": "xl",
    "borderWidth": "4px",
    "borderColor": "{}".format(setbot["separator"]),
    "spacing": "sm",
    "contents": [
    {
    "type": "box",
    "layout": "baseline",
    "contents": [
    {
    "type": "icon",
    "url": "https://i.ibb.co/PGJt3qP/Pics-Art-12-07-05-41-20.png",
    "size": "md"
    },
    {
    "type": "text",
    "text": text,
    "color": "{}".format(setbot["text"]),
    "gravity": "center",
    "align":"center",
    "wrap": True,
    "size": "md"
    },
    {
    "type": "icon",
    "url": "https://i.ibb.co/PGJt3qP/Pics-Art-12-07-05-41-20.png",
    "size": "md"
    },
    ]
    }
    ]
    }
    }
    }
    sendTemplate(to, data)
def helpss(to):
    ret_ = helpers(to)
    k = len(ret_)//10
    for aa in range(k+1):
        data = {
            "type": "flex",
            "altText": "Help",
            "contents": {
                "type": "carousel",
                "contents": ret_[aa*10 : (aa+1)*10]
            }
        }
        sendTemplate(to, data)
def helpers(to):
    ret_ = []
    ret_.append(
        {
            "styles": {"body": {"backgroundColor": "{}".format(setbot["background"])},"header": {"backgroundColor": "{}".format(setbot["background"])}},
            "type": "bubble",
            "body": {"contents": [{
                "type": "box",
                "layout": "baseline",
                "contents": [
                    {
                        "type": "spacer",
                        "size": "xxl"
                    },
                    {
                        "contents": [{
                        "url": "https://i.ibb.co/PGJt3qP/Pics-Art-12-07-05-41-20.png",
                        "size": "xxs",
                        "type": "image",
                        "action": {
                        "type": "uri",
                        "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=Login%20sb"
                    }
                }, {
                                                    "url": "https://i.ibb.co/PGJt3qP/Pics-Art-12-07-05-41-20.png",
                                                    "size": "xxs",
                                                    "type": "image",
                                                    "action": {
                                                        "type": "uri",
                                                        "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=Restart%20sb"
                                                    }
                                                },{
                                                    "url": "https://i.ibb.co/PGJt3qP/Pics-Art-12-07-05-41-20.png",
                                                    "size": "xxs",
                                                   "type": "image",
                                                    "action": {
                                                        "type": "uri",
                                                        "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=Logout%20sb"
                                                    }
                                                }],
                                                "layout": "horizontal",
                                                "type": "box",
                                                "flex": 1
                                            }, 
                                                                 {
        "type": "box",
        "layout": "horizontal",
        "spacing": "xxl",       
        "contents": [
          {
            "type": "text", 
            "text": 'Login sb',
            "color": "{}".format(setbot["text"]),
            "size": "xs",
            "align": "center",
          },
          {
            "type": "text",
            "text": 'Restart sb',
            "color": "{}".format(setbot["text"]),
            "size": "xs",
            "align": "center"
          },
          {
            "type": "text", 
            "text": 'Logout sb',
            "color": "{}".format(setbot["text"]),
            "size": "xs"
          }
        ]
      },
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "contents": [
              {
       "type": "spacer",
       "size": "xl"
     }
],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }  
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical",
      }
    }
    )
    ret_.append(
        {
            "styles": {"body": {"backgroundColor": "{}".format(setbot["background"])},"header": {"backgroundColor": "{}".format(setbot["background"])}},
            "type": "bubble",
            "body": {"contents": [{
                "type": "box",
                "layout": "baseline",
                "contents": [
                    {
                        "type": "spacer",
                        "size": "xxl"
                    },
                    {
                        "contents": [{
                        "url": "https://i.ibb.co/PGJt3qP/Pics-Art-12-07-05-41-20.png",
                        "size": "xxs",
                        "type": "image",
                        "action": {
                        "type": "uri",
                        "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=Reader"
                    }
                }, {
                                                    "url": "https://i.ibb.co/PGJt3qP/Pics-Art-12-07-05-41-20.png",
                                                    "size": "xxs",
                                                    "type": "image",
                                                    "action": {
                                                        "type": "uri",
                                                        "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=Support"
                                                    }
                                                },{
                                                    "url": "https://i.ibb.co/PGJt3qP/Pics-Art-12-07-05-41-20.png",
                                                    "size": "xxs",
                                                   "type": "image",
                                                    "action": {
                                                        "type": "uri",
                                                        "uri": "line://app/1609119464-PAkYKJ7J?type=fotext&text=Mentions"
                                                    }
                                                }],
                                                "layout": "horizontal",
                                                "type": "box",
                                                "flex": 1
                                            }, 
                                                                 {
        "type": "box",
        "layout": "horizontal",
        "spacing": "xxl",       
        "contents": [
          {
            "type": "text", 
            "text": 'Reader',
            "color": "{}".format(setbot["text"]),
            "size": "xs",
            "align": "center",
          },
          {
            "type": "text",
            "text": 'Support',
            "color": "{}".format(setbot["text"]),
            "size": "xs",
            "align": "center"
          },
          {
            "type": "text", 
            "text": 'Mentions',
            "color": "{}".format(setbot["text"]),
            "size": "xs"
          }
        ]
      },
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "contents": [
              {
       "type": "spacer",
       "size": "xl"
     }
],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }  
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical",
      }
    }
    )
    return ret_

def debug():
    get_profile_time_start = time.time()
    get_profile = enesbyrk.getProfile()
    get_profile_time = time.time() - get_profile_time_start
    get_group_time_start = time.time()
    get_group = enesbyrk.getGroupIdsJoined()
    get_group_time = time.time() - get_group_time_start
    get_contact_time_start = time.time()
    get_contact = enesbyrk.getContact(get_profile.mid)
    get_contact_time = time.time() - get_contact_time_start
    elapsed_time = time.time() - get_profile_time_start
    return " 「 Debug 」\n - Send Message\n   %.5f\n - Get Profile\n   %.5f\n - Get Contact\n   %.5f\n - Get Group\n   %.5f" % (elapsed_time,get_profile_time,get_contact_time,get_group_time)
#=====================================================================
def powpow():
    Headers = {
    'User-Agent': "Line/8.9.1",
    'X-Line-Application': "IOSIPAD\t11.2.5\tiPhone X\t11.2.5",
    "x-lal": "ja-US_US",
    }
    return Headers
def getmytoken():
    Headers = {
    'User-Agent': "Line/8.9.1",
    'X-Line-Application': "IOSIPAD\t11.2.5\tiPhone X\t11.2.5",
    "x-lal": "ja-US_US",
    }
    return Headers
def shareall(to, text):
    lol = enesbyrk.getGroupIdsJoined()
    for group in lol:
        enesbyrk.sendPostToTalk(group, text)
    enesbyrk.sendMessage(to, "Share in {} group".format(str(len(lol))))
#=====================================================================
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
#=====================================================================
#def Template(to):
def sendMessageCustom(to, text, icon , name):
    annda = {'MSG_SENDER_ICON': icon,
        'MSG_SENDER_NAME':  name,
    }
    enesbyrk.sendMessage(to, text, contentMetadata=annda)
def sendMessageCustomContact(to, icon, name, mid):
    annda = { 'mid': mid,
    'MSG_SENDER_ICON': icon,
    'MSG_SENDER_NAME':  name,
    }
    enesbyrk.sendMessage(to, '', annda, 13)

def B64e(to, url):
	import base64
	return enesbyrk.sendMessage(to, base64.b64encode(url.encode()).decode())

def B64d(to, url):
	import base64
	return enesbyrk.sendMessage(to, base64.b64decode(url.encode()).decode())
	
def sendMention(to, mid, firstmessage='', lastmessage=''):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        try:
            enesbyrk.sendMessage(to, text, {'MSG_SENDER_NAME': enesbyrk.getContact(mid).displayName,'MSG_SENDER_ICON': "http://dl.profile.line-cdn.net/" + enesbyrk.getContact(mid).pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        except Exception as e:
            enesbyrk.sendMessage(to, text, {'MSG_SENDER_NAME': enesbyrk.getContact("u085311ecd9e3e3d74ae4c9f5437cbcb5").displayName,'MSG_SENDER_ICON': 'http://dl.profile.line-cdn.net/' + enesbyrk.getContact("u085311ecd9e3e3d74ae4c9f5437cbcb5").pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        print(error)
def mentions(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@PydrFans  "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    enesbyrk.sendMessage(to, textx, {'AGENT_NAME':'LINE OFFICIAL', 'AGENT_LINK': 'line://ti/p/~{}'.format(enesbyrk.getProfile().userid), 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + enesbyrk.getContact("u085311ecd9e3e3d74ae4c9f5437cbcb5").picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = enesbyrk.genOBSParams({'oid': enesbyrkMID, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = enesbyrk.server.postContent('{}/talk/vp/upload.nhn'.format(str(enesbyrk.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        enesbyrk.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))
        os.remove("enesbyrkWasHere.mp4")
#=====================================================================
def speedtest(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weaks, days = divmod(days,7)
    if days == 0:
        return '%02d' % (secs)
    elif days > 0 and weaks == 0:
        return '%02d' %(secs)
    elif days > 0 and weaks > 0:
        return '%02d' %(secs)
        
def change(url):
	import base64
	return base64.b64encode(url.encode()).decode()
	
def tagdia(to, text="",ps='', mids=[]):
        arrData = ""
        arr = []
        mention = "@MentionOrang "
        if mids == []:
            raise Exception("Invalid mids")
        if "@!" in text:
            if text.count("@!") != len(mids):
                raise Exception("Invalid mids")
            texts = text.split("@!")
            textx = ''
            h = ''
            for mid in range(len(mids)):
                h+= str(texts[mid].encode('unicode-escape'))
                textx += str(texts[mid])
                if h != textx:slen = len(textx)+h.count('U0');elen = len(textx)+h.count('U0') + 13
                else:slen = len(textx);elen = len(textx) + 13
                arrData = {'S':str(slen), 'E':str(elen), 'M':mids[mid]}
                arr.append(arrData)
                textx += mention
            textx += str(texts[len(mids)])
        else:
            textx = ''
            slen = len(textx)
            elen = len(textx) + 18
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
            arr.append(arrData)
            textx += mention + str(text)
        enesbyrk.sendMessage(to, textx, {'MSG_SENDER_NAME': client.getContact(ps).displayName,'MSG_SENDER_ICON': "http://dl.profile.line-cdn.net/" + enesbyrk.getContact(ps).pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
#=====================================================================
def logError(text):
    enesbyrk.log("ERROR 404 !\n" + str(text))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + " | " + inihari.strftime('%H:%M:%S')
    with open("enesbyrk/errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
#=====================================================================
#=====================================================================
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
#=====================================================================
def likeNotify(to):
    true = True
    data = {
        "type": "flex",
        "altText": "LIKE BILDIRIMI",
        "contents": {
            "type": "bubble",
            "styles": {
                "header": {
                    "backgroundColor": "#333333"
                },
                "hero": {
                    "backgroundColor": "#333333"
                },
                "body": {
                    "backgroundColor": "#FFFFFF",
                    "separator": true,
                    "separatorColor": "#FFFFFF"
                },
                "footer": {
                    "backgroundColor": "#333333",
                    "separator": true
                }
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "LIKE BILDIRIMI",
                        "weight": "bold",
                        "size": "xxl",
                        "color": "#000000",
                        "margin": "md"
                    },
                    {
                        "type": "text",
                        "text": "Your Post Has Been Liked",
                        "size": "xs",
                        "color": "#aaaaaa",
                        "wrap": true
                    },
                    {
                        "type": "separator",
                        "margin": "xxl"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "xxl",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "SELFBOT KİRALA",
                                        "weight": "bold",
                                        "color": "#000000",
                                        "size": "sm",
                                        "flex": 0
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "ÖDEME :",
                                        "size": "sm",
                                        "color": "#aaaaaa",
                                        "flex": 0
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "• Selfbot",
                                        "size": "sm",
                                        "color": "#aaaaaa",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "80 ₺",
                                        "size": "sm",
                                        "color": "#aaaaaa",
                                        "align": "end"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "• Helper",
                                        "size": "sm",
                                        "color": "#aaaaaa",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "300 ₺",
                                        "size": "sm",
                                        "color": "#aaaaaa",
                                        "align": "end"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "• KORUMA",
                                        "size": "sm",
                                        "color": "#aaaaaa",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "150 ₺",
                                        "size": "sm",
                                        "color": "#aaaaaa",
                                        "align": "end"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Get free 100 accounts autolike bots",
                                        "size": "sm",
                                        "color": "#aaaaaa",
                                        "flex": 0
                                    }
                                ]
                            },
                            {
                                "type": "separator",
                                "margin":"md"
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "margin": "md",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Sunucu mu istiyorsun ?",
                                "size": "xs",
                                "color": "#000000",
                                "flex": 0
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "md",
                        "contents": [
                            {
                                "type": "spacer",
                                "size": "xl"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "uri",
                                    "label": "İletişime geç",
                                    "uri": "line://ti/p/~parazit0nline"
                                },
                                "style": "primary",
                                "color": "#000000"
                            }
                        ]
                    }
                ]
            }
        }
    }
    sendTemplate(to, data)
#=====================================================================
def removeCmd(cmd, text):
	key = settings["keyCommand"]
	if settings["setKey"] == False: key = ''
	rmv = len(key + cmd) + 1
	return text[rmv:]
def backupData():
    try:
        backup = settings
        f = codecs.open('enesbyrk/temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = wait
        f = codecs.open('enesbyrk/wait.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = premium
        f = codecs.open('enesbyrk/user.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = java
        f = codecs.open('enesbyrk/java.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        f = codecs.open('by.json','w','utf-8')
        json.dump(wait, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = premium
        return True
    except Exception as error:
        logError(error)
        return False
#=====================================================================
def bcTemplate(gr, data):
    xyz = LiffChatContext(gr)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1609119464-PAkYKJ7J', xyzz)
    token = enesbyrk.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
#=====================================================================
async def enesbyrkBot(op):
    try:
        if settings["restartPoint"] != None:
            enesbyrk.sendMessage(settings["restartPoint"], 'Activated♪')
            settings["restartPoint"] = None
        if op.type == 0:
            return
                        
        if op.type in [22,24]:
            enesbyrk.leaveRoom(op.param1)
#=====================================================================
        if op.type == 13:
            if enesbyrk.getProfile().mid in op.param3:
                G = enesbyrk.getCompactGroup(op.param1)
                if settings["autoJoin"] == True:
                    enesbyrk.acceptGroupInvitation(op.param1)
        if op.type == 15:
            #print ("[ 15 ] NOTIFIED LEAVE GROUP")
            if lvin["lMessage"] == True:
                mat = enesbyrk.getContact(op.param2)
                fit = enesbyrk.getCompactGroup(op.param1)
                pesanya = lvin["textnya"]
                data={"type":"flex","altText":"LUX-STORE™","contents":{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                          {
                            "type": "image",
                            "url": "https://obs.line-scdn.net/{}".format(mat.pictureStatus)
                          }
                        ],
                        "width": "60px",
                        "height": "60px",
                        "borderWidth": "2px",
                        "borderColor": "#ffffff",
                        "cornerRadius": "100px"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Bye bye {}".format(str(mat.displayName)),
                            "weight": "bold",
                            "size": "md",
                            "color": "#ffffff",
                            "wrap": True
                          },
                          {
                            "type": "text",
                            "text": "{}".format(pesanya),
                            "weight": "bold",
                            "size": "md",
                            "color": "#ffffff",
                            "wrap": True,
                          }
                        ],
                        "margin": "lg"
                      }
                    ]
                  }
        ],
        "paddingAll": "13px",
        "backgroundColor": "#000000",
        "cornerRadius": "2px",
        "margin": "xl"
      }
    ],
    "paddingAll": "0px"
  }
}}
                sendTemplate(op.param1,data)
        if op.type == 17:
            #print ("[ 17 ] NOTIFIED INVITE INTO GROUP")
            if wmin["wMessage"] == True:
                mat = enesbyrk.getContact(op.param2)
                fit = enesbyrk.getCompactGroup(op.param1)
                pesanya = wmin["textnya"]
                data={"type":"flex","altText":"LUX-STORE™","contents":{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                          {
                            "type": "image",
                            "url": "https://obs.line-scdn.net/{}".format(mat.pictureStatus)
                          }
                        ],
                        "width": "60px",
                        "height": "60px",
                        "borderWidth": "2px",
                        "borderColor": "#ffffff",
                        "cornerRadius": "100px"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Hello {}".format(str(mat.displayName)),
                            "weight": "bold",
                            "size": "md",
                            "color": "#ffffff",
                            "wrap": True
                          },
                          {
                            "type": "text",
                            "text": "Welcome to {}".format(str(fit.name)),
                            "weight": "bold",
                            "size": "md",
                            "color": "#ffffff",
                            "wrap": True,
                          },
                          {
                            "type": "text",
                            "text": "{}".format(pesanya),
                            "weight": "bold",
                            "size": "md",
                            "color": "#ffffff",
                            "wrap": True,
                          }
                        ],
                        "margin": "lg"
                      }
                    ]
                  }
        ],
        "paddingAll": "13px",
        "backgroundColor": "#000000",
        "cornerRadius": "2px",
        "margin": "xl"
      }
    ],
    "paddingAll": "0px"
  }
}}
                sendTemplate(op.param1,data)
        if op.type == 19:
                    khie = enesbyrk.getContact(op.param2)
                    ayu = enesbyrk.getContact(op.param3)
                    data={"type":"flex","altText":"LUX-STORE™","contents":{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "cornerRadius": "xl",
    "borderWidth": "4px",
    "borderColor": "#ffffff",
    "contents": [
      {
        "type": "text",
        "text": "KICK NOTIFY",
        "weight": "bold",
        "size": "xxl",
        "margin": "md"
      },
      {
        "type": "separator",
        "color": "#000000"
      },
      {
        "type": "text",
        "text": "Execution :",
        "weight": "bold",
        "size": "md",
        "margin": "md"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(khie.pictureStatus),
                "aspectMode": "cover",
                "size": "full"
              }
            ],
            "cornerRadius": "100px",
            "width": "30px",
            "height": "30px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": f"{enesbyrk.getContact(op.param2).displayName}",
                    "size": "md",
                    "color": "#000000"
                  }
                ],
                "spacing": "md",
                "margin": "sm",
                "offsetTop": "2px"
              }
            ]
          }
        ],
        "spacing": "xl",
        "paddingAll": "6px"
      },
      {
        "type": "text",
        "text": "Victim :",
        "weight": "bold",
        "size": "md",
        "margin": "md"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(ayu.pictureStatus),
                "aspectMode": "cover",
                "size": "full"
              }
            ],
            "cornerRadius": "100px",
            "width": "30px",
            "height": "30px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": f"{enesbyrk.getContact(op.param3).displayName}",
                    "size": "md",
                    "color": "#000000"
                  }
                ],
                "spacing": "md",
                "margin": "sm",
                "offsetTop": "2px"
              }
            ]
          }
        ],
        "spacing": "xl",
        "paddingAll": "6px"
      }
    ],
    "paddingAll": "0px"
  }
}}
                    sendTemplate(op.param1,data)
#=====================================================================
        if op.type == 26:
            #print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            khietag = "ud90a462b1164062d021fc190136ccd52"
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != enesbyrkMID: to = sender
                else: to = receiver
                if msg.contentType == 6:
                    try:
                        contact = enesbyrk.getContact(sender)
                        if msg.toType == 2:
                            anu = enesbyrk.getGroup(to)
                            if msg.contentMetadata['GC_EVT_TYPE'] == 'S' and msg.contentMetadata['GC_MEDIA_TYPE'] == 'LIVE':
                                anu = msg.contentMetadata={'GC_EVT_TYPE': 'S', 'GC_CHAT_MID': to, 'RESULT': 'INFO', 'SKIP_BADGE_COUNT': 'false', 'GC_IGNORE_ON_FAILBACK': 'false', 'TYPE': 'G', 'DURATION': '0', 'GC_MEDIA_TYPE': 'VIDEO', 'VERSION': 'X', 'CAUSE': '16'}
                    except Exception as e:
                        enesbyrk.sendMessage(to, str(e))
                if msg.contentType == 14:
                    if hoho["savefile"] == True:
                        try:
                             namafile = hoho["namafile"]
                             enesbyrk.downloadObjectMsg(msg_id,saveAs=namafile)
                             hoho["savefile"] = False
                             enesbyrk.sendMessage(to, "Successful, the file has been uploaded")
                        except Exception as e:
                         	enesbyrk.sendMessage(to, str(e))
                if msg.contentType == 1:
                    if settings["changePicture"] == True:
                        path = enesbyrk.downloadObjectMsg(msg_id, saveAs="tmp/pict.bin")
                        settings["changePicture"] = False
                        enesbyrk.updateProfilePicture(path)
                        sendFooter(to,"Profile Image Updated.")
                if msg.contentType == 1: 
                    if settings["changeCoverProfile"] == True:
                        path = enesbyrk.downloadObjectMsg(msg_id)
                        settings["changeCoverProfile"] = False
                        enesbyrk.updateProfileCover(path)
                        sendFooter(to,"Cover Image Updated.")                                           
                if msg.contentType in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]:
                    if msg.toType == 0:
                        if settings["autoRead"] == True:
                            enesbyrk.sendChatChecked(to, msg_id)
                    if msg.toType == 2:
                        if settings["autoRead1"] == True:
                            enesbyrk.sendChatChecked(to, msg_id)
                if msg.contentType == 0:
                    if "/ti/g/" in text.lower():
                        if settings["autoJoin"] == True:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                   n_links.append(l)
                            for ticket_id in n_links:
                                group = enesbyrk.findGroupByTicket(ticket_id)
                                if len(group.members) >= wait["Members"]:
                                    enesbyrk.acceptGroupInvitationByTicket(group.id,ticket_id)
                                else:
                                    enesbyrk.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    enesbyrk.leaveGroup(group.id)
                    if msg._from in myAdmin:
                        if "/remote" in cmd:
                            function = lambda s:s[:1].lower() + s[1:] if s else ''
                            number = cmd.split("/remote:")[1];number = number.split()[0];enesbyrk.getGroupIdsJoined()
                            if number.isdigit():number = int(number);group = enesbyrk.getGroupIdsJoined()[number-1];to = group
                            cmd = cmd.replace("/remote:%s"%number,"").lstrip().rstrip()
                            if '/remote:' in text:text = text.replace("/remote:%s"%number,"").lstrip().rstrip();function(text)
                            else:text = text.replace("/remote:%s"%number,"").lstrip().rstrip();function(text)
                            if msg.toType == 0:msg.to = sender
                            elif msg.toType == 2:msg.to = msg.to
                            sendFooter(msg.to, "Command '%s' has been send to : %s" % (cmd, enesbyrk.getGroup(group).name))
#==========================================
                    if cmd == "threads":
                        enesbyrk.sendMessage(to,'Threads: {}'.format(threading.active_count()))
                        log.info("Debug Threads.")                            
#==========================================
                    elif cmd.startswith("savefile"):
                        if msg._from in myAdmin:
                            text = removeCmd("savefile", text)
                            sep = text.split(" ")
                            key = text.replace(sep[0] + " ", text)
                            if " " in key:
                                enesbyrk.sendMessage(to, "Failed !")
                            else:
                                hoho["namafile"] = str(key).lower()
                                hoho["savefile"] = True
                                enesbyrk.sendMessage(to, "Send file to save to be「 {} 」".format(str(key).lower()))
                    elif cmd.startswith("exec"):
                        if msg._from in myAdmin:
                            try:
                                sep = text.split("\n")
                                txt = text.replace(sep[0] + "\n","")
                                exec(txt)
                            except:
                                pass
#==========================================
                    elif cmd.startswith("down "):
                        if msg._from in myAdmin:
                           number = removeCmd("down", text)
                           if len(number) > 0:
                               if number.isdigit():
                                   number = int(number)
                                   if number > 5000:                                             
                                       enesbyrk.sendMessage(to,"invalid >_< ! Max: 5000.")
                                   else:
                                       for i in range(0,number):
                                           enesbyrk.sendMessage(to,str(number))
                                           number -= 1
                                           time.sleep(0.008)
                               else:
                                  enesbyrk.sendMessage(to,"Please specify a valid number.")
                    elif cmd == "change dp" :
                        if msg._from in myAdmin:
                            settings["changePicture"] = True
                            sendFooter(to, "Send a Image to change picture.")
                    elif cmd == "change cover":
                        if msg._from in myAdmin:
                            settings["changeCoverProfile"] = True
                            sendFooter(to,"Send a Image to change cover.")
                    elif cmd == "read on":
                        tailah["siderTemp"][receiver] = []
                        sendFooter(to, "Getreader set to on.")
                    elif cmd == "read off":
                        if receiver in tailah["siderTemp"]:
                            del tailah["siderTemp"][receiver]
                            sendFooter(to, "Getreader set to off.")
                    elif cmd == "welcome on":
                        if wmin["wMessage"] == True:
                            msgs=" 「 Welcome 」\nWelcomemsg already Enable♪"
                        else:
                            msgs=" 「 Welcome 」\nWelcomemsg set to Enable♪"
                            wmin["wMessage"] = True
                        sendFooter(to, msgs)
                    elif cmd == "welcome off":
                        if wmin["wMessage"] == False:
                            msgs=" 「 wMessage 」\nWelcomemsg already DISABLED♪"
                        else:
                            msgs=" 「 Welcome 」\nWelcomemsg set to DISABLED♪"
                            wmin["wMessage"] = False
                        sendFooter(to, msgs)
                    elif cmd == "leave on":
                        if lvin["lMessage"] == True:
                            msgs=" 「 Leave 」\nLeavemsg already Enable♪"
                        else:
                            msgs=" 「 Leave 」\nLeavemsg set to Enable♪"
                            lvin["lMessage"] = True
                        sendFooter(to, msgs)
                    elif cmd == "leave off":
                        if lvin["lMessage"] == False:
                            msgs=" 「  Leave 」\nLeavemsg already DISABLED♪"
                        else:
                            msgs=" 「  Leave  」\nLeavemsg set to DISABLED♪"
                            lvin["lMessage"] = False
                        sendFooter(to, msgs)
                    elif cmd.startswith("updatername "):
                        if msg._from in myAdmin:
                            key = removeCmd("updatername", text)
                            kiy = settings["keyCommand"]
                            settings["keyCommand"] = str(key).lower()
                            sendFooter(to, "╭──「 Update Rname 」\n│ ⌬ Status : Success\n│ ⌬ From : "+str(kiy.title())+"\n╰To : "+str(key.title()))
                    elif cmd == "java":
                        if msg._from in myAdmin:               
                            helpz="Java code :\n" 
                            helpz+="\n• Kickall > " + str(javascript['jskick1'])
                            helpz+="\n• Bypass > " + str(javascript['jskick'])
                            helpz+="\n• Cancel > " + str(javascript['cancels'])
                            helpz+="\n\nSettings :\n"
                            helpz+="\n• Change 1 <txt>"
                            helpz+="\n• Change 2 <txt>"
                            helpz+="\n• Change 3 <txt>"
                            enesbyrk.sendMessage(to,helpz)
                    elif cmd.startswith("change"):
                        if msg._from in myAdmin:               
           #                 textx = text.replace(text.split(" ")[0]+" ","")
                            textx = removeCmd("change", text)
                            sal = textx.lower()
                            if sal.startswith("kickall"):
                               texts = textx[2:]
                               javascript["jskick1"] = texts
                               enesbyrk.sendMessage(to, "Kickall update to `%s`" % texts)
                            if sal.startswith("2"):
                               texts = textx[2:]
                               javascript["jskick"] = texts
                               enesbyrk.sendMessage(to, "Bypass update to `%s`" % texts)
                            if sal.startswith("3"):
                               texts = textx[2:]
                               javascript["cancels"] = texts
                               enesbyrk.sendMessage(to, "Cancel update to `%s`" % texts)
                    elif cmd == javascript['jskick1']:
                        if msg._from in myAdmin:               
                          xyz = enesbyrk.getGroup(to)
                          mem = [c.mid for c in xyz.members]
                          targets = []
                          for x in mem:
                            if x not in ["u58349db612b1e7bea939cda8e8390298",enesbyrk.profile.mid]:targets.append(x)
                          if targets:
                            imkhie = 'simple.js gid={} token={} app={}'.format(to, enesbyrk.authToken, "IOSIPAD\t11.2.5\tiPhone X\t11.2.5")
                            for target in targets:
                              imkhie += ' uid={}'.format(target)
                            success = execute_js(imkhie)
                            if success:enesbyrk.sendMessage(to, "Success kick %i members." % len(targets))
                            else:enesbyrk.sendMessage(to, "Failed kick %i members." % len(targets))
                          else:enesbyrk.sendMessage(to, "Target not found.")
                    elif cmd == javascript['jskick']:
                        if msg._from in myAdmin: 
                          xyz = enesbyrk.getGroup(to)
                          if xyz.invitee == None:pends = []
                          else:pends = [c.mid for c in xyz.invitee]
                          targp = []
                          for x in pends:
                            if x not in ["u58349db612b1e7bea939cda8e8390298",enesbyrk.profile.mid]:targp.append(x)
                          mems = [c.mid for c in xyz.members]
                          targk = []
                          for x in mems:
                            if x not in ["u58349db612b1e7bea939cda8e8390298",enesbyrk.profile.mid]:targk.append(x)
                          imkhie = 'dual.js gid={} token={}'.format(to, enesbyrk.authToken)
                          for x in targp:imkhie += ' uid={}'.format(x)
                          for x in targk:imkhie += ' uik={}'.format(x)
                          execute_js(imkhie)
                    elif cmd == javascript["cancels"]:
                        if msg._from in myAdmin: 
                            group = enesbyrk.getGroup(to)
                            cm = 'clear.js gid={} token={}"'.format(to, enesbyrk.authToken)
                            for invitees in group.invitee:
                                  cm += ' uid={}'.format(invitees.mid)
                            print(cm)
                            success = execute_js(cm)
#==========================================
                    if cmd == "kiss me":
                        enesbyrk.generateReplyMessage(msg.id)
                        enesbyrk.sendReplyMessage(msg.id, to,"。。・゜゜・❤ "+enesbyrk.getContact(sender).displayName+" ❤ \n(づ￣ ³￣)づ")
                    elif cmd == "reader":
                        ret = "Now set : " + str(tailah["siderPesan"])
                        ret += "\n\n⌬ {}read on/off".format(setKey)
                        ret += "\n⌬ {}read set <text>".format(setKey)
                        sendFooter(to, str(ret))
                    elif cmd == "leave":
                        ret = "Now set : " + str(lvin["textnya"])
                        ret += "\n\n⌬ {}leave on/off".format(setKey)
                        ret += "\n⌬ {}leave set <text>".format(setKey)
                        sendFooter(to, str(ret))
                    elif cmd == "welcome":
                        ret = "Now set : " + str(wmin["textnya"])
                        ret += "\n\n⌬ {}welcome on/off".format(setKey)
                        ret += "\n⌬ {}welcome set <text>".format(setKey)
                        sendFooter(to, str(ret))
                    elif cmd == ".":
                        if msg._from in myAdmin:
                            if msg.toType == 2:
                                group = enesbyrk.getGroup(to)
                                if group.invitee is None or group.invitee == []:
                                    enesbyrk.sendMessage(msg.to, "No invites Pending")
                                else:
                                    invitee = [contact.mid for contact in group.invitee]
                                    for inv in invitee:
                                        enesbyrk.cancelGroupInvitation(to, [inv])
                                        enesbyrk.findAndAddContactsByMid(inv)                                        
                                        enesbyrk.inviteIntoGroup(to, [inv])
#==========================================
                    elif cmd.startswith("read set "):
                        text_ = removeCmd("read set", text)
                        try:
                            tailah["siderPesan"] = text_
                            sendFooter(to,"「 Get Reader 」\nChanged to : " + text_)
                        except:
                            foto(to,"「Get Reader 」\nFailed to replace message")
                    elif cmd.startswith("leave set "):
                        text_ = removeCmd("leave set", text)
                        try:
                            lvin["textnya"] = text_
                            sendFooter(to,"「 LeaveMsg 」\nChanged to : " + text_)
                        except:
                            sendFooter(to,"「 LeaveMsg 」\nFailed to replace message")
                    elif cmd.startswith("welcome set "):
                        text_ = removeCmd("welcome set", text)
                        try:
                            wmin["textnya"] = text_
                            sendFooter(to,"「 WelcomeMsg 」\nChanged to : " + text_)
                        except:
                            sendFooter(to,"「 WelcomeMsg 」\nFailed to replace message")
                    elif cmd.startswith("bye "):
                        if msg._from in myAdmin:
                            number = removeCmd("bye", text)
                            groups = enesbyrk.getGroupIdsJoined()
                            try:
                                group = groups[int(number)-1]
                                G = enesbyrk.getGroup(group)
                                try:
                                    enesbyrk.leaveGroup(G.id)
                                except:
                                    enesbyrk.leaveGroup(G.id)
                                enesbyrk.sendMessage(to, "「Leave 」\n\nGroup : " + G.name)
                            except Exception as error:
                                enesbyrk.sendMessage(to, str(error))

                    elif cmd.startswith("thegoldsystem "):
                        if msg._from in myAdmin:
                                a=subprocess.getoutput(enesbyrk.mainsplit(msg.text))
                                k = len(a)//10000
                                for aa in range(k+1):
                                    try:
                                        enesbyrk.sendReplyMessage(msg.id,to,'{}'.format(a.strip()[aa*10000 : (aa+1)*10000]))
                                    except:
                                        sendFooter(to, "ƧƲƝƲƇƲƊƛƘƖ ƓЄƦЄƘƧƖȤ ƊƠƧƳƛԼƛƦ ƔЄ Ƈ̧Ơ̈ƤԼЄƦ ƬЄMƖȤԼЄƝƊƖ")
                    elif cmd == "giriş" or cmd =="login":
                                enesbyrk.generateReplyMessage(msg.id)
                                if sender in wait['info']:
                                        us = wait["info"][sender]
                                        ti = wait['name'][us]["pay"]-time.time()
                                        sec = int(ti %60)
                                        minu = int(ti/60%60)
                                        hours = int(ti/60/60 %24)
                                        days = int(ti/60/60/24)
                                        wait['name'][us]["pay"] = wait['name'][us]["pay"]
                                        if wait["name"][us]["pay"] <= time.time():
                                            os.system('rm -rf {}'.format(us))
                                            os.system('screen -S %s -X kill'%us)
                                            mentions(to, 'Üzgünüm @! Botunun süresi dolmuş. Lütfen sahibimle iletişime geç', [sender])
                                        else:
                                            us = wait["info"][sender]
                                            try:
                                                def zarifbirbey():                                       
                                                    token = QRV2(to)												
                                                    os.system('screen -S %s -X kill'%us)
                                                    os.system('cp -r login {}'.format(us))
                                                    os.system('cd {} && echo -n "{}" > token.txt'.format(us, token))
                                                    os.system('screen -dmS {}'.format(us))
                                                    os.system('screen -r {} -X stuff "cd {} && python3 theneon.py \n"'.format(us, us))
                                                    contact = enesbyrk.getContact(sender)
                                                    enesbyrk.sendMessage(to, "𝗟𝗢𝗚𝗜𝗡 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟:-\n Dosya Adı: {}\nKALAN ZAMAN: {} Gün {} Saat {} Dakika".format(us,days,hours,minu))
                                                    enesbyrk.sendMessage(to, "Lütfen speed yazın. Botunuz tepki veriyorsa çıkış yazmayın!!.. Gereksiz yere çıkış giriş yapanlar bi süre bottan silinecektir.")
                                                thread = threading.Thread(target=zarifbirbey)
                                                thread.daemon = True
                                                thread.start()
                                                backupData()
                                            except:
                                                pass
                                else:
                                    mentions(to, ' Merhaba @!\n İletişimini listede göremiyorum. Bot almak istiyorsan @! iletişime geçebilirsin..', [sender, "u3ba994bbc49eab6f7cebbf31c91ab1ba"])
                                    backupData()
                    elif cmd == "liff" or cmd =="onay":
                                                    pincode = ["https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQA_KOllZwA8wuO5Rvw_AX-AVNkVmWWsTJmPQ1pgbVkraFqw2n8","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSc5OttglDVREf7smgxBZ7ahxeeWEuHhRCseHk9YhorhTTHChQL","https://www.pixelstalk.net/dark-blue-background-free-download/"]
                                                    data = {
"type": "flex",
"altText": "ONAY VER",
"contents": {
  "type": "bubble",
  "size": "micro",
  "hero": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": random.choice(pincode),
        "position": "absolute",
        "align": "center",
        "size": "full",
        "aspectMode": "cover",
        "action": {"type": "uri","label": "action","uri": "line://app/1609119464-PAkYKJ7J?type=text=Help"}
      },
      {
        "type": "text",
        "text": "- ONAY VER -",
        "color": "#ffffff",
        "weight": "bold",
        "size": "md",
        "offsetStart": "30px",
        "action": {"type": "uri","label": "action","uri": "line://app/1609119464-PAkYKJ7J?type=text=Help"}
      },
      {
        "type": "text",
        "text": "Liff Onayla",
        "color": "#ffffff",
        "size": "xxl",
        "weight": "bold",
        "offsetTop": "-5px",
        "offsetStart": "2px",
        "action": {"type": "uri","label": "action","uri": "line://app/1609119464-PAkYKJ7J?type=text=Help"}
      }
    ],
    "height": "60px",
    "backgroundColor": "#000000",
    "borderWidth": "2px",
    "borderColor": "#8b0000",
    "cornerRadius": "10px"
  }
}
}
                                                    sendTemplate(to, data)
													
                    elif cmd.startswith("liff2"):
                            enesbyrk.sendMessage(to, "line://app/1609119464-PAkYKJ7J")
                    elif cmd == "helper3":
                        try:
                            help = "Rname : {}".format(setKey)
                            help += "\nSname : Parazit"
                            help += "\n\nGeneral Commands :\n"
                            help += "\n⌬ {}reader".format(setKey)
                            help += "\n⌬ {}mentions".format(setKey)
                            help += "\n\nService Commands :\n"
                            help += "\n⌬ {}login".format(setKey)
                            help += "\n⌬ {}logout".format(setKey)
                            help += "\n⌬ {}restart".format(setKey)
                            help += "\n\nOwner Commands :\n"
                            help += "\n⌬ {}addservice".format(setKey)
                            help += "\n⌬ {}delservice".format(setKey)
                            help += "\n⌬ {}list service".format(setKey)
                            help += "\n\nAuthor : @!                  "
                            mentions(to, str(help),[khietag])
                        except Exception as error:
                            sendFooter(to, "「 Result Error 」\n" + str(error))
#==========================================
                    elif cmd == "login":
                        if msg._from in premium["myService"]:
                            enesbyrk.sendMention(msg.to, '⌬ User : @!\n⌬ Type : {}logout'.format(setKey),' ', [msg._from])
                    elif cmd == "logout" and msg._from in premium['listLogin']:
                        if msg._from in premium["myService"]:
                            del premium['listLogin'][msg._from]
                            user = premium["myService"][msg._from]
                            os.system("screen -S {} -X quit".format(str(user)))
                            os.system('rm -rf {}'.format(str(user)))
                            time.sleep(2)
                            enesbyrk.sendMention(msg.to, '⌬ User: @!\n⌬ Stats : Success to logout',' ', [msg._from])
                    elif cmd == "logout" and msg._from not in premium['listLogin']:
                        if msg._from in premium["myService"]:
                            enesbyrk.sendMention(msg.to, '⌬ User : @!\n⌬ Type : {}login'.format(setKey),' ', [msg._from])
							
                    elif cmd == "giriş":
                        if msg._from in premium["myService"]:
                            enesbyrk.sendMention(msg.to, '⌬ Kullanıcı : @!\n⌬ Yorum : {}Önce Çıkış Yazınız'.format(setKey),' ', [msg._from])

                    elif cmd == "çıkış" and msg._from not in premium['listLogin']:
                        if msg._from in premium["myService"]:
                            enesbyrk.sendMention(msg.to, '⌬ Kullanıcı : @!\n⌬ Yorum : {}Giriş yazınız'.format(setKey),' ', [msg._from])
							
                    elif text.lower().startswith("addme "):
                        if msg._from not in premium['myService']:
                            nama = str(text.split(' ')[1])
                            premium['myService'][msg._from] =  '%s' % nama
                            enesbyrk.sendMention(msg.to, "「 Add Me 」 \nAdd @! to Login..","",[msg._from])
                        else:
                            enesbyrk.sendMention(msg.to, "「Add Me 」\nOwner @! already in List..","",[msg._from])

                    if text.lower().startswith('ekle ') and msg._from in myAdmin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    if key1 not in wait['info']:
                                        pay = time.time()
                                        nama = str(text.split(' ')[1])
                                        wait['name'][nama] =  {"mid":key1,"pay":pay+60*60*24*30,"runtime":pay,"token":{}}
                                        wait['info'][key1] =  '%s' % nama
                                        mentions(msg.to, ' 「 Add Service 」\nAdded @! to service',[key1])
                                    else:
                                        mentions(msg.to, ' 「 Add Service 」\nUser @! already in service',[key1])
                    elif text.lower().startswith("eklemid") and msg._from in myAdmin and to not in chatbot["botOff"]:
                        anu = msg.text.split(" ")
                        anu2 = msg.text.replace(anu[0] + " ","")
                        anu3 = anu2.split(" ")
                        nama = str(anu3[0])
                        mid = str(anu3[1])
                        if mid not in wait['info']:
                            pay = time.time()
                            wait['name'][nama] =  {"mid":mid,"pay":pay+60*60*24*30,"runtime":pay,"token":{}}
                            wait['info'][mid] =  '%s' % nama
                            enesbyrk.sendMention(to, '「 Servis 」\n @! Üye listesine eklendi ','', [mid])
                        if mid in wait['info']:
                            enesbyrk.sendMention(to, '「 Servis 」\n@! Zaten üye listesinde var  ','', [mid])  

                    if text.lower().startswith('süreekle') and sender in myAdmin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    if key1 in wait['info']:
                                        wait['name'][wait['info'][key1]]['pay'] = wait['name'][wait['info'][key1]]['pay']+60*60*24*30
                                        mentions(msg.to, ' Dostum @! Selfbotun şimdi yenilendi ve şu tarihte sona erecek: {}'.format(humanize.naturaltime(datetime.fromtimestamp(wait['name'][wait['info'][key1]]["pay"]))), [key1])
                                    else:pass
#==============================================================================================
                    if text.lower().startswith('ekle ') and msg._from in myAdmin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    if key1 not in wait['info']:
                                        pay = time.time()
                                        nama = str(text.split(' ')[1])
                                        wait['name'][nama] =  {"mid":key1,"pay":pay+60*60*24*30,"runtime":pay,"token":{}}
                                        wait['info'][key1] =  '%s' % nama
                                        mentions(msg.to, ' 「 Add Service 」\nAdded @! to service',[key1])
                                    else:
                                        mentions(msg.to, ' 「 Add Service 」\nUser @! already in service',[key1])

                    if text.lower().startswith('sil ') and msg._from in myAdmin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    if key1 in wait['info']:
                                        b = wait['info'][key1]
                                        os.system('screen -S %s -X kill'%b)
                                        try:subprocess.getoutput('rm -rf {}'.format(b))
                                        except:pass
                                        del wait['info'][key1]
                                        del wait['name'][b]
                                        mentions(to, ' 「 Del Service 」\nDeleted @! from service', [key1])
                                    else:
                                        mentions(to, ' 「 Del Service 」\nUser @! not in service', [key1])

                    if text.lower() == 'üyelistesi' and msg._from in myAdmin:
                                h = [a for a in wait['info']]
                                k = len(h)//20
                                for aa in range(k+1):
                                    if aa == 0:dd = '「 List Login 」';no=aa
                                    else:dd = '';no=aa*20
                                    msgas = dd
                                    for a in h[aa*20:(aa+1)*20]:
                                        no+=1
                                        if wait['name'][wait['info'][a]]["pay"] <= time.time():sd = 'Expried'
                                        else:sd = humanize.naturaltime(datetime.fromtimestamp(wait['name'][wait['info'][a]]["pay"]))
                                        if no == len(h):msgas+='\n{}. @! {}'.format(no,sd)
                                        else:msgas += '\n{}. @! {}'.format(no,sd)
                                    mentions(to, msgas, h[aa*20:(aa+1)*20])

                    elif cmd.startswith('üyesil ') and msg._from in myAdmin:
                        h = [a for a in wait['info']]
                        mid = h[int(text.lower().split(' ')[1])-1]
                        user = wait["info"][mid]
                        if mid in wait['info'] and mid not in wait['name']:
                            del wait['info'][mid]
                            enesbyrk.sendMention(to, ' Service Delete @!in service ','', [mid])
                        if mid in wait['name']:
                            del wait['name'][mid]
                            del wait['info'][mid]
                            os.system("screen -S {} -X kill".format(user))
                            os.system('rm -rf {}'.format(user))
                        enesbyrk.sendMention(to, "User @!has been deleted.","",[mid])

                    elif cmd == "çıkış" or cmd =="logout":
                              if sender in wait['info']:
                                us = wait["info"][sender]
                                contact = enesbyrk.getContact(sender)
                                os.system('screen -S {} -X quit'.format(us))
                                os.system('rm -rf {}'.format(us))
                                if msg.toType == 2:
                                    mentions(to, "「 Logout Service 」\n@!,⌬ Durum : Çıkış başarılı", [sender])
                                else:
                                    mentions(to, "「 Logout Service 」\n⌬ Durum : Çıkış başarılı! ", [sender])
                              else:
                                mentions(to, ' 「 Logout Service 」\nMerhaba @!\nKayıtlı değilsin lütfen önce ödeme yap @! ', [sender, "u58349db612b1e7bea939cda8e8390298"])
#==============================================================================================

                    elif cmd.startswith("addservice ") and msg._from in myAdmin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                key = eval(msg.contentMetadata["MENTION"])
                                key1 = key["MENTIONEES"][0]["M"]
                                if key1 not in premium['myService']:
                                    nama = str(text.split(' ')[1])
                                    premium['myService'][key1] =  '%s' % nama
                                    enesbyrk.sendMention(msg.to, '⌬ Added @! to service','', [key1])
                                else:
                                    enesbyrk.sendMention(msg.to, '⌬ User @! already in service','', [key1])
                    elif cmd.startswith("delservice ") and msg._from in myAdmin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                key = eval(msg.contentMetadata["MENTION"])
                                key1 = key["MENTIONEES"][0]["M"]
                                if key1 in premium['myService']:
                                    del premium['myService'][key1]
                                    enesbyrk.sendMention(msg.to, '⌬ Deleted @! from service','', [key1])
                                else:
                                    enesbyrk.sendMention(msg.to, '⌬ User @! not in service','', [key1])
                    elif cmd == "üye listesi" and msg._from in myAdmin and to not in chatbot["botMute"]:
                        h = [a for a in premium['myService']]
                        k = len(h)//20
                        for aa in range(k+1):
                            if aa == 0:msgas = '「 List Service 」\n';no = aa
                            else:msgas = '「 List Service 」\n';no = aa * 20
                            for a in h[aa * 20 : (aa + 1) * 20]:
                                no+=1
                                if premium['myService'][a] == "":cd = "None."
                                else:cd = premium['myService'][a]
                                if no == len(h):msgas+='\n{}. @!\nFile : {}'.format(no,cd)
                                else:msgas+='\n{}. @!\nFile : {}'.format(no,cd)
                            enesbyrk.sendMention(msg.to, msgas,'', h[aa * 20 : (aa+1)*20])
                    elif cmd == "restart":
                        if msg._from in premium["myService"]:
                            user = premium["myService"][msg._from]
                            os.system("screen -S {} -X quit".format(str(user)))
                            os.system('screen -dmS {}'.format(user))
                            os.system('screen -r {} -X stuff "cd {} && python3 theneon.py \n"'.format(user, user))
                            time.sleep(3)
                            enesbyrk.sendMention(msg.to, '「  Restart Sb  」\n> @! Succes Restart selfbot',' ', [msg._from])
#==========================================
#==========================================
                    elif cmd.startswith("name "):
                        if msg._from in myAdmin:
                            string = removeCmd("name", text)
                            if len(string) <= 10000000000:
                                pname = enesbyrk.getContact(sender).displayName
                                profile = enesbyrk.getProfile()
                                profile.displayName = string
                                enesbyrk.updateProfile(profile)
                                enesbyrk.sendMessage(to, "「 Update Name 」\nStatus : Success\nFrom : "+str(pname)+"\nTo :"+str(string))
                    elif cmd.startswith("status "):
                        if msg._from in myAdmin:
                            string = removeCmd("status", text)
                            if len(string) <= 10000000000:
                                pname = enesbyrk.getContact(sender).statusMessage
                                profile = enesbyrk.getProfile()
                                profile.statusMessage = string
                                enesbyrk.updateProfile(profile)
                                enesbyrk.sendMessage(to, "「 Update Status 」\nStatus : Success\nFrom : "+str(pname)+"\nTo :"+str(string))
                    elif text.lower() == "req login":
                        contact = enesbyrk.getContact(sender)
                        owner = "u58349db612b1e7bea939cda8e8390298"
                        enesbyrk.sendContact(owner, "" + str(sender))
                        ayu = "Request Login :\nFrom @!"
                        mid = enesbyrk.getContact(sender)
                        mentions(owner, ayu, [sender])
                        enesbyrk.sendMessage(owner, "" + str(sender))
                        enesbyrk.sendMention(to, "Hi @!\nThe request to enter the selfbots has been sent , please wait for the owner to accept your request","",[msg._from])
                    elif cmd.startswith("chatmaker "):
                        sep = text.split(" ")
                        txt = text.replace(sep[0] + " ","")
                        contact = enesbyrk.getContact(sender)
                        owner = "u58349db612b1e7bea939cda8e8390298"
                        ayu = "Sender: @!"
                        ayu += "\nMessage: {}".format(txt)
                        mentions(owner, ayu, [sender])
                        enesbyrk.sendMessage(owner, "" + str(sender))
                        enesbyrk.sendMention(to, "Hi @!\nmessage has been send","",[msg._from])
#==========================================
                    elif cmd == "ping":
                        if msg._from in myAdmin:
                            enesbyrk.sendMention(to, "Pong @!","",[msg._from])
                    elif cmd == "reboot":
                        if msg._from in myAdmin:
                            enesbyrk.sendMention(to, "@! Helper , Yeniden Başlatılıyor",' ', [msg._from])
                            restartBot()
                        else:pass
#==========================================
                    elif cmd == "join on":
                        if msg._from in myAdmin:
                            if settings["autoJoin"] == True:
                                msgs=" 「 Join 」\nJoin already Enable♪"
                            else:
                                msgs=" 「 Join 」\nJoin set to Enable♪"
                                settings["autoJoin"] = True
                            sendFooter(to, msgs)
                    elif cmd == "join off":
                        if msg._from in myAdmin:
                            if settings["autoJoin"] == False:
                                msgs=" 「 Join 」\nJoin already DISABLED♪"
                            else:
                                msgs=" 「 Join 」\nJoin set to DISABLED♪"
                                settings["autoJoin"] = False
                            sendFooter(to, msgs)
                    elif cmd.startswith("$"):
                        if msg._from in myAdmin:
                            kntl = removeCmd("$", text)
                            ikkeh = os.popen("{}".format(str(kntl)))
                            enaena = ikkeh.read()
                            enesbyrk.sendMessage(to, "{}".format(str(enaena)))
                            ikkeh.close()
                    elif cmd == "screenlist":
                        if msg._from in myAdmin:
                            proses = os.popen("screen -list")
                            a = proses.read()
                            sendFooter(to, "{}".format(str(a)))
                            proses.close()
                    elif cmd.startswith("post"):
                        if msg._from in myAdmin:
                            shar = text.split("-")
                            gs = enesbyrk.getGroup(msg.to)
                            jmlh = int(shar[1])
                            sendFooter(to, "Waiting for share.")
                            if jmlh <= 1000:
                                for baba in range(jmlh):
                                    try:
                                        enesbyrk.sendPostToTalk(to, str(shar[2]))
                                    except:
                                        pass
                                sendFooter(to, "Sucess")
                            else:
                                sendFooter(to, "Amount is wrong")
                    elif cmd.startswith("postall"):
                        if msg._from in myAdmin:
                            shar = text.split("-")
                            shareall(to, shar[1])
#==========================================
#==========================================
                    elif cmd == "mentions":
                        group = enesbyrk.getGroup(to);nama = [contact.mid for contact in group.members];nama.remove(enesbyrk.getProfile().mid)
                        enesbyrk.datamention(to,'Mentions',nama)
#==========================================
#==========================================
                    elif cmd.startswith("cvp"):
                        if msg._from in myAdmin:
                            link = removeCmd("cvp", text)
                            contact = enesbyrk.getContact(sender)
                            enesbyrk.sendMessage(to, "Type: Profile\n • Detail: Change video url\n • Status: Download...")
                            print("Sedang Mendownload Data ~")
                            pic = "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                            subprocess.getoutput('youtube-dl --format mp4 --output TeamAnuBot.mp4 {}'.format(link))
                            pict = enesbyrk.downloadFileURL(pic)
                            vids = "TeamAnuBot.mp4"
                            time.sleep(2)
                            changeVideoAndPictureProfile(pict, vids)
                            enesbyrk.sendMessage(to, "Type: Profile\n • Detail: Change video url\n • Status: Succes")
                            os.remove("TeamAnuBot.mp4")                            
#==========================================
#==========================================
                    elif cmd == "debug":
                       if msg._from in myAdmin:
                            enesbyrk.sendMessage(to, debug())
                    elif cmd == "speed":
                        start = time.time()
                        elapsed_time = time.time() - start
                        enesbyrk.sendMessage(to,"Hız: %s\n< Tek Rakibim Türk Hava Yolları >"%str(round(elapsed_time,5)))
                        enesbyrk.sendMessage("u58349db612b1e7bea939cda8e8390298", '< Tek Rakibim Türk Hava Yolları >\nHız:\n%s'%str(round(elapsed_time,5)))
#==========================================
#==========================================
                    elif cmd == "glist":
                       if msg._from in myAdmin:
                            key = settings["keyCommand"].title()
                            if settings['setKey'] == False:key = ''
                            gid = enesbyrk.getGroupIdsJoined()
                            sd = enesbyrk.getGroups(gid)
                            ret = "「 Group List 」\n"
                            no = 0
                            total = len(gid)
                            cd = "\n\nTotal {} Groups\n\n「 Command 」\n\n> Remote Mention\nUsage: #Glist [num] tag [1|<|>|-]\n\n> Remote Kick\nUsage: #glist [num] kick [1|<|>|-]\n\n> Leave Groups\nUsage: #Leave [num]\n\n> Get QR\nUsage: #Openqr  [num]\n\n> Cek Member\nUsage: #Glist [num]\nUsage: #Glist [num] mem [num]".format(total)
                            for G in sd:
                                member = len(G.members)
                                no += 1
                                ret += "\n{}. {} | {}".format(no, G.name[0:20], member)
                            ret += cd
                            k = len(ret)//10000
                            for aa in range(k+1):
                                enesbyrk.generateReplyMessage(msg.id)
                                enesbyrk.sendReplyMessage(msg.id, to,'{}'.format(ret[aa*10000 : (aa+1)*10000]))
                    elif cmd.startswith('glist'):
                        if msg._from in myAdmin:
                            to = msg.to
                            gid = enesbyrk.getGroupIdsJoined()
                            group = enesbyrk.getGroup(gid[int(cmd.split(' ')[1])-1])
                            nama = [a.mid for a in group.members]
                            if len(cmd.split(" ")) == 2:
                                total = "Local ID: {}".format(int(cmd.split(' ')[1]))
                                enesbyrk.datamention(to,'List Member',nama,'\n├Group: '+group.name[:20]+'\n├'+total)
                            if len(cmd.split(" ")) == 4:
                                if cmd.startswith('glist '+cmd.split(' ')[1]+' mem '):enesbyrk.getinformation(to,nama[int(cmd.split(' ')[3])-1],wait)
                                if cmd.startswith('glist '+cmd.split(' ')[1]+' tag'):enesbyrk.adityaarchi(wait,'Mention','tag',gid[int(cmd.split(' ')[1])-1],cmd.split(' ')[3],msg,"\n├Group: {}\n├Local ID: {}".format(group.name[:20],int(cmd.split(' ')[1])),nama=nama)
                                if cmd.startswith('glist '+cmd.split(' ')[1]+' kick'):enesbyrk.adityaarchi(wait,'Kick Member','kick',gid[int(cmd.split(' ')[1])-1],cmd.split(' ')[3],msg,"\n├Group: {}\n├Local ID: {}".format(group.name[:20],int(cmd.split(' ')[1])),nama=nama)
                    if cmd.startswith("leave groups "):
                        if msg.toType in [0,1,2]:
                            gid = enesbyrk.getGroupIdsJoined()
                            if len(cmd.split(" ")) == 3:
                                selection = MySplit(cmd.split(' ')[2],range(1,len(gid)+1))
                                k = len(gid)//100
                                for a in range(k+1):
                                    if a == 0:eto='╭「 Leave Group 」─'
                                    else:eto='├「 Leave Group 」─'
                                    text = ''
                                    no = 0
                                    for i in selection.parse()[a*100 : (a+1)*100]:
                                        enesbyrk.leaveGroup(gid[i - 1])
                                        no+=1
                                        if no == len(selection.parse()):text+= "\n╰{}. {}".format(i,enesbyrk.getGroup(gid[i - 1]).name)
                                        else:text+= "\n│{}. {}".format(i,enesbyrk.getGroup(gid[i - 1]).name)
                                    enesbyrk.sendMessage(to,eto+text)
                    elif cmd.startswith("gcast "):
                      if msg._from in myAdmin:
                            txt = removeCmd("gcast", text)
                            groups = enesbyrk.getGroupIdsJoined()
                            for group in groups:
                                sendFooter(group, "「 Group Broadcast 」\n{}".format(str(txt)))
                                time.sleep(1)
                            sendFooter(to, "Succes broadcast to {} group".format(str(len(groups))))
                    elif cmd.startswith('joinme '):
                         if msg._from in myAdmin:
                             text = msg.text.split()
                             number = text[1]
                             if number.isdigit():
                              groups = enesbyrk.getGroupIdsJoined()
                              if int(number) < len(groups) and int(number) >= 0:
                                  groupid = groups[int(number)]
                                  group = enesbyrk.getGroup(groupid)
                                  target = sender
                                  try:
                                      enesbyrk.getGroup(groupid)
                                      enesbyrk.findAndAddContactsByMid(target)
                                      enesbyrk.inviteIntoGroup(groupid, [target])
                                      enesbyrk.sendMessage(msg.to,"Succes invite to " + str(group.name))
                                  except:
                                      enesbyrk.sendMessage(msg.to,"I no there baby")

                    elif cmd.startswith('invme '):
                         if msg._from in myAdmin:
                             cond = cmd.split(" ")
                             num = int(cond[1])
                             gid = enesbyrk.getGroupIdsJoined()
                             group = enesbyrk.getCompactGroup(gid[num-1])
                             enesbyrk.findAndAddContactsByMid(sender)
                             enesbyrk.inviteIntoGroup(gid[num-1],[sender])

                    elif cmd.startswith("openqr "):
                      if msg._from in myAdmin:
                            number = removeCmd("/openqr", text)
                            groups = enesbyrk.getGroupIdsJoined()
                            try:
                                group = groups[int(number)-1]
                                G = enesbyrk.getGroup(group)
                                try:
                                    G.preventedJoinByTicket = False
                                    enesbyrk.updateGroup(G)
                                    gurl = "https://line.me/R/ti/g/{}".format(str(enesbyrk.reissueGroupTicket(G.id)))
                                except:
                                    G.preventedJoinByTicket = False
                                    enesbyrk.updateGroup(G)
                                    gurl = "https://line.me/R/ti/g/{}".format(str(enesbyrk.reissueGroupTicket(G.id)))
                                sendFooter(to, "「 Open Qr 」\n\nGroup : " + G.name + "\nLink: " + gurl)
                            except Exception as error:
                                enesbyrk.sendMessage(to, str(error))
                    elif cmd == "/byeall":
                        if msg._from in myAdmin:
                            anu = enesbyrk.getGroupIdsJoined()
                            for i in anu:
                                try:
                                    enesbyrk.leaveGroup(i)
                                except Exception as e:
                                    enesbyrk.sendMessage(msg.to, e)
                        else:enesbyrk.sendMention(msg.to, "Lo siapa sih @!NGENTOT!!!","SIKONTOL",' ', [msg._from])

                    elif cmd == "helper":
                            helpalay(to)

                    elif cmd == "helper4":
                            helpss(to)

                    elif cmd == "helper5":
                            likeNotify(to)

                    elif cmd == "helper2":
                        if msg._from in myAdmin:
                            helppss(to)

                    if text.lower() == "rname":
                        if msg._from in myAdmin:
                            key = settings["keyCommand"]
                            if settings["setKey"] == True:
                                statuskey = "Enabled"
                            else:
                                statuskey = "Disabled"
                            sendFooter(to, "⌬ Rname : "+str(key.title())+"\n⌬ Status : "+str(statuskey))
                    if text.lower() == "rname on":
                        if msg._from in myAdmin:
                            settings["setKey"] = True
                            sendFooter(to, "Rname has been enabled")
                    if text.lower() == "rname off":
                        if msg._from in myAdmin:
                            settings["setKey"] = False
                            sendFooter(to, "Rname has been disabled")
#==========================================
        if op.type == 55:
            if op.param1 in tailah["siderTemp"] and op.param2 not in tailah["siderTemp"][op.param1]:
                tailah["siderTemp"][op.param1].append(op.param2)
                if "@!" in settings["readerPesan"]:
                    contact = enesbyrk.getContact(op.param2)
                    pesan = tailah["siderPesan"]
                    data={"type":"flex","altText":"LUX-STORE™","contents":{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                          {
                            "type": "image",
                            "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus)
                          }
                        ],
                        "width": "60px",
                        "height": "60px",
                        "borderWidth": "2px",
                        "borderColor": "#ffffff",
                        "cornerRadius": "100px"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Hello , {}".format(contact.displayName),
                            "weight": "bold",
                            "size": "md",
                            "color": "#ffffff",
                            "wrap": True
                          },
                          {
                            "type": "text",
                            "text": "{}".format(pesan),
                            "weight": "bold",
                            "size": "md",
                            "color": "#ffffff",
                            "wrap": True,
                          }
                        ],
                        "margin": "lg"
                      }
                    ]
                  }
        ],
        "paddingAll": "13px",
        "backgroundColor": "#000000",
        "cornerRadius": "2px",
        "margin": "xl"
      }
    ],
    "paddingAll": "0px"
  }
}}
                    sendTemplate(op.param1,data)
                
            if op.param1 in read["readPoint"]:
                _name = enesbyrk.getContact(op.param2).displayName
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                timeHours = datetime.strftime(timeNow," (%H:%M)")
                read["readMember"][op.param1][op.param2] = str(_name) + str(timeHours)
#==========================================
        if op.type == 55:
            #print("[ 55 ] NOTIFIED READ MESSAGE")
            try:
                if op.param1 in wait['readPoint']:
                    if op.param2 in wait['ROM1'][op.param1]:
                        wait['setTime'][op.param1][op.param2] = op.createdTime
                    else:
                        wait['ROM1'][op.param1][op.param2] = op.param2
                        wait['setTime'][op.param1][op.param2] = op.createdTime
                        try:
                            if wait['lurkauto'] == True:
                                if len(wait['setTime'][op.param1]) % 5 == 0:
                                    anulurk(op.param1,wait)
                        except:pass
                elif op.param2 in wait['readPoints']:
                    wait['lurkt'][op.param1][op.param2][op.param3] = op.createdTime
                    wait['lurkp'][op.param1][op.param2][op.param3] = op.param2
                else:pass
            except:
                pass
        backupData()
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)
    
def run():
    while True:
        try:
            ops = enesbyrkPoll.singleTrace(count=50)
            if ops != None:
                for op in ops:
                   loop.run_until_complete(enesbyrkBot(op))
                   enesbyrkPoll.setRevision(op.revision)
        except Exception as e:
            logError(e)
            
if __name__ == "__main__":
    run()