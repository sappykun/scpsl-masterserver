from app import db

class ServerInfo(db.Model):

    __tablename__   = 'servers'
    __table_args__  = (db.PrimaryKeyConstraint('ip', 'port', name='_ip_port_pk'),)
    
    ip              = db.Column(db.String(128), nullable=False)
    port            = db.Column(db.Integer, nullable=False)
    
    info                = db.Column(db.String(1024), nullable=True)
    player_count    = db.Column(db.Integer, nullable=False)
    player_total    = db.Column(db.Integer, nullable=False)
    servermod_version   = db.Column(db.String(32), nullable=True)
    pastebin_url        = db.Column(db.String(32), nullable=True)
    game_version        = db.Column(db.String(32), nullable=True)
    
    date_updated    = db.Column(db.DateTime, default=db.func.current_timestamp(),
                                            onupdate=db.func.current_timestamp())
    
    def __getitem__(self, item):
        return getattr(self, item)  
    
    def __setitem__(self, key, value):
        self.__dict__[key] = value
       
    @property
    def serialize(self):
        return {
            "ip": self.ip,
            "port": self.port,
            "info": self.info,
            "player_count": self.player_count,
            "player_total": self.player_total,
            "servermod_version": self.servermod_version,
            "pastebin_url": self.pastebin_url,
            "date_updated": self.date_updated
        }
