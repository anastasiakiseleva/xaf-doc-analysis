---
uid: "404223"
seealso:
- linkType: HRef
  linkId: https://community.devexpress.com/blogs/news/archive/2023/05/04/consume-the-devexpress-backend-web-api-from-javascript-with-svelte-part-4-edit-and-validate.aspx
  altText: Consume the DevExpress Backend Web API from JavaScript with Svelte (Part 4. Edit and Validate Data)
title: 'Validate Data Sent to Web API Endpoints'
owner: Vladimir Abadzhev
---
# Validate Data Sent to Web API Endpoints 

This topic shows how you can validate user input if you use DevExpress Web API Service for data access.

The following technologies enable data validation: 

[XPO](xref:1998) | [EF Core](https://learn.microsoft.com/en-us/ef/)  
:   These ORM tools allow you to define your Business Model together with validation attributes.
[XAF Validation Module](xref:113684)  
:   Allows you to apply 10+ predefined rules or any number of custom [validation rules](xref:113008) to your data objects. Enforces those rules in XAF applications.

Even if you don't use predefined validation attributes in your data model, you can still use **DevExpress Web API Service** to validate user input. You can add custom data validation logic if you extend the basic implementation described in this article. 

>[!note]
 This option of our Web API Service ships as part of the [DevExpress Universal Subscription](https://www.devexpress.com/subscriptions/universal.xml).

## Validation API Availability

If you use DevExpress Web API Service endpoints to manage data and need to enable validation, use a specially designed `IValidator` service available in the following namespace: `DevExpress.Persistent.Validation`.

You can use the following methods to enable the service. 

### Enable the Validation Module in the Template Kit

If you use the [Template Kit](xref:405447) to create your **Backend Web API** project, you can enable the **Validation** module the the **Additional Modules** section. For additional information, refer to the following topic: [Create a Standalone Web API Application](xref:403401).

### Add the Validation Module to a Standalone Web API or XAF Blazor Application

Install the **DevExpress.ExpressApp.Validation.Blazor** NuGet package. 

Register the **Validation** module and required services in *Startup.cs*. Use the Web API or XAF Application builder:

**File:** _MySolution.WebApi\Startup.cs_ (_MySolution.Blazor.Server\Startup.cs_)

# [C# (Standalone WEB API Service)](#tab/tabid-csharp-standalone)

```csharp
services.AddXafWebApi(builder => {
    //..
    builder.Modules
        .AddValidation(options => {
            //...
        })
    //...
}, Configuration);
```

# [C# (XAF Application Builder)](#tab/tabid-csharp-builder)

```csharp
services.AddXaf(Configuration, builder => {
    //..
    builder.Modules
        .AddValidation(options => {
            //...
        })
    //...
}
```
***

## Validation Does Not Run Automatically

For [performance](xref:DevExpress.ExpressApp.Validation.PersistenceValidationController.CustomGetAggregatedObjectsToValidate#remarks) optimization, CRUD endpoints don't initiate data validation: you need to add that functionality.

## Basic Data Validation Implementation

In a most basic scenario, you access your data using CRUD endpoints. When a user changes data, you enforce specified validation attributes in your data model. 

The following example shows how you can enable such functionality. The code implements a custom `IDataService`. This service runs validation before it commits an object space (`IObjectSpace`). 

For details about custom data services, please see the following article: [](xref:403850).


# [C#](#tab/tabid-csharp)
 
```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Core;
using DevExpress.ExpressApp.DC;
using DevExpress.ExpressApp.WebApi.Services;
using DevExpress.Persistent.Validation;
// ...
public class CustomDataService : DataService {
    readonly IValidator validator;
    public CustomDataService(IObjectSpaceFactory objectSpaceFactory,
     ITypesInfo typesInfo, IValidator validator) 
     : base(objectSpaceFactory, typesInfo) {
        this.validator = validator;
    }

    protected override IObjectSpace CreateObjectSpace(Type objectType) {
        IObjectSpace objectSpace = base.CreateObjectSpace(objectType);
        objectSpace.Committing += ObjectSpace_Committing;
        return objectSpace;
    }

    private void ObjectSpace_Committing(object? sender, 
      System.ComponentModel.CancelEventArgs e) {
        IObjectSpace os = (IObjectSpace)sender!;
        var validationResult = validator.RuleSet.ValidateAllTargets(
            os, os.ModifiedObjects, DefaultContexts.Save
        );
        if(validationResult.ValidationOutcome == ValidationOutcome.Error) {
            throw new ValidationException(validationResult);
        }
    }
}
```
***

## Configure the Request Locale

You can use the `HttpRequestMessage` API to change the request locale. The invalid validation results you obtain from the service will use the locale you specified.

# [C#](#tab/tabid-csharp)
 
```csharp
// ...
httpClient.DefaultRequestHeaders.Add("Accept-Language", "de-DE");
// ...
```
***

## Add Unit Tests

### Test Scenario

This example checks validation rules for XAF's standard `ApplicationUser` class. XAF declares this class in all new projects that use the **Security** feature.

The `ApplicationUser` class applies a [`RuleRequiredField`](xref:DevExpress.Persistent.Validation.RuleRequiredFieldAttribute) attribute to the `UserName` property. In other words, you cannot create a new user with an empty name. 

The test tries to create an `ApplicationUser` object with an empty `UserName` property and receives a validation error. 

This example uses the `IDataService` implementation demonstrated above. You can find the same test included in our **MainDemo.EFCore** demo application.

### Step-by-Step Instructions

Follow the steps below to add a test to your solution:

1. If your solution does not include a testing project, add a new **xUnit test project**.
2. Add a reference to the `{SolutionName}.Blazor.Server` project.
3. Add the `Microsoft.AspNetCore.Mvc.Testing` package reference.
4. Add the following test to the xUnit project.

    # [C#](#tab/tabid-csharp5)
     
    ```csharp
    using System.Net;
    using System.Net.Http.Headers;
    using System.Net.Http.Json;
    using System.Text;
    using System.Text.Json;
    using MySolution.Module.BusinessObjects;
    using Microsoft.AspNetCore.Http;
    using Microsoft.AspNetCore.Mvc.Testing;
    using Xunit;

    public class CustomValidationTests_out : IClassFixture<WebApplicationFactory<MySolution.Blazor.Server.Startup>> {
        HttpClient httpClient;
        public CustomValidationTests_out(WebApplicationFactory<MySolution.Blazor.Server.Startup> webApplicationFactory) {
            httpClient = webApplicationFactory.CreateClient();
        }

        [Fact]
        public async System.Threading.Tasks.Task CreateApplicationUser_ValidateUserNameIsNotEmpty() {
            string tokenString = await GetUserTokenAsync("Admin", "", "/api/Authentication/Authenticate");
            var authorizationToken = new AuthenticationHeaderValue("Bearer", tokenString);

            string url = $"/api/odata/{typeof(ApplicationUser).Name}";

            string content = $"{{\"{nameof(ApplicationUser.ChangePasswordOnFirstLogon)}\":true}}";
            var httpRequest = new HttpRequestMessage(HttpMethod.Post, url);

            httpRequest.Content = new StringContent(content, Encoding.UTF8, "application/json");
            httpRequest.Headers.Authorization = authorizationToken;
            var basResponse = await httpClient.SendAsync(httpRequest);

            Assert.False(badResponse.IsSuccessStatusCode);
            string expectedErrorMessage =
                $"Bad Request : Data Validation Error: Please review and correct the data validation error(s) listed below to proceed.{Environment.NewLine}" +
                $" - The user name must not be empty";
            string actualErrorMessage;
            using(var stream = await badResponse.Content.ReadAsStreamAsync()) {
                using(StreamReader reader = new StreamReader(stream)) {
                    actualErrorMessage = badResponse.ReasonPhrase + " : " + reader.ReadToEnd();
                }
            }
            Assert.Equal(expectedErrorMessage, actualErrorMessage);
            Assert.Equal(HttpStatusCode.BadRequest, badResponse.StatusCode);

            //Correct request content
            content = $"{{\"{nameof(ApplicationUser.UserName)}\":\"TestUserName\",\"{nameof(ApplicationUser.ChangePasswordOnFirstLogon)}\":true}}";
            httpRequest = new HttpRequestMessage(HttpMethod.Post, url);
            httpRequest.Content = new StringContent(content, Encoding.UTF8, "application/json");
            httpRequest.Headers.Authorization = authorizationToken;
            var response = await httpClient.SendAsync(httpRequest);
            Assert.Equal(HttpStatusCode.Created, response.StatusCode);

            var jsonResult = await response.Content.ReadFromJsonAsync<JsonElement>();
            var newUser = jsonResult.Deserialize(typeof(ApplicationUser)) as ApplicationUser;
            ArgumentNullException.ThrowIfNull(newUser);
            try {
                Assert.Equal("TestUserName", newUser.UserName);
                Assert.True(newUser.ChangePasswordOnFirstLogon);
            }
            finally {
                //Delete a new user
                httpRequest = new HttpRequestMessage(HttpMethod.Delete, $"/api/odata/{typeof(ApplicationUser).Name}/{newUser.ID}");
                httpRequest.Headers.Authorization = authorizationToken;
                await httpClient.SendAsync(httpRequest);
            }
        }

        async Task<string> GetUserTokenAsync(string userName, string password, string requestPath) {
            var request = new HttpRequestMessage(HttpMethod.Post, requestPath);
            request.Content = new StringContent(
                $"{{ \"userName\": \"{userName}\", \"password\": \"{password}\" }}", Encoding.UTF8, "application/json");

            var httpResponse = await httpClient.SendAsync(request);
            if(!httpResponse.IsSuccessStatusCode) {
                throw new UnauthorizedAccessException($"Authorization request failed! Code {(int)httpResponse.StatusCode}, '{httpResponse.ReasonPhrase}'");
            }
            var tokenString = await httpResponse.Content.ReadAsStringAsync();
            return tokenString;
        }
    }
    ```
    ***