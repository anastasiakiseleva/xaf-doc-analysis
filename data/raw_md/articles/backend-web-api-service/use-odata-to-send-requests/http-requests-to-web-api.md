---
uid: "403715"
title: 'Make HTTP Requests to the Web API from .NET Applications'
seealso:
- linkId: "403551"
- linkType: HRef
  linkId: https://community.devexpress.com/blogs/news/archive/2023/04/06/consume-the-devexpress-backend-web-api-from-javascript-with-svelte-part-1.aspx?utm_source=DevExpress&utm_medium=Blog&utm_id=XAF&utm_term=part4&utm_content=oliver-apr2022
  altText: Consume the DevExpress Backend Web API from JavaScript with Svelte (Part 1. Set Up a New Project)
- linkType: HRef
  linkId: https://community.devexpress.com/blogs/news/archive/2023/04/28/consume-the-devexpress-backend-web-api-from-javascript-with-svelte-part-3-sort-and-filter.aspx
  altText: Consume the DevExpress Backend Web API from JavaScript with Svelte (Part 3. Sort and Filter)
- linkType: HRef
  linkId: https://community.devexpress.com/blogs/news/archive/2023/03/29/authorize-ef-core-crud-operations-and-download-reports-in-net-maui-with-odata-web-api.aspx
  altText: Authorize EF Core CRUD Operations and Download Reports in .NET MAUI with OData Web API
- linkType: HRef
  linkId: https://community.devexpress.com/blogs/news/archive/2023/05/01/authorize-ef-core-crud-operations-and-download-reports-in-blazor-webassembly-with-odata-web-api.aspx
  altText: Authorize EF Core CRUD Operations and Download Reports in Blazor WebAssembly with OData Web API
---

# Make HTTP Requests to the Web API from .NET Applications

You can send requests to a [Web API](xref:403394) service from any [.NET application with the HttpClient](https://learn.microsoft.com/en-us/dotnet/csharp/tutorials/console-webapiclient) library. Use the [OData](https://learn.microsoft.com/en-us/odata/overview) syntax to build requests.

> [!NOTE]
>
> If you target .NET for your backend API,  register your [FREE copy of our Web API Service](https://www.devexpress.com/security-api-free). The [Template Kit](xref:405447) scaffolds an OData v4 Web API Service (.NET) with integrated RBAC authorization, and CRUD operations powered by EF Core and our XPO ORM library. Among its numerous capabilities, our built-in Web API Service filters secured server data based on user permissions. [Advanced/enterprise functions](xref:404176) include audit trail, endpoints to download reports, attaching files, validation, obtaining localized captions, and so on.
>
> To manage users, roles, and security permissions at runtime in WinForms and ASP.NET Core Blazor administrative UI/portal, use our Cross-Platform .NET App UI (XAF): [Getting Started Tutorial](xref:402125) | [Demos](https://www.devexpress.com/support/demos/?mtm_campaign=XAF&mtm_kwd=use-odata-to-send-requests#xaf).

See the following topics for more information on [OData](https://learn.microsoft.com/en-us/odata/overview) query options:
* [Query options overview](https://learn.microsoft.com/en-us/odata/concepts/queryoptions-overview)
* [Query options usage](https://learn.microsoft.com/en-us/odata/concepts/queryoptions-usage)

The examples below send requests to the Web API service available at the following address: `https://localhost:44319/`. 

## Authenticate with JSON Web Tokens (JWT)

To obtain the [JWT Authentication](xref:403504) token for further data requests, send a request to the following endpoint: `api/Authentication/Authenticate`. The following example uses "Sam" as a user name and an empty password:


# [C#](#tab/tabid-csharp)
  
```csharp
using System;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading.Tasks;

namespace ConsoleApp1 {
    class Program {
        static async Task Main(string[] args) {
            HttpClient httpClient = new HttpClient();

            // Obtain a JWT token.
            StringContent httpContent = new StringContent(@"{ ""userName"": ""Sam"", ""password"": """" }", Encoding.UTF8, "application/json");
            var response = await httpClient.PostAsync("https://localhost:44319/api/Authentication/Authenticate", httpContent);

            // Save the token for further requests.
            var token = await response.Content.ReadAsStringAsync();

            // Set the authentication header. 
            httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", token);
        }
    }
}
```
***

> [!NOTE]
> For more information about cookie or JWT authentication in JavaScript instead of .NET, review the [JavaScript — Consume the DevExpress Backend Web API with Svelte (Part 5. Authenticate Users and Protect Data)](https://community.devexpress.com/blogs/news/archive/2023/05/24/javascript-consume-the-devexpress-backend-web-api-with-svelte-part-5-authenticate-users.aspx) article and the corresponding GitHub example (the [src/hooks.server.js](https://github.com/oliversturm/demo-dx-webapi-js/blob/stage-5/svelte-frontend/src/hooks.server.js) file in particular).

## Authenticate with OAuth2

If your Web API Service application uses `OAuth2` authentication, follow the steps below to obtain an access token. The described steps assume that a user, on whose behalf you authenticate in the Web API Service, is already registered in the service's Security System. Refer to the following topic for more information on how to configure OAuth2 on the Web API Service side: [Configure the OAuth2 Azure Authentication for the Web API](xref:403505).

### Register the ITokenAcquisition Service

Add the following lines to your client application's startup code to register the `Microsoft.Identity.Web.ITokenAcquisition` service:

# [C#](#tab/tabid-csharp)

```csharp
builder.services.AddMicrosoftIdentityWebApi(Configuration, configSectionName: "Authentication:AzureAd", jwtBearerScheme: "AzureAd")
    .EnableTokenAcquisitionToCallDownstreamApi()
    .AddInMemoryTokenCaches(); // Add this line to register the `ITokenAcquisition` service
```

***

### Acquire the Access Token

Access the `ITokenAcquisition` service through Dependency Injection or use the application's [`ServiceProvider`](xref:System.IServiceProvider) to resolve it:

# [C# - Dependency Injection](#tab/tabid-csharp-di)

```csharp
private readonly ITokenAcquisition _tokenAcquisition;

public YourContextConstructor(ITokenAcquisition tokenAcquisition {
    _tokenAcquisition = tokenAcquisition;
}
```

# [C# - Service Provider](#tab/tabid-csharp-provider)

```csharp
_tokenAcquisition = application.ServiceProvider.GetRequiredService<ITokenAcquisition>();
```

***

After that, use the `ITokenAcquisition.GetAccessTokenForUserAsync` method to acquire the access token:

# [C#](#tab/tabid-csharp)

```csharp
var scopes = new[] { "scope1", "scope2" }; // Replace with the required scopes
var oAuthToken = await _tokenAcquisition.GetAccessTokenForUserAsync(scopes);
```

***

### Create and Send a Request

Create an [HttpRequestMessage](xref:System.Net.Http.HttpRequestMessage ) instance and assign the obtained access token to the authorization header:

# [C#](#tab/tabid-csharp)

```csharp
string endPointAddress = "https://your-endpoint.com/api/endpoint"; 
using var httpRequestMessage = new HttpRequestMessage(HttpMethod.Get, endPointAddress);
httpRequestMessage.Headers.Authorization = new AuthenticationHeaderValue("Bearer", oAuthToken);

using var responseMessage = await _httpClient.SendAsync(httpRequestMessage);
```

***

## Operate with Business Objects

### Get Business Objects

The following code retrieves the _LastName_ and _Email_ fields of the _Employee_ business object where _FirstName_ equals "Mary":
# [C#](#tab/tabid-csharp)
  
```csharp{21-23}
using System;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading.Tasks;

namespace ConsoleApp1 {
    class Program {
        static async Task Main(string[] args) {
            HttpClient httpClient = new HttpClient();
            
            // Obtain a JWT token. This example uses "Sam" as a user name and an empty password.
            StringContent httpContent = new StringContent(@"{ ""userName"": ""Sam"", ""password"": """" }", Encoding.UTF8, "application/json");
            var response = await httpClient.PostAsync("https://localhost:44319/api/Authentication/Authenticate", httpContent);

            // Save the token for further requests.
            var token = await response.Content.ReadAsStringAsync();

            // Set the authentication header. 
            httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", token);
            
            // Send a request to fetch data.
            string requestAddress = "https://localhost:44319/api/odata/Employee";
            var employees = await httpClient.GetStringAsync($"{requestAddress}?$filter=FirstName eq 'Mary'&$select=LastName,Email");
            Console.WriteLine(employees);
        }
    }
}
```
***

[`HttpClient`]: xref:System.Net.Http.HttpClient
[`StringContent`]: xref:System.Net.Http.StringContent
[`PostAsync`]: xref:System.Net.Http.HttpClient.PostAsync*
[`ReadAsStringAsync`]: xref:System.Net.Http.HttpContent.ReadAsStringAsync*
[`DefaultRequestHeaders`]:xref:System.Net.Http.HttpClient.DefaultRequestHeaders*
[`Authorization`]: xref:System.Net.Http.Headers.HttpRequestHeaders.Authorization*
[`AuthenticationHeaderValue`]: xref:System.Net.Http.Headers.AuthenticationHeaderValue

> [!spoiler][Result]
> # [JSON](#tab/tabid-json)
> ```JSON
{"@odata.context":"https://localhost:44319/api/odata/$metadata#Employee(LastName,Email)",
"value":[{"LastName":"Tellitson",
            "Email":"Mary_Tellitson@example.com"}]}
> ```
> ***

### Create a Business Object

The code below adds a new _Employee_ instance with the _FirstName_ field set to "Mary" and the _LastName_ field set to "Gordon":
# [C#](#tab/tabid-csharp)
 
```csharp{21-23}
using System;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1 {
    class Program {
        static async Task Main(string[] args) {
            HttpClient httpClient = new HttpClient();
            // Obtain a JWT token. This example uses "Sam" as a user name and an empty password.
            StringContent httpContent = new StringContent(@"{ ""userName"": ""Sam"", ""password"": """" }", Encoding.UTF8, "application/json");
            var response = await httpClient.PostAsync("https://localhost:44319/api/Authentication/Authenticate", httpContent);

            // Save the token for further requests.
            var token = await response.Content.ReadAsStringAsync();

            // Set the authentication header. 
            httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", token);
            
            // Pass data to the Web API service. 
            StringContent dataHttpContent = new StringContent(@"{ ""FirstName"": ""Mary"", ""LastName"":""Gordon"" }", Encoding.UTF8, "application/json");
            var dataResponse = await httpClient.PostAsync($"{requestAddress}", dataHttpContent);
            Console.WriteLine(dataResponse.StatusCode);
        }
    }
}
```
***

[`StatusCode`]: xref:System.Net.Http.HttpResponseMessage.StatusCode*

**Result** (the _dataResponse.StatusCode_ value): 201 Created

### Get a Reference Object 

You can use one of the following techniques:

[Technique 1 (Expand Query Parameter)](#technique-1-expand-query-parameter)
:   The [$expand](https://learn.microsoft.com/en-us/odata/webapi/odata-expand) OData query parameter allows you to obtain a reference business object **together with** the main object.

[Technique 2 (Ref Endpoint)](#technique-2-ref-endpoint)
:   The [$ref](https://learn.microsoft.com/en-us/aspnet/web-api/overview/odata-support-in-aspnet-web-api/odata-v4/entity-relations-in-odata-v4#getting-related-entities) endpoint allows you to obtain a reference business object **without** its main object.

[!include[auto-expand-attribute-note](~/templates/auto-expand-attribute-note.md)]

#### Technique 1 (Expand Query Parameter)

The example below uses **$expand** to get an _Employee_ object with its related _Department_ object:

# [C#](#tab/tabid-csharp)
 
```csharp{21-23}
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1 {
    class Program {
        static async Task Main(string[] args) {
            HttpClient httpClient = new HttpClient();
           
            // Obtain a JWT token. This example uses "Sam" as a user name and an empty password.
            StringContent httpContent = new StringContent(@"{ ""userName"": ""Sam"", ""password"": """" }", Encoding.UTF8, "application/json");
            var response = await httpClient.PostAsync("https://localhost:44319/api/Authentication/Authenticate", httpContent);

            // Save the token for further requests.
            var token = await response.Content.ReadAsStringAsync();

            // Set the authentication header. 
            httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", token);

            // Send a request to fetch data.
            string requestAddress = "https://localhost:44319/api/odata/Employee";
            var employees = await httpClient.GetStringAsync($"{requestAddress}?$filter=FirstName eq 'Mary'&$select=LastName,Email&$expand=Department");
            Console.WriteLine(employees);
        }
    }
}
```
***

[`GetStringAsync`]: xref:System.Net.Http.HttpClient.GetStringAsync*
[`Console.WriteLine`]: xref:System.Console.WriteLine*

> [!spoiler][Result]
> # [JSON](#tab/tabid-json)
> ```JSON
{"@odata.context":"https://localhost:44319/api/odata/$metadata#Employee(LastName,Email,Department())",
 "value":[{"LastName":"Tellitson",
           "Email":"Mary_Tellitson@example.com",
           "Department":{
                "Oid":"6eff292f-f871-4237-a22c-8a50aa747ea3",
                "Title":"Development Department",
                "Description":"The Information Technology Department manages the company's information infrastructure and online assets.",
                "Location":"Building 2",
                "Office":"205"}
        }]
}
> ```
> ***

The **$expand** parameter can be applied to more than one level of related business objects. The following example retrieves a data chain that consists of two related business objects:

# [C#](#tab/tabid-csharp)
 
```csharp
// ...
string requestAddress = "https://localhost:44319/api/odata/Department";
var departments = await httpClient.GetStringAsync($"{requestAddress}?$select=Title&$expand=Employees($select=FirstName,LastName;$expand=Tasks($select=Subject))");
// ...
```
***

> [!spoiler][Result]
> # [JSON](#tab/tabid-json)
> ```JSON
{"@odata.context": "https://localhost:44319/api/odata/$metadata#Department(Title,Employees(FirstName,LastName,Tasks(Subject)))",
 "value": [{ "Title": "Human Resources",
             "Employees": [{ "FirstName": "Angela",
                             "LastName": "Gross",
                             "Tasks": [{ "Subject": "Create 2022 R&D Plans"},
                                       { "Subject": "Submit D&B Number to ISP for Credit Approval"},
                                       { "Subject": "Deliver R&D Plans for 2022"}]
                           },
                           { "FirstName": "Barbara",
                             "LastName": "Faircloth",
                             "Tasks": [{ "Subject": "Subject": "Deliver R&D Plans for 2022"},
                                       { "Subject": "Submit D&B Number to ISP for Credit Approval"},
                                       { "Subject": "Create 2022 R&D Plans"}]
                            }]
           },
          { "Title": "Purchasing",
            "Employees": [{ "FirstName": "Ernest",
                            "LastName": "Webb",
                            "Tasks": [{ "Subject": "Submit D&B Number to ISP for Credit Approval"},
                                       { "Subject": "Deliver R&D Plans for 2022"}]
                           },
                           ... 
                         ]
          }]
}
> ```
> ***

The default [max expansion depth](https://learn.microsoft.com/en-us/odata/webapi/odata-expand#expand-depth) equals two. You can change this parameter as described in the following topic: [Change the Expansion Depth for Related Business Objects](xref:403719#change-the-expansion-depth-for-related-business-objects).

#### Technique 2 (Ref Endpoint)

The example below gets the Employee's _Department_ reference object:

# [C#](#tab/tabid-csharp)
 
```csharp{21-25}
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1 {
    class Program {
        static async Task Main(string[] args) {
            HttpClient httpClient = new HttpClient();
           
            // Obtain a JWT token. This example uses "Sam" as a user name and an empty password.
            StringContent httpContent = new StringContent(@"{ ""userName"": ""Sam"", ""password"": """" }", Encoding.UTF8, "application/json");
            var response = await httpClient.PostAsync("https://localhost:44319/api/Authentication/Authenticate", httpContent);

            // Save the token for further requests.
            var token = await response.Content.ReadAsStringAsync();

            // Set the authentication header. 
            httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", token);

            // Send a request to fetch data.
            string requestAddress = "https://localhost:44319/api/odata/Employee/1/Department/$ref";
            // or 
            // string requestAddress = "https://localhost:44319/api/odata/Employee(1)/Department/$ref";
            var department = await httpClient.GetStringAsync(requestAddress);
            Console.WriteLine(department);
        }
    }
}
```
***

> [!spoiler][Result]
> # [JSON](#tab/tabid-json)
> ```JSON
{"@odata.context":"https://localhost:44319/api/odata/$metadata#Department/$entity",
"ID":1,
"Title":"Development Department",
"Office":"205","Location":"Building 2",
"Description":"The Information Technology Department manages the company's information infrastructure and online assets."}
> ```
> ***

### Get an Associated Collection

You can use one of the following techniques:

[Technique 1 (Expand Query Parameter)](#technique-1-expand-query-parameter-1)
:   The [$expand](https://learn.microsoft.com/en-us/odata/webapi/odata-expand) OData query parameter allows you to obtain objects from an associated collection **together with** the main object.

[Technique 2 (Ref Endpoint)](#technique-2-ref-endpoint-1)
:   The [$ref](https://learn.microsoft.com/en-us/aspnet/web-api/overview/odata-support-in-aspnet-web-api/odata-v4/entity-relations-in-odata-v4#getting-related-entities) endpoint allows you to obtain objects from an associated collection **without** its main object.

#### Technique 1 (Expand Query Parameter)

The following example gets _LastName_, _Email_, and the related _Tasks_ collection of the _Employee_ business object where _FirstName_ equals "Mary":

# [C#](#tab/tabid-csharp)
 
```csharp{21-23}
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1 {
    class Program {
        static async Task Main(string[] args) {
            HttpClient httpClient = new HttpClient();

            // Obtain a JWT token. This example uses "Sam" as a user name and an empty password.
            StringContent httpContent = new StringContent(@"{ ""userName"": ""Sam"", ""password"": """" }", Encoding.UTF8, "application/json");
            var response = await httpClient.PostAsync("https://localhost:44319/api/Authentication/Authenticate", httpContent);

            // Save the token for further requests.
            var token = await response.Content.ReadAsStringAsync();

            // Set the authentication header. 
            httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", token);

            // Send a request to fetch data.
            string requestAddress = "https://localhost:44319/api/odata/Employee";
            var employees = await httpClient.GetStringAsync($"{requestAddress}?$filter=FirstName eq 'Mary'&$select=LastName,Email&$expand=Tasks");
            Console.WriteLine(employees);
        }
    }
}
```
***


> [!spoiler][Result]
> # [JSON](#tab/tabid-json)
> ```JSON
{"@odata.context":"https://localhost:44319/api/odata/$metadata#Employee(LastName,Email,Tasks())",
 "value":[{"LastName":"Tellitson",
           "Email":"Mary_Tellitson@example.com",
           "Tasks":[{"Oid":"b958f20a-118d-4af0-b249-94445608549d",
                     "Subject":"2022 Brochure Designs",
                     "DueDate":"2022-01-15T00:00:00+04:00",
                     "StartDate":"0001-01-01T00:00:00Z",
                     "Status":"Deferred",
                     "PercentCompleted":0,
                     "Priority":"Normal"},
                    {"Oid":"7de87fc8-4dc0-4b76-82b3-18dffdc61ba4",
                     "Subject":"Review Benefits",
                     "DueDate":"2021-10-02T00:00:00+04:00",
                     "StartDate":"2021-09-12T00:00:00+04:00",
                     "Status":"Completed",
                     "PercentCompleted":100,
                     "Priority":"Normal"},
                    {"Oid":"67d36cda-a261-489f-afa9-c8ac43e1c2ea",
                     "Subject":"Lunch Potluck",
                     "DueDate":"2021-10-03T00:00:00+04:00",
                     "StartDate":"0001-01-01T00:00:00Z",
                     "Status":"Deferred",
                     "PercentCompleted":0,
                     "Priority":"Low"}
                    ]
        }]
}
> ```
> ***

#### Technique 2 (Ref Endpoint)

The example below gets the Employee's _Tasks_ collection:

# [C#](#tab/tabid-csharp)
```csharp{21-25}
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1 {
    class Program {
        static async Task Main(string[] args) {
            HttpClient httpClient = new HttpClient();
           
            // Obtain a JWT token. This example uses "Sam" as a user name and an empty password.
            StringContent httpContent = new StringContent(@"{ ""userName"": ""Sam"", ""password"": """" }", Encoding.UTF8, "application/json");
            var response = await httpClient.PostAsync("https://localhost:44319/api/Authentication/Authenticate", httpContent);

            // Save the token for further requests.
            var token = await response.Content.ReadAsStringAsync();

            // Set the authentication header. 
            httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", token);

            // Send a request to fetch data.
            string requestAddress = "https://localhost:44319/api/odata/Employee(1)/Tasks/$ref";
            // or 
            // string requestAddress = "https://localhost:44319/api/odata/Employee/1/Tasks/$ref";
            var tasks = await httpClient.GetStringAsync(requestAddress);
            Console.WriteLine(tasks);
        }
    }
}
```
***

> [!spoiler][Result]
> # [JSON](#tab/tabid-json)
> ```JSON
{"@odata.context":"https://localhost:44319/api/odata/$metadata#DemoTask",
"value":[
    {
        "ID":8,
        "Subject":"Approve Overtime Pay",
        "Description":"Brett, the overtime I submitted was not paid and I'm being told it was not approved. I thought you approved this. What is the problem?\r\nBrett Wade: I did approve it. It was an error in payroll. Trying to figure it out.",
        "DueDate":"2022-04-22T00:00:00+04:00",
        "StartDate":"2022-03-28T00:00:00+04:00",
        "PercentCompleted":0,
        "Status":"Completed",
        "Priority":"Normal",
        "ActualWorkHours":15,
        "EstimatedWorkHours":19
    },
    {
        "ID":9,
        "Subject":"Move Inventory to New Warehouse",
        "Description":"Robin, you are point person to get all inventory moved to the new warehouse location. You can hire temp workers if needed.",
        "DueDate":"2022-04-24T00:00:00+04:00",
        "StartDate":null,
        "PercentCompleted":0,
        "Status":"NotStarted",
        "Priority":"Low",
        "ActualWorkHours":0,
        "EstimatedWorkHours":10
    },
    {
        "ID":10,
        "Subject":"Shipping Label Artwork",
        "Description":"Kevin wants new shipping labels and I cannot print them without the artwork from your team. Can you please hurry and send it to me.\r\nMorgan Kennedy: Send me the specs and I will work on it when I can.",
        "DueDate":"2022-04-24T00:00:00+04:00",
        "StartDate":"2022-04-19T00:00:00+04:00",
        "PercentCompleted":0,
        "Status":"InProgress",
        "Priority":"High",
        "ActualWorkHours":19,
        "EstimatedWorkHours":12
    }
]}
> ```
> ***

### Assign an Object to a Reference Property

The example below sets an Employee's _Department_ reference property to a _Department_ object:

#### Technique 1 (In Body)

# [C#](#tab/tabid-csharp)
 
```csharp{2-4}
string requestAddress = "https://localhost:44318/api/odata/Employee/1";
string jsonBody = @"{ ""Department"": ""1""}";
// or
// string jsonBody = @"{ ""Department"": { ""Oid"": ""1"" }}";
StringContent content = new StringContent(jsonBody, Encoding.UTF8, "application/json");
var response = await httpClient.PatchAsync(requestAddress, content);
Console.WriteLine(response);
```
***

**Result** (the _dataResponse.StatusCode_ value): 204 No Content

To clear a Reference property, send a **null** value. The example below assigns **null** to an Employee's _Department_ property:

# [C#](#tab/tabid-csharp)
 
```csharp{2}
string requestAddress = "https://localhost:44318/api/odata/Employee/1";
string jsonBody = @"{ ""Department"": null }";
StringContent content = new StringContent(jsonBody, Encoding.UTF8, "application/json");
var response = await httpClient.PatchAsync(requestAddress, content);
Console.WriteLine(response);
```
***

**Result** (the dataResponse.StatusCode value): 204 No Content

#### Technique 2 (Ref Endpoint)
# [C#](#tab/tabid-csharp)
 
```csharp{2}
string requestAddress = "https://localhost:44319/api/odata/Employee/1/Department/$ref";
string jsonBody = "{\"@odata.id\":\"https://localhost:44319/api/odata/Department/1\"}";
StringContent content = new StringContent(jsonBody, Encoding.UTF8, "application/json");
var response = await httpClient.PutAsync(requestAddress, content);
Console.WriteLine(response);
```
***

**Result** (the _dataResponse.StatusCode_ value): 204 No Content

### Add an Object to a Collection
#### Technique 1 (In Body)

The example below adds a _DemoTask_ object to an Employee's _Tasks_ collection:

# [C#](#tab/tabid-csharp)
 
```csharp{2}
string requestAddress = "https://localhost:44319/api/odata/Employee/1";
string jsonBody = @"{ ""Tasks@delta"": [ { ""Oid"": 1 } ] }";
var response = await httpClient.PatchAsync(requestAddress, content);
Console.WriteLine(response);
```
***

**Result** (the dataResponse.StatusCode value): 204 No Content
#### Technique 2 (Ref Endpoint)

The example below adds a _DemoTask_ object to an Employee's _Tasks_ collection:

# [C#](#tab/tabid-csharp)
 
```csharp{2}
string requestAddress = "https://localhost:44319/api/odata/Employee/1/Tasks/$ref";
string jsonBody = "{\"@odata.id\":\"https://localhost:44319/api/odata/DemoTask(1)\"}";
StringContent content = new StringContent(jsonBody, Encoding.UTF8, "application/json");
var response = await httpClient.PostAsync(requestAddress, content);
Console.WriteLine(response);
```
***

**Result** (the _dataResponse.StatusCode_ value): 204 No Content

### Unlink an Object from a Reference Property

The example below removes the Employee's _Department_ reference property value:

# [C#](#tab/tabid-csharp)
 
```csharp
string requestAddress = @"https://localhost:44319/api/odata/Employee/1/Department/$ref?
                          $id=https://localhost:44319/api/odata/Department/1";
// or 
// string requestAddress = @"https://localhost:44319/api/odata/Employee(1)/Department/$ref?
//                           $id=https://localhost:44319/api/odata/Department(1)";
var response = await httpClient.DeleteAsync(requestAddress);
Console.WriteLine(response)
```
***

**Result** (the _dataResponse.StatusCode_ value): 204 No Content

### Remove an Object from a Collection

The example below removes the _DemoTask_ object from the Employee's _Tasks_ collection:

# [C#](#tab/tabid-csharp)
 
```csharp
string requestAddress = @"https://localhost:44319/api/odata/Employee/1/Tasks/$ref?
                          $id=https://localhost:44319/api/odata/DemoTask/1";
// or 
// string requestAddress = @"https://localhost:44319/api/odata/Employee(1)/Tasks/$ref?
//                           $id=https://localhost:44319/api/odata/DemoTask(1)";
var response = await httpClient.DeleteAsync(requestAddress);
Console.WriteLine(response)
```
***

**Result** (the _dataResponse.StatusCode_ value): 204 No Content

### Modify an Object Assigned to a Reference Property

The example below modifies the _Department_ object assigned to the Employee's _Department_ reference property:

# [C#](#tab/tabid-csharp)
 
```csharp{2}
string requestAddress = "https://localhost:44319/api/odata/Employee/1";
string jsonBody = @"{ ""Department"": { ""Office"":""504""} }";
StringContent content = new StringContent(jsonBody, Encoding.UTF8, "application/json");
var response = await httpClient.PatchAsync(requestAddress, content);
Console.WriteLine(response);
```
***

**Result** (the _dataResponse.StatusCode_ value): 204 No Content

### Modify Objects Added to an Associated Collection

The example below modifies the _DemoTask_ object with `Oid`=1 from the Employee's _Tasks_ collection. If the collection does not contain the _DemoTask_ object with this `Oid`, this object is added:

# [C#](#tab/tabid-csharp)
 
```csharp{2}
string requestAddress = "https://localhost:44319/api/odata/Employee/1";
string jsonBody = @"{ ""Tasks@delta"": [{ ""Oid"": ""1"", ""Subject"":""New subject""} ]}";
StringContent content = new StringContent(jsonBody, Encoding.UTF8, "application/json");
var response = await httpClient.PatchAsync(requestAddress, content);
Console.WriteLine(response);
```
***

**Result** (the _dataResponse.StatusCode_ value): 204 No Content

### Call an Object's Action Method

The example below demonstrates how to call an object's method decorated with an [ActionAttribute](xref:DevExpress.Persistent.Base.ActionAttribute). See the [](xref:404488) topic for more information on this feature and how to enable it.

# [C#](#tab/tabid-csharp)
 
```csharp
string requestAddress = "https://localhost:44319/api/odata/Task/b1fea24f-4b60-4cd9-2158-08db8797bd56/Postpone";
string jsonBody = "{\"Days\": 7}";
StringContent content = new StringContent(jsonBody, Encoding.UTF8, "application/json");
var response = await httpClient.PostAsync(requestAddress, content);
Console.WriteLine(response);
```
***

**Result** (the _dataResponse.StatusCode_ value): 200 OK

### Deep Update and Batch Operations

The XAF Backend Web API Service enables deep insert and update operations using POST, PATCH, and PUT methods. You can create or modify business objects along with their referenced objects in a single request. Batch operations allow you to execute multiple unrelated operations across different object types in one HTTP request.

Refer to the following help topic for more details and usage examples: <xref:405468>

## Review GitHub Examples

- [Consume the DevExpress Backend Web API from JavaScript with Svelte Kit](https://github.com/oliversturm/demo-dx-webapi-js/tree/stage-4)
- [How to Create a Web API Service Backend for a .NET MAUI Application](https://go.devexpress.com/XAF_Security_NonXAF_MAUI.aspx)
- [How to Create a Web API Service Backend for a Blazor WebAssembly Application](https://go.devexpress.com/XAF_Security_NonXAF_Blazor_WebAssembly.aspx)
