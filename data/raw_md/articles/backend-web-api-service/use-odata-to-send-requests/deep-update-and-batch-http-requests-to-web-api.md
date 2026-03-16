---
uid: "405468"
title: 'Deep Update and Batch Operations: HTTP Requests from a .NET Application to the DevExpress Web API Service'
---
# Deep Update and Batch Operations: HTTP Requests from a .NET Application to the DevExpress Web API Service

The XAF Backend Web API Service enables deep insert and update operations using POST, PATCH, and PUT methods. You can create or modify business objects with their referenced objects in a single request. Batch operations allow you to execute multiple changes across different object types in one HTTP request.

Example code in this help topic applies to a project that uses EF Core. If you use XPO for data access, replace `ID` property references with `Oid`.

> [!tip]
> Code samples in this topic are extracted from the **MainDemo.WebAPI.Tests** project installed as part of the XAF package. The default location of the project: _%PUBLIC%\Documents\DevExpress Demos <:xx.x:>\Components\XAF\MainDemo.NET.EFCore\CS\MainDemo.WebAPI.Tests_.

## Authenticate with JSON Web Tokens (JWT)

To obtain the [JWT Authentication](xref:403504) token for data requests, send a request to `api/Authentication/Authenticate` and specify a username and password. The following example uses `Sam` as the username and an empty password.

Note that for patch and post requests, the server returns only the HTTP status code. Add a [Prefer](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-odata/b4768cbf-13d5-40df-bfa3-7d43ef73e882) header to a request and set its value to `return=representation` to include the modified content in the response body.

```csharp
HttpClient httpClient = new() { BaseAddress = new Uri("https://localhost:44319") };
StringContent httpContent = new(@"{ ""userName"": ""Sam"", ""password"": """" }", Encoding.UTF8, "application/json");
var tokenResponse = await httpClient.PostAsync("/api/Authentication/Authenticate", httpContent);

var token = await tokenResponse.Content.ReadAsStringAsync();

httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", token);
httpClient.DefaultRequestHeaders.Add("Accept", "application/json");
httpClient.DefaultRequestHeaders.Add("OData-Version", "4.01");
httpClient.DefaultRequestHeaders.Add("Prefer", "return=representation");
```

> [!NOTE]
> For more information about cookie or JWT authentication in JavaScript instead of .NET, review the following article: [JavaScript — Consume the DevExpress Backend Web API with Svelte (Part 5. Authenticate Users and Protect Data)](https://community.devexpress.com/blogs/news/archive/2023/05/24/javascript-consume-the-devexpress-backend-web-api-with-svelte-part-5-authenticate-users.aspx). See the following code file in the associated GitHub Example: [src/hooks.server.js](https://github.com/oliversturm/demo-dx-webapi-js/blob/stage-5/svelte-frontend/src/hooks.server.js).

## Create a Business Object with a Referenced Object

The following code creates a new `Employee` object with an associated `Task` object in a single request: 

```csharp
StringContent content = new(@"{
    ""FirstName"": ""Mary"",
    ""LastName"":""Gordon"",
    ""Email"":""CRUDTests@example.com"",
    ""Tasks"": [
        { ""Description"":""Foo"",""Subject"":""Bar"" }
    ]
}", Encoding.UTF8, "application/json");

var response = await httpClient.PostAsync("/api/odata/Employee?$expand=Tasks", content);
response.EnsureSuccessStatusCode();
var responseContent = await response.Content.ReadAsStringAsync();
```

> [!spoiler][Display example result][Hide example result]
> ```JSON
{
    "@context": "http://localhost/api/odata/$metadata#Employee(Tasks())/$entity",
    "ID": "b40bcbad-0c66-4688-60c5-08dd895281b7",
    "FullName": "Mary Gordon",
    "FirstName": "Mary",
    "LastName": "Gordon",
    "Email": "CRUDTests@example.com",
    "Tasks": [
        {
        "ID": "5ca52dbf-c812-4e24-b057-08dd895281c3",
            "Subject": "Bar",
            "Description": "Foo",
            "PercentCompleted": 0,
            "Status": "NotStarted",
            "Priority": "Low",
            "ActualWorkHours": 0,
            "EstimatedWorkHours": 0
        }
    ]
}
> ```

## Create a Referenced Object

The code sample in this section performs the following operations in one request:
* Finds an `Employee` object with the specified ID and creates a referenced `Department` object.  
    Note that if `Employee` already has an associated `Department` object, the code updates the existing object. To learn how to create a new object and replace the reference property value, refer to the following section: [Replace a Referenced Object](#replace-a-referenced-object).
* Creates two referenced `Position` objects for the `Department` object.

```csharp
var employee_ID = "b40bcbad-0c66-4688-60c5-08dd895281b7";
// ...
using var createDepartmentResponse = await httpClient.PatchAsync(
    $"/api/odata/Employee/{employee_ID}?$expand=Department($expand=Positions)",
    new StringContent(
        $@"{{
            ""Department"": {{
                ""Title"": ""Logistics"",
                ""DepartmentHead"": {{ ""ID"": ""{employee_ID}"" }},
                ""Positions"": [
                    {{ ""Title"": ""Logistics Head"" }},
                    {{ ""Title"": ""Logistics Head Assistant"" }}
                ]
            }}
        }}", Encoding.UTF8, "application/json"));

createDepartmentResponse.EnsureSuccessStatusCode();
var responseContent = await createDepartmentResponse.Content.ReadAsStringAsync();
```

> [!spoiler][Display example result][Hide example result]
> ```JSON
{
    "@context": "http://localhost/api/odata/$metadata#Employee(Department(Positions()))/$entity",
    "ID": "b40bcbad-0c66-4688-60c5-08dd895281b7",
    "FullName": "Mary Gordon",
    "FirstName": "Mary",
    "LastName": "Gordon",
    "Email": "CRUDTests@example.com",
    "Department": {
        "ID": "2f4c580f-1d17-4be7-bda8-08dd8662f8d7",
        "Title": "Logistics",
        "Positions":[
              {
                "ID":"5561593f-5f55-4f92-9f74-08dd8cb0f592",
                "Title":"Logistics Head"
              },
              {
                "ID":"6afc0a3e-392f-483b-9f75-08dd8cb0f592",
                "Title":"Logistics Head Assistant"
              }
        ]
    }
}
> ```

## Modify a Referenced Object

The following code sample updates the title of the `Department` object associated with the `Employee` object:

```csharp
using var updateDepartmentResponse = await httpClient.PatchAsync(
    $"/api/odata/Employee/b40bcbad-0c66-4688-60c5-08dd895281b7?$expand=Department",
        new StringContent(
        @"{
            ""Department"": {
                ""Title"": ""Logistics And Warehouse""
            }
        }", Encoding.UTF8, "application/json"));

updateDepartmentResponse.EnsureSuccessStatusCode();
var responseContent = await updateDepartmentResponse.Content.ReadAsStringAsync();
```

> [!spoiler][Display example result][Hide example result]
> ```JSON
{
    "@context": "http://localhost/api/odata/$metadata#Employee(Department())/$entity",
    "ID": "b40bcbad-0c66-4688-60c5-08dd895281b7",
    "FullName": "Mary Gordon",
    "FirstName": "Mary",
    "LastName": "Gordon",
    "Email": "CRUDTests@example.com",
    "Department": {
        "ID": "2f4c580f-1d17-4be7-bda8-08dd8662f8d7",
        "Title": "Logistics And Warehouse"
    }
}
> ```

## Replace a Referenced Object

To replace a referenced object, specify the new object ID. The original object remains intact.
    * Set the `ID` property value to an existing object's ID to reference this object.
    * Set the `ID` property to its default value to create a new referenced object.  
        You can use the [default(T)](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/default) expression to get a type's default value. For @System.Int32, this default is `0`, and for @System.Guid, it is represented by the [Guid.Empty](xref:System.Guid.Empty) field (`00000000-0000-0000-0000-000000000000`). 
    
        You can change the default ID value for an object as follows:

        # [MySolution.WebApi/Startup.cs](#tab/tabid-startup)
        ```csharp
        services.Configure<WebApiOptions>(opts => {
            opts.DeltaHandlerOptions.IsDefaultKeyValue =
                (keyValue, typesInfo, context) => keyValue.Equals(-1);
        });
        ```
        ***

Other specified property values are applied to the newly created or assigned referenced object.

The following code sample finds an `Employee` object by ID and creates a new referenced `Department` object:

```csharp{6}
using var newDepartmentLinkResponse = await httpClient.PatchAsync(
    $"/api/odata/Employee/4011fcb7-d8bf-4c95-2e7a-08dd8661082a?$expand=Department($expand=Positions)",
    new StringContent(
    $@"{{
        ""Department"": {{
            ""ID"": ""{System.Guid.Empty}"",
            ""Title"": ""Sales"",
            ""DepartmentHead"": {{ ""ID"": ""4011fcb7-d8bf-4c95-2e7a-08dd8661082a"" }},
            ""Positions"": [ {{ ""Title"": ""Sales Head Assistant"" }} ]
        }}
    }}", Encoding.UTF8, "application/json"));

newDepartmentLinkResponse.EnsureSuccessStatusCode();
var responseContent = await newDepartmentLinkResponse.Content.ReadAsStringAsync();
```

> [!spoiler][Display example result][Hide example result]
> ```JSON
{
    "@context": "http://localhost/api/odata/$metadata#Employee(Department(Positions()))/$entity",
    "ID": "4011fcb7-d8bf-4c95-2e7a-08dd8661082a",
    "FullName": "Mary Gordon",
    "FirstName": "Mary",
    "LastName": "Gordon",
    "Email": "CRUDTests@example.com",
    "Department": {
        "ID": "4349F735-19B8-4DFE-8C18-88117B855EDD",
        "Title": "Sales",
        "Positions":[
              {
                "ID":"5561593f-5f55-4f92-9f74-08dd8cb0f592",
                "Title":"Sales Head Assistant"
              }
        ]
    }
}
> ```

## Modify a Collection Assigned to an Object

Use the `@delta` annotation to send a list of modifications in a request. The code sample in this section performs the following actions:

* Creates a new task: `New test task 100`
* Links an existing task (`…5450`) to the current employee
* Modifies the task's (`…f585`) `EstimatedWorkHours` value
* Unlinks the task (`…b018`) from the current employee
* Deletes the task (`…d4fa`)

```csharp
using var updateTasksResponse = await httpClient.PatchAsync(
    "/api/odata/Employee",
    new StringContent(
        $@"{{
            ""@context"": ""http://localhost/api/odata/$metadata#Employee/$delta"",
            ""value"": [
                {{
                ""ID"": ""{employeeKey}"",
                ""Tasks@delta"": [
                    {{ 
                        ""Subject"": ""New test task 100""
                    }},
                    {{
                        ""ID"": ""3f5e43dd-7b1a-45b1-ce31-08dd7db05450""
                    }},
                    {{
                        ""ID"": ""e847e4a3-d151-41e2-5a5f-08dd8723f585"",
                        ""EstimatedWorkHours"": 15
                    }},
                    {{
                        ""@removed"": {{ ""reason"": ""changed"" }},
                        ""ID"": ""70461055-5c93-48c8-6dfd-08dd87f5b018""
                    }},
                    {{
                        ""@removed"": {{ ""reason"": ""deleted"" }},
                        ""ID"": ""a74366e4-b391-4e01-3234-08dd87f7d4fa""
                    }}
                ]
            }}
        ]
    }}", Encoding.UTF8, "application/json"));

updateTasksResponse.EnsureSuccessStatusCode();
responseContent = await updateTasksResponse.Content.ReadAsStringAsync();
```

> [!spoiler][Display example result][Hide example result]
> ```JSON
{"@context": "http:localhost/api/odata/$metadata#Employee/$delta",
    "value": [
        {
            "ID": "4011fcb7-d8bf-4c95-2e7a-08dd8661082a",
            "Tasks@delta": [
                {
                    "ID": "13632d9d-9875-411a-dd93-08dd87f9079c",
                    "Subject": "New test task 100"
                },
                {
                    "ID": "3f5e43dd-7b1a-45b1-ce31-08dd7db05450"
                },
                {
                    "ID": "e847e4a3-d151-41e2-5a5f-08dd8723f585",
                    "EstimatedWorkHours": 15
                },
                {
                    "@removed": {
                      "reason": "changed"
                    },
                    "@id": "http:localhost/api/odata/DemoTask(70461055-5c93-48c8-6dfd-08dd87f5b018)",
                    "ID": "70461055-5c93-48c8-6dfd-08dd87f5b018"
                },
                {
                    "@removed": {
                      "reason": "deleted"
                    },
                    "@id": "http:localhost/api/odata/DemoTask(a74366e4-b391-4e01-3234-08dd87f7d4fa)",
                    "ID": "a74366e4-b391-4e01-3234-08dd87f7d4fa"
                }
            ]
        }
    ]
}
> ```


## Modify Several Objects of the Same Type

You can create, update, and delete several objects of the same type in one request. The following code sample creates two `DemoTask` objects:

```csharp
using var createTaskResponse = await httpClient.PatchAsync("/api/odata/DemoTask", 
    new StringContent(
    $@"{{
        ""@context"": ""http://localhost/api/odata/$metadata#DemoTask/$delta"",
        ""value"": [
            {{ ""Subject"": ""Test task 1"" }},
            {{ ""Subject"": ""Test task 2"" }}
        ]
    }}", Encoding.UTF8, "application/json"));

createTaskResponse.EnsureSuccessStatusCode();
var responseContent = await createTaskResponse.Content.ReadAsStringAsync();
```

> [!spoiler][Display example result][Hide example result]
> ```JSON
{
    "@context":"http://localhost/api/odata/$metadata#DemoTask/$delta",
    "value":[
        {
            "ID":"a82866a5-9793-4e4c-a17c-23eb0736c5e7",
            "Subject":"Test task 1"
        },
        {
            "ID":"59b76c2b-0539-48db-b7e5-49563db7a5e5",
            "Subject":"Test task 2"
        }
    ]
}
> ```

## Batch Query

[Batch query](https://learn.microsoft.com/en-us/odata/client/batch-operations#batch-query) allows you to request several objects in a single HTTP request to the service. The following code sample sends two queries in a single HTTP request:

1. The first query obtains an `Employee` object by its `ID`
2. The second query obtains a `Department` object by its `ID` along with its referenced `Position` objects

```csharp
var batchRequestContent = @$"{{
    ""requests"": [
        {{
            ""method"": ""{HttpMethod.Get}"",
            ""url"": ""{$"/api/odata/{typeof(Employee).Name}/e1574d97-fafd-46be-21cd-08dd8d554255"}"",
            ""headers"": {{
            ""content-type"": ""application/json; odata.metadata=minimal; odata.streaming=true"",
            ""odata-version"": ""4.01""
            }},
            ""id"": ""0""
        }},
        {{
            ""method"": ""{HttpMethod.Get}"",
            ""url"": ""{$"/api/odata/{typeof(Department).Name}/c666e9e6-bd06-4b17-04a5-08dd8d554376"}?$expand=Positions"",
            ""headers"": {{
            ""content-type"": ""application/json; odata.metadata=minimal; odata.streaming=true"",
            ""odata-version"": ""4.01""
            }},
            ""id"": ""1""
        }}
    ]
}}";

var httpResponse = await httpClient.PostAsync("/api/odata/$batch", new StringContent(batchRequestContent, Encoding.UTF8, "application/json"));
httpResponse.EnsureSuccessStatusCode();
string responseContent = await httpResponse.Content.ReadAsStringAsync();
```

> [!spoiler][Display example result][Hide example result]
> ```JSON
{"responses":[
    {
        "id":"0",
        "status":200,
        "headers":{"content-type":"application/json; odata.metadata=minimal; odata.streaming=true; charset=utf-8","odata-version":"4.01"},
        "body" :{
            "@context":"http://localhost/api/odata/$metadata#Employee/$entity",
            "ID":"e1574d97-fafd-46be-21cd-08dd8d554255",
            "FullName":"Stefan Johnson",
            "FirstName":"Stefan",
            "LastName":"Johnson",
            "Email":"BatchTests@example.com",
        }
    },
    {
        "id":"1",
        "status":200,
        "headers":{"content-type":"application/json; odata.metadata=minimal; odata.streaming=true; charset=utf-8","odata-version":"4.01"},
        "body" :{
            "@context":"http://localhost/api/odata/$metadata#Department(Positions())/$entity",
            "ID":"c666e9e6-bd06-4b17-04a5-08dd8d554376",
            "Title":"New department",
            "Positions":[
                {
                    "ID":"2462f989-969d-415e-e9ab-08dd8d55437e",
                    "Title":"New position in new department"
                }
            ]
        }
    }
]}
> ```

> [!note]
> * Batch queries are disabled by default. To enable them, refer to the following blog post: [All in One with OData $Batch](https://devblogs.microsoft.com/odata/all-in-one-with-odata-batch/#setting-things-up). You can also review the _Startup.cs_ file in the **MainDemo** application, typically located in _%PUBLIC%\Documents\DevExpress Demos <:xx.x:>\Components\XAF\MainDemo.NET.EFCore\CS_.
> * OData Client for .NET does not support sending both query and modifications in one batch request.

## Batch Modifications

[Batch modifications](https://learn.microsoft.com/en-us/odata/client/batch-operations#batch-modification) allow you to create, update, or delete several objects in a single HTTP request to the service. The following code sample modifies two objects in a single batch request:

1. The first request modifies an `Employee` object: sets the new value for the `FirstName` property and changes the title of the linked `Department` object.
2. The second request modifies a `Department` object: changes the `Office` property value and requests a `Position` collection.

```csharp
var batchRequestContent = @$"{{
    ""requests"": [
        {{
            ""method"": ""{HttpMethod.Patch}"",
            ""url"": ""{$"/api/odata/{typeof(Employee).Name}/{employee.ID}"}"",
            ""headers"": {{
                ""content-type"": ""application/json; odata.metadata=minimal; odata.streaming=true"",
                ""odata-version"": ""4.01"",
                ""Prefer"": ""return=representation""
            }},
            ""id"": ""0"",
            ""body"": {{
                ""FirstName"": ""Stefan"",
                ""Department@delta"": {{
                    ""Title"": ""Department new Title""
                }}
            }}
        }},
        {{
            ""method"": ""{HttpMethod.Patch}"",
            ""url"": ""{$"/api/odata/{typeof(Department).Name}/{department.ID}"}?$expand=Positions"",
            ""headers"": {{
                ""content-type"": ""application/json; odata.metadata=minimal; odata.streaming=true"",
                ""odata-version"": ""4.01"",
                ""Prefer"": ""return=representation""
            }},
            ""id"": ""1"",
            ""body"": {{
                ""Office"": ""New office on the top floor""
            }}
        }}
    ]
}}";

var httpResponse = await httpClient.PostAsync("/api/odata/$batch", new StringContent(batchRequestContent, Encoding.UTF8, "application/json"));
httpResponse.EnsureSuccessStatusCode();
string responseContent = await httpResponse.Content.ReadAsStringAsync();
```

> [!spoiler][Display example result][Hide example result]
> ```JSON
{"responses":[
    {
        "id":"0",
        "status":200,
        "headers":{"content-type":"application/json; odata.metadata=minimal; odata.streaming=true; charset=utf-8","odata-version":"4.01"},
        "body" :{
            "@context":"http://localhost/api/odata/$metadata#Employee/$entity",
            "ID":"4b304322-5e9c-4b59-5196-08dd8cd06915",
            "FullName":"Stefan Johnson",
            "FirstName":"Stefan",
            "LastName":"Johnson",
            "Email":"BatchTests@example.com",
        }
    },
    {
        "id":"1",
        "status":200,
        "headers":{"content-type":"application/json; odata.metadata=minimal; odata.streaming=true; charset=utf-8","odata-version":"4.01"},
        "body" :{
            "@context":"http://localhost/api/odata/$metadata#Department(Positions())/$entity",
            "ID":"a3c6d14a-95ad-4bd9-2786-08dd8cd06a53",
            "Title":"Department new Title",
            "Office":"New office on the top floor",
            "Positions":[
                {
                    "ID":"4b304322-5e9c-4b59-5196-08dd8cd06915",
                    "Title":"New position in new department"
                }
            ]
        }
    }
]}
> ```

> [!note]
> * Batch queries are disabled by default. To enable them, refer to the following blog post: [All in One with OData $Batch](https://devblogs.microsoft.com/odata/all-in-one-with-odata-batch/#setting-things-up). You can also review the _Startup.cs_ file in the **MainDemo** application, typically located in _%PUBLIC%\Documents\DevExpress Demos <:xx.x:>\Components\XAF\MainDemo.NET.EFCore\CS_.
> * OData Client for .NET does not support sending both query and modifications in one batch request.
> * To obtain modified objects in the response, you can specify the `Prefer` header separately for every request (as demonstrated in this example) or globally as described in the following section: [Authenticate with JSON Web Tokens (JWT)](#authenticate-with-json-web-tokens-jwt).
