# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import json, html5lib, re, requests

class Instagram():

    def __init__(self):
        self.session = requests.session()
        self.host    = 'https://www.instagram.com'
        self.api = '?__a=1'
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def InstagramDownload(self, link):
        try:
            aa = self.session.get(link+self.api)
            data = aa.json()
            try:
                bb = data['graphql']['shortcode_media']['video_url']
                type = "video"
            except:
                bb = data['graphql']['shortcode_media']['display_url']
                type = "picture"
            result = {
                'code': 200,
                'result': {
                    'download': bb,
                    'type': type,
                }
            }
            return result
        except:
            return "Not found"
    
    def InstagramProfile(self, username):
        try:
            r = self.session.get(self.host + '/{username}/'.format(username=username))
            soup = BeautifulSoup(r.content, 'html5lib')
            for script in soup.findAll('script', type='text/javascript')[3]:
                js = json.loads(re.search(r'window._sharedData\s*=\s*(\{.+\})\s*;', script).group(1))
                for profile in js['entry_data']['ProfilePage']:
                    profile = profile['graphql']['user']
                    username = profile['username']
                    name = profile['full_name']
                    pict = profile['profile_pic_url_hd']
                    bio = profile['biography']
                    followers = profile['edge_followed_by']['count']
                    following = profile['edge_follow']['count']
                    private = profile['is_private']
                    media = profile['edge_owner_to_timeline_media']['count']
                    result = {
                        'code': 200,
                        'result': {
                            'username': username,
                            'name': name,
                            'pict': pict,
                            'bio': bio,
                            'followers': followers,
                            'following': following,
                            'private': private,
                            'media': media
                        }
                    }
                    return result
        except:
            return "Username not found"

    def InstagramPost(self, username, no):
        try:    
            r = self.session.get(self.host + '/{username}/'.format(username=username))
            data = BeautifulSoup(r.content, 'html5lib')    
            for getInfoInstagram in data.findAll("script", {"type":"text/javascript"})[3]:
                getJsonInstagram = re.search(r'window._sharedData\s*=\s*(\{.+\})\s*;', getInfoInstagram).group(1)
                data = json.loads(getJsonInstagram)
                for instagramProfile in data["entry_data"]["ProfilePage"]:
                    body = instagramProfile["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][int(no)]
                    username = instagramProfile["graphql"]["user"]["username"]
                    caption = body["node"]["edge_media_to_caption"]["edges"][0]["node"]["text"]
                    link = "https://www.instagram.com/p/"+body["node"]["shortcode"]
                    jml_komen = body["node"]["edge_media_to_comment"]["count"]
                    jml_like = body["node"]["edge_media_preview_like"]["count"]
                    sts_komen =body["node"]["comments_disabled"]
                    pict = body["node"]["display_url"]
                    result = {
        	        	"code": 200,
        	        	"result": {
        		            "caption":caption,
        		            "image":pict,
        		            "jml_komen":jml_komen,
        		            "jml_like":jml_like,
        	        	    "link":link,
        		            "komen":sts_komen,
        	        	    "username":username
        		            }
                	}
                    return result
        except:
            r = self.session.get(self.host + '/{username}/'.format(username=username))
            data = BeautifulSoup(r.content, 'html5lib')    
            for getInfoInstagram in data.findAll("script", {"type":"text/javascript"})[3]:
                getJsonInstagram = re.search(r'window._sharedData\s*=\s*(\{.+\})\s*;', getInfoInstagram).group(1)
                data = json.loads(getJsonInstagram)
                for instagramProfile in data["entry_data"]["ProfilePage"]:
                    body = instagramProfile["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][int(no)]
                    username = instagramProfile["graphql"]["user"]["username"]
                    jml_komen = body["node"]["edge_media_to_comment"]["count"]
                    link = "https://www.instagram.com/p/"+body["node"]["shortcode"]
                    jml_like = body["node"]["edge_media_preview_like"]["count"]
                    sts_komen =body["node"]["comments_disabled"]
                    pict = body["node"]["display_url"]
                    result = {
                		"code": 200,
                		"result": {
        	        	    "caption":"no Caption",
        	    	        "image":pict,
        	    	        "jml_komen":jml_komen,
        	    	        "link":link,
        	    	        "jml_like":jml_like,
        	    	        "komen":sts_komen,
        	    	        "username":username
        	    	        }
                	}
                    return result
    
    def InstagramComment(self, link):
        try:
            r = self.session.get('{link}'.format(link=link))
            data = BeautifulSoup(r.content, 'html5lib') 
            dataKomen = []
            for getInfoInstagram in data.findAll("script", {"type":"text/javascript"})[3]:
                getJsonInstagram = re.search(r'window._sharedData\s*=\s*(\{.+\})\s*;', getInfoInstagram).group(1)
                data = json.loads(getJsonInstagram)
                for instagramProfile in data["entry_data"]["PostPage"]:
                    body = instagramProfile["graphql"]["shortcode_media"]["edge_media_to_comment"]["edges"]
                    for komen in body:
                        user = komen["node"]["owner"]["username"]
                        text = komen["node"]["text"]
                        res = user + " : "+ text
                        dataKomen.append(res)
                        result = {
                            "code": 200,
                            "result": {
                                "komen":dataKomen,
                                }
                        }
                        return result
        except:
            error = "No Comment For This Post"
            return error