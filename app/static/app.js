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
	
	var prettify = function(seconds) {
		var days = Math.floor(seconds / 86400);
		var hours = Math.floor(seconds / 3600);
		var minutes = Math.floor(seconds / 60);
		
		if (days) { return days + " days ago"; }
		if (hours) { return hours + " hours ago"; }
		if (minutes) { return minutes + " minutes ago"; }
		return seconds + " seconds ago";
	}
	
	var get_status = function(server) {
		if (server.difference > 60)
			return {'background': "#FFAAAA"}
		else if (server.player_count == server.player_total)
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