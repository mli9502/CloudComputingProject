/*
 * Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License").
 * You may not use this file except in compliance with the License.
 * A copy of the License is located at
 *
 *  http://aws.amazon.com/apache2.0
 *
 * or in the "license" file accompanying this file. This file is distributed
 * on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
 * express or implied. See the License for the specific language governing
 * permissions and limitations under the License.
 */

var apigClientFactory = {};
apigClientFactory.newClient = function (config) {
    var apigClient = { };
    if(config === undefined) {
        config = {
            accessKey: '',
            secretKey: '',
            sessionToken: '',
            region: '',
            apiKey: undefined,
            defaultContentType: 'application/json',
            defaultAcceptType: 'application/json'
        };
    }
    if(config.accessKey === undefined) {
        config.accessKey = '';
    }
    if(config.secretKey === undefined) {
        config.secretKey = '';
    }
    if(config.apiKey === undefined) {
        config.apiKey = '';
    }
    if(config.sessionToken === undefined) {
        config.sessionToken = '';
    }
    if(config.region === undefined) {
        config.region = 'us-east-1';
    }
    //If defaultContentType is not defined then default to application/json
    if(config.defaultContentType === undefined) {
        config.defaultContentType = 'application/json';
    }
    //If defaultAcceptType is not defined then default to application/json
    if(config.defaultAcceptType === undefined) {
        config.defaultAcceptType = 'application/json';
    }

    
    // extract endpoint and path from url
    var invokeUrl = 'https://8d3b9wyav7.execute-api.us-east-2.amazonaws.com/prod';
    var endpoint = /(^https?:\/\/[^\/]+)/g.exec(invokeUrl)[1];
    var pathComponent = invokeUrl.substring(endpoint.length);

    var sigV4ClientConfig = {
        accessKey: config.accessKey,
        secretKey: config.secretKey,
        sessionToken: config.sessionToken,
        serviceName: 'execute-api',
        region: config.region,
        endpoint: endpoint,
        defaultContentType: config.defaultContentType,
        defaultAcceptType: config.defaultAcceptType
    };

    var authType = 'NONE';
    if (sigV4ClientConfig.accessKey !== undefined && sigV4ClientConfig.accessKey !== '' && sigV4ClientConfig.secretKey !== undefined && sigV4ClientConfig.secretKey !== '') {
        authType = 'AWS_IAM';
    }

    var simpleHttpClientConfig = {
        endpoint: endpoint,
        defaultContentType: config.defaultContentType,
        defaultAcceptType: config.defaultAcceptType
    };

    var apiGatewayClient = apiGateway.core.apiGatewayClientFactory.newClient(simpleHttpClientConfig, sigV4ClientConfig);
    
    
    
    apigClient.bookGetBookDetailsGet = function (params, body, additionalParams) {
        if(additionalParams === undefined) { additionalParams = {}; }
        
        apiGateway.core.utils.assertParametersDefined(params, ['isbn'], ['body']);
        
        var bookGetBookDetailsGetRequest = {
            verb: 'get'.toUpperCase(),
            path: pathComponent + uritemplate('/book/getBookDetails').expand(apiGateway.core.utils.parseParametersToObject(params, [])),
            headers: apiGateway.core.utils.parseParametersToObject(params, []),
            queryParams: apiGateway.core.utils.parseParametersToObject(params, ['isbn']),
            body: body
        };
        
        
        return apiGatewayClient.makeRequest(bookGetBookDetailsGetRequest, authType, additionalParams, config.apiKey);
    };
    
    
    apigClient.bookGetBookDetailsOptions = function (params, body, additionalParams) {
        if(additionalParams === undefined) { additionalParams = {}; }
        
        apiGateway.core.utils.assertParametersDefined(params, [], ['body']);
        
        var bookGetBookDetailsOptionsRequest = {
            verb: 'options'.toUpperCase(),
            path: pathComponent + uritemplate('/book/getBookDetails').expand(apiGateway.core.utils.parseParametersToObject(params, [])),
            headers: apiGateway.core.utils.parseParametersToObject(params, []),
            queryParams: apiGateway.core.utils.parseParametersToObject(params, []),
            body: body
        };
        
        
        return apiGatewayClient.makeRequest(bookGetBookDetailsOptionsRequest, authType, additionalParams, config.apiKey);
    };
    
    
    apigClient.bookRecommendGet = function (params, body, additionalParams) {
        if(additionalParams === undefined) { additionalParams = {}; }
        
        apiGateway.core.utils.assertParametersDefined(params, ['user_id'], ['body']);
        
        var bookRecommendGetRequest = {
            verb: 'get'.toUpperCase(),
            path: pathComponent + uritemplate('/book/recommend').expand(apiGateway.core.utils.parseParametersToObject(params, [])),
            headers: apiGateway.core.utils.parseParametersToObject(params, []),
            queryParams: apiGateway.core.utils.parseParametersToObject(params, ['user_id']),
            body: body
        };
        
        
        return apiGatewayClient.makeRequest(bookRecommendGetRequest, authType, additionalParams, config.apiKey);
    };
    
    
    apigClient.bookSearchGet = function (params, body, additionalParams) {
        if(additionalParams === undefined) { additionalParams = {}; }
        
        apiGateway.core.utils.assertParametersDefined(params, ['publish_year', 'publisher', 'author', 'title', 'isbn'], ['body']);
        
        var bookSearchGetRequest = {
            verb: 'get'.toUpperCase(),
            path: pathComponent + uritemplate('/book/search').expand(apiGateway.core.utils.parseParametersToObject(params, [])),
            headers: apiGateway.core.utils.parseParametersToObject(params, []),
            queryParams: apiGateway.core.utils.parseParametersToObject(params, ['publish_year', 'publisher', 'author', 'title', 'isbn']),
            body: body
        };
        
        
        return apiGatewayClient.makeRequest(bookSearchGetRequest, authType, additionalParams, config.apiKey);
    };
    
    
    apigClient.bookstoreGetStoreDetailGet = function (params, body, additionalParams) {
        if(additionalParams === undefined) { additionalParams = {}; }
        
        apiGateway.core.utils.assertParametersDefined(params, ['place_id'], ['body']);
        
        var bookstoreGetStoreDetailGetRequest = {
            verb: 'get'.toUpperCase(),
            path: pathComponent + uritemplate('/bookstore/getStoreDetail').expand(apiGateway.core.utils.parseParametersToObject(params, [])),
            headers: apiGateway.core.utils.parseParametersToObject(params, []),
            queryParams: apiGateway.core.utils.parseParametersToObject(params, ['place_id']),
            body: body
        };
        
        
        return apiGatewayClient.makeRequest(bookstoreGetStoreDetailGetRequest, authType, additionalParams, config.apiKey);
    };
    
    
    apigClient.bookstoreSearchGet = function (params, body, additionalParams) {
        if(additionalParams === undefined) { additionalParams = {}; }
        
        apiGateway.core.utils.assertParametersDefined(params, ['user_id'], ['body']);
        
        var bookstoreSearchGetRequest = {
            verb: 'get'.toUpperCase(),
            path: pathComponent + uritemplate('/bookstore/search').expand(apiGateway.core.utils.parseParametersToObject(params, [])),
            headers: apiGateway.core.utils.parseParametersToObject(params, []),
            queryParams: apiGateway.core.utils.parseParametersToObject(params, ['user_id']),
            body: body
        };
        
        
        return apiGatewayClient.makeRequest(bookstoreSearchGetRequest, authType, additionalParams, config.apiKey);
    };
    
    
    apigClient.userGetPreviousRatesGet = function (params, body, additionalParams) {
        if(additionalParams === undefined) { additionalParams = {}; }
        
        apiGateway.core.utils.assertParametersDefined(params, ['user_id'], ['body']);
        
        var userGetPreviousRatesGetRequest = {
            verb: 'get'.toUpperCase(),
            path: pathComponent + uritemplate('/user/getPreviousRates').expand(apiGateway.core.utils.parseParametersToObject(params, [])),
            headers: apiGateway.core.utils.parseParametersToObject(params, []),
            queryParams: apiGateway.core.utils.parseParametersToObject(params, ['user_id']),
            body: body
        };
        
        
        return apiGatewayClient.makeRequest(userGetPreviousRatesGetRequest, authType, additionalParams, config.apiKey);
    };
    
    
    apigClient.userGetUserDetailGet = function (params, body, additionalParams) {
        if(additionalParams === undefined) { additionalParams = {}; }
        
        apiGateway.core.utils.assertParametersDefined(params, ['user_id'], ['body']);
        
        var userGetUserDetailGetRequest = {
            verb: 'get'.toUpperCase(),
            path: pathComponent + uritemplate('/user/getUserDetail').expand(apiGateway.core.utils.parseParametersToObject(params, [])),
            headers: apiGateway.core.utils.parseParametersToObject(params, []),
            queryParams: apiGateway.core.utils.parseParametersToObject(params, ['user_id']),
            body: body
        };
        
        
        return apiGatewayClient.makeRequest(userGetUserDetailGetRequest, authType, additionalParams, config.apiKey);
    };
    
    
    apigClient.userRatePost = function (params, body, additionalParams) {
        if(additionalParams === undefined) { additionalParams = {}; }
        
        apiGateway.core.utils.assertParametersDefined(params, ['user_id', 'rate', 'isbn'], ['body']);
        
        var userRatePostRequest = {
            verb: 'post'.toUpperCase(),
            path: pathComponent + uritemplate('/user/rate').expand(apiGateway.core.utils.parseParametersToObject(params, [])),
            headers: apiGateway.core.utils.parseParametersToObject(params, []),
            queryParams: apiGateway.core.utils.parseParametersToObject(params, ['user_id', 'rate', 'isbn']),
            body: body
        };
        
        
        return apiGatewayClient.makeRequest(userRatePostRequest, authType, additionalParams, config.apiKey);
    };
    

    return apigClient;
};
