---
uid: "404233"
title: Execute CRUD Operations for Non-Persistent Objects
---
# Execute CRUD Operations for Non-Persistent Objects

This topic describes how to implement _Create_, _Read_, _Update_, and _Delete_ operations for Non-Persistent Objects. 

>[!note]
 This option of our Web API Service ships as part of the [DevExpress Universal Subscription](https://www.devexpress.com/subscriptions/universal.xml).

You may need [Non-Persistent Objects](xref:116516) if you develop a project with the help of **XAF**. See our XAF documentation to familiarize yourself with this concept, if necessary. To implement CRUD operations for non-persistent objects in the Web API Service, follow the steps that are described in the following topic: [](xref:115672).

Use the steps below as an implementation guide:

- Declare a Non-Persistent Object
- Create an Endpoint for the New Type
- Enable the Object Space Provider for Non-Persistent Types
- Create a Singleton Service for Data Access
- Implement an Object Space Customizer Service


## Declare a Non-Persistent Object

The following code implements a new `CustomNonPersistentObject` type:

- The `Name` property stores string values. 
- The `DomainComponentAttribute` marks the object as non-persistent.
- The base class - `NonPersistentBaseObject` - implements the key field property.

# [C#](#tab/tabid-csharp2)
 
```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.DC;

[DomainComponent]
public class CustomNonPersistentObject : NonPersistentBaseObject {
    public string Name { get; set; }
}
```
***

## Create an Endpoint for the New Type 

The code in this section creates an endpoint for `CustomNonPersistentObject`. 

In the **Startup.cs** file, add or find the `AddXafWebApi()` method call and use the `BusinessObject()` method to create an endpoint.


# [C#](#tab/tabid-csharp2)
 
```csharp{6}
public class Startup {
    public void ConfigureServices(IServiceCollection services) {
        // ...
        services.AddXafWebApi(builder => {
            builder.ConfigureOptions(options => {
                options.BusinessObject<CustomNonPersistentObject>();
            });
        }, Configuration);
    }
    // ...
}
```
***

You can review the following topic to learn about endpoint creation: [Add CRUD Endpoints and Consume the Web API](xref:403551).

## Enable the Non-Persistent Object Space Provider

The [Template Kit](xref:405447) automatically adds registration code for the Non-Persistent Object Space Provider. Make sure that the following code is present in your Web API Service project's **Startup.cs** file. Add it if needed (in case you didn't use the **Template Ki**). 

**File:** _MySolution.WebApi\Startup.cs_ (standalone),  _MySolution.Blazor.Server\Startup.cs_ (integrated) 

# [C#](#tab/tabid-csharp2)
 
```csharp{3}
builder.ObjectSpaceProviders
    //...
    .AddNonPersistent();
```
***

## Create a Singleton Service for Data Access

The following class will enable data storage and access. The `ObjectCache` property - a `Dictionary` - holds the object list. The constructor initializes this list with a few objects.  


>[!note]
>If you are familiar with Non-Persistent Object management in XAF applications, this step is new for you. You need to implement a storage in this manner because our Web API Service doesn't work with the `ValueManager`. 

# [C#](#tab/tabid-csharp2)
 
```csharp
using DevExpress.ExpressApp;

public class NonPersistentObjectStorageService {
    public Dictionary<Guid, NonPersistentBaseObject> 
      ObjectCache { get; } = new();

    public NonPersistentObjectStorageService() {
        CreateObject<CustomNonPersistentObject>("A");
        CreateObject<CustomNonPersistentObject>("B");
        CreateObject<CustomNonPersistentObject>("C");
    }
    private NonPersistentBaseObject CreateObject<T>(string value) where T : NonPersistentBaseObject, new() {
        T result = new T();
        if(result is CustomNonPersistentObject custom) {
            custom.Name = value;
        }
        ObjectCache.Add(result.Oid, result);
        return result;
    }
}
```
***

Register the class as a singleton service. Add the following line to **Startup.cs**:

# [C#](#tab/tabid-csharp2)
 
```csharp
public void ConfigureServices(IServiceCollection services) {
    services.AddSingleton<NonPersistentObjectStorageService>();
    //...
}
```
***
> [!tip]
> In the Web API Service, you can choose to register the global object storage as a scoped service. The lifetime of such a service depends on whether you host the Web API Service as part of a Blazor Server project or as a standalone ASP.NET Core project. 
>
> - **Integrated (Single Project - Blazor Server Application)** <br/> The service's visibility scope matches the lifetime of the Blazor app's user circuit. The application typically releases a circuit if a user closes the browser tab or window. 
> - **Standalone (Separate Projects)**<br/> The service's visibility scope matches the lifetime of a single request. 
>
> The DevExpress [Template Kit](xref:405447) allows you to select the integration style in the **Blazor / Web API Service Options** section. 
> 
> ![|Integrated or Standalone Web API Service Project](~/images/template-kit/template-kit-web-api-section.png)


## Unit Tests

Follow the steps below to add unit tests for the code that queries Non-Persistent Objects via the Web API Service.

1. If your solution does not have a testing project, add a new **xUnit test project**.
2. Add a reference to the `{SolutionName}.Blazor.Server` project.
3. Add the `Microsoft.AspNetCore.Mvc.Testing` package reference.
4. Add the following test to the test project:


# [C#](#tab/tabid-csharp2)
 
```csharp
using System.Net;
using System.Net.Http.Headers;
using System.Net.Http.Json;
using System.Text;
using System.Text.Json;
using Microsoft.AspNetCore.Mvc.Testing;
using Xunit;

public class CRUDNonPersistentTests : IClassFixture<WebApplicationFactory<MySolution.Blazor.Server.Startup>> {
    readonly string url = $"/api/odata/{typeof(CustomNonPersistentObject).Name}";

    HttpClient httpClient;
    public CRUDNonPersistentTests(WebApplicationFactory<Blazor.Server.Startup> webApplicationFactory) {
        httpClient = webApplicationFactory.CreateClient();
    }

    [Fact]
    public async System.Threading.Tasks.Task Create_Read_Delete() {
        string tokenString = await GetUserTokenAsync("Sam", "", "/api/Authentication/Authenticate");
        var authorizationToken = new AuthenticationHeaderValue("Bearer", tokenString);

        string content = $"{{\"{nameof(CustomNonPersistentObject.Name)}\":'Test Data'}}";
        var httpRequest = new HttpRequestMessage(HttpMethod.Post, url);
        httpRequest.Content = new StringContent(content, Encoding.UTF8, "application/json");
        httpRequest.Headers.Authorization = authorizationToken;
        var response = await httpClient.SendAsync(httpRequest);
        Assert.Equal(HttpStatusCode.Created, response.StatusCode);

        var jsonResult = await response.Content.ReadFromJsonAsync<JsonElement>();
        var newNonPersistentObject = jsonResult.Deserialize(typeof(CustomNonPersistentObject)) as CustomNonPersistentObject;
        ArgumentNullException.ThrowIfNull(newNonPersistentObject);
        var objKey = newNonPersistentObject.Oid;

        try {
            Assert.Equal("Test Data", newNonPersistentObject.Name);

            //Get by key
            var getHttpRequest = new HttpRequestMessage(HttpMethod.Get, $"{url}/{objKey}");
            getHttpRequest.Headers.Authorization = authorizationToken;
            var getResponse = await httpClient.SendAsync(getHttpRequest);
            Assert.Equal(HttpStatusCode.OK, getResponse.StatusCode);

            jsonResult = await getResponse.Content.ReadFromJsonAsync<JsonElement>();
            var loadedObj = jsonResult.Deserialize(typeof(CustomNonPersistentObject)) as CustomNonPersistentObject;
            ArgumentNullException.ThrowIfNull(loadedObj);
            Assert.Equal("Test Data", loadedObj.Name);
        }
        finally {
            //Delete the test object
            var deleteHttpRequest = new HttpRequestMessage(HttpMethod.Delete, $"{url}/{objKey}");
            deleteHttpRequest.Headers.Authorization = authorizationToken;
            var deleteResponse = await httpClient.SendAsync(deleteHttpRequest);
            Assert.Equal(HttpStatusCode.OK, deleteResponse.StatusCode);
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
