import re, time, calendar

from flask import jsonify, request
from flask_restful import Resource

from app import db
from app.modules.serverinfo import ServerInfo

class ServerInfoResource(Resource):

    def get(self):
        return jsonify([x.serialize for x in ServerInfo.query.all()])

    def post(self):
        content = request.form.to_dict(flat=True)
        
        if content['update'] == "1":

            print("Received data from {}:{}".format(content['ip'], content['port']))

            content.pop('update')

            if 'passcode' in content:
                content.pop('passcode')

            stuff = content.pop('info').split(':[:BREAK:]:')

            info = stuff[0]
            pastebin_url = stuff[1]
            game_version = stuff[2]

            morestuff = content.pop('players').split('/')
            player_count = morestuff[0]

            try:
                player_total = morestuff[1]
            except:
                player_total = 20
            
            try:
                temp = re.search(r"<size=1>(.*)<\/size>$", info)
                servermod_version = temp.group(1)
                info = re.sub(r"<size=1>(.*)<\/size>$", "", info)
            except AttributeError:
                servermod_version = None

            content['info'] = info
            content["player_count"] = player_count
            content["player_total"] = player_total
            content["pastebin_url"] = pastebin_url
            content["game_version"] = game_version
            content['servermod_version'] = servermod_version
    
            server = ServerInfo.query.get([content["ip"], content["port"]])
             
            if not server:
                server = ServerInfo(**content)
            else:
                server.player_count = content['player_count']
                server.player_total = content['player_total']
                server.info = content['info']
                server.pastebin_url = content["pastebin_url"]
                server.game_version = content["game_version"]
                server.servermod_version = content['servermod_version']
            
            db.session.add(server) 
            db.session.commit()

        return "YES", 200
        
