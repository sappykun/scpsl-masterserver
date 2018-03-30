var SCPApp = angular.module("SCPApp", []);
    
SCPApp.factory("ServerService", function($http) {
	return {
		getServers: function() {
			return $http.get("http://localhost:5000/api/servers/").then(function(response) {
				return angular.fromJson(response.data);
			});
		}
	}
});

SCPApp.controller('ServerListController', function ($scope, $interval, ServerService) {
	var update = function() {
		ServerService.getServers().then(function(data) {
			$scope.servers = data;
		})
	};
	
	update();
	$interval(update, 5000);
});