var SCPApp = angular.module("SCPApp", []);
    
SCPApp.factory("ServerService", function($http) {
	return {
		getServers: function() {
			return $http.get("http://memesystem.party:30000/scp/api/servers/").then(function(response) {
				return angular.fromJson(response.data);
			});
		}
	}
});

SCPApp.controller('ServerListController', function ($scope, $interval, ServerService) {
	
	$scope.lessThan = function(prop, val){
	    return function(item){
	      return item[prop] < val;
	    }
	}
	
	var plural = function(n) {
		return (n == 1) ? "" : "s";
	}
	
	var prettify = function(seconds) {
		seconds = Math.max(seconds, 1)
		
		var days = Math.floor(seconds / 86400);
		var hours = Math.floor(seconds / 3600);
		var minutes = Math.floor(seconds / 60);
		
		if (days)    { return days + " day{0} ago".format(plural(days)); }
		if (hours)   { return hours + " hour{0} ago".format(plural(hours)); }
		if (minutes) { return minutes + " minute{0} ago".format(plural(minutes)); }
		return seconds + " second{0} ago".format(plural(seconds)); 
	}
	
	var get_status = function(server) {
		if (server.difference > 60)
			return {'background': "#FFAAAA"}
		else if (server.player_count >= server.player_total)
			return {'background': "#FFFFAA"}
		
		return {}
	}

	var update = function() {
		ServerService.getServers().then(function(data) {
			var servers = data;
			var now = new Date().getTime()/1000;
			
			for (s in servers) {
				servers[s].difference = Math.floor(now - servers[s].date_updated);
				servers[s].difference_pretty = prettify(servers[s].difference);
				servers[s].status = get_status(servers[s]);
			}
			
			$scope.servers = servers;
		})
	};
	
	update();
	$interval(update, 5000);
});