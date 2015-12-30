/**
 * Created by FRAMGIA\nguyen.huy.quyet on 30/12/2015.
 */

var myApp = angular.module('facebook-home', []).config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});

myApp.controller('LoadPostHomeController', function ($scope, $http) {
    $scope.posts = [];
    console.log($scope.username);
    //$http({
    //    method: 'GET',
    //    url: '/someUrl'
    //}).then(function successCallback(response) {
    //    // this callback will be called asynchronously
    //    // when the response is available
    //}, function errorCallback(response) {
    //    // called asynchronously if an error occurs
    //    // or server returns response with an error status.
    //});

});