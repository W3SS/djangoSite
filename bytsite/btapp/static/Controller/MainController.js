var App = angular.module("djngSite.controllers",['ngRoute','ngResource']);

       
App.config(function($httpProvider, $interpolateProvider,$routeProvider, $locationProvider){
  $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
  $interpolateProvider.startSymbol('{$');
  $interpolateProvider.endSymbol('$}');
  $routeProvider
        .when('/', { // If URL is at /, uses template at
            templateUrl: '/static/pages/home.html', // this location
            controller: 'HomeController' // and apply instructions from this controller
         })
         .when("/about",{
             templateUrl : "/static/pages/about.html"   
         })
         .when("/services",{
             templateUrl : "/static/pages/services.html"  
         })
         .when("/products",{
             templateUrl : "/static/pages/products.html"    
         })
         .when("/contact",{
             templateUrl : "/static/pages/contact.html"  
         })
         .when("/news",{
             templateUrl: "/static/pages/news.html"  
         })
        .otherwise({ // Any other URL, take me back to /
            redirectTo: '/'
        });
});

App.controller("MainController",['$scope',function($scope){
   $scope.menu = [
       {id: 1, menuitem: 'Inicio', icon: 'dashboard', path: 'home'},
       {id: 2, menuitem: 'Nosotros', icon: 'account_balance', path: 'about'},
       {id: 3, menuitem: 'Servicios' ,icon: 'contacts', path:'services'},
       {id: 4, menuitem: 'Productos' ,icon: 'perm_phone_msg', path:'products'},
       {id: 5, menuitem: 'Noticias', icon: 'class', path: 'news'},
       {id: 6, menuitem: 'Contacto', icon: 'class', path: 'contact'}
      ];


}]);
App.factory('BannersApi',['$http', function($http){
    return $http.get('/api/banner/')
        .then(function(response) {
                return response.data;
    });
}]);
App.factory('ArticulosApi',['$http', function($http){
    return $http.get('/api/articulo/')
        .then(function(response) {
                return response.data;
    });
}]);

App.controller("HomeController",['$scope','ArticulosApi','BannersApi',function($scope,ArticulosApi, BannersApi){
    ArticulosApi.then(function(data){
     $scope.Articulos = data.objects; 
    });
    BannersApi.then(function(data){
     $scope.Banners = data.objects; 
    });
}]);
