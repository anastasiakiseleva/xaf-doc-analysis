---
uid: "404207"
title: Manage BLOB Data Through a Web API Controller Endpoint
---
# Manage BLOB Data Through a Web API Controller Endpoint

This topic demonstrates how to use HTTP requests to download, upload, and modify BLOB data (file attachments) in your data model.

The endpoint can work with BLOB data stored in properties of the following types:
- `Byte[]`
- [System.Drawing.Image](xref:System.Drawing.Image)
- [`IFileData`](xref:DevExpress.Persistent.Base.IFileData)
- [`MediaDataObject`](xref:DevExpress.Persistent.BaseImpl.EF.MediaDataObject) (EF Core) / [`MediaDataObject`](xref:DevExpress.Persistent.BaseImpl.MediaDataObject) (XPO)

## Download BLOB Data

XAF implements the `DownloadStream` method to download BLOB data through a Web API controller endpoint:

```csharp
[HttpGet(nameof(DownloadStream))]
public IActionResult DownloadStream(string objectType, string objectKey, string propertyName) { ... }
```

| Method Parameter | Description | 
| ------- | ------- | 
| `objectType` | The business object type name. Use short or full format: `Employee` or `MainDemo.Module.BusinessObjects.Employee`. | 
| `objectKey` | The value that identifies an object/record by its primary key value. | 
| `propertyName` | The name of the property that contains BLOB data. | 

Corresponding Web API Endpoint: `/api/MediaFile/DownloadStream`

The following example demonstrates how to obtain an image contained in the `Photo` property of the `AplicationUser` object:

```csharp
HttpClient httpClient = new HttpClient();

// Set up client Uri.
httpClient.BaseAddress = new Uri("https://localhost:5001/");

string objectTypeName = typeof(ApplicationUser).Name;
string objectKey = "C4890105-CF95-4DFA-8083-08DACE0F086B";
string propertyName = nameof(ApplicationUser.Photo);

// Send request for a photo.
string url = "/api/MediaFile/DownloadStream" + 
  $"?objectType={objectTypeName}" + 
  $"&objectKey={objectKey}" + 
  $"&propertyName={propertyName}";
var response = await httpClient.GetAsync(url);

// Parse the result from HttpResponseMessage.
var photo = await response.Content.ReadAsStringAsync();
```

[!video[Add Custom Web API Endpoints To Check Permissions & Query Media Data in .NET MAUI Apps with EF Core](https://www.youtube.com/watch?v=Pj9CbgzFT-A)]

## Upload BLOB Data

XAF implements the `UploadStream` method to upload BLOB data through a Web API controller endpoint:

```csharp
[HttpPost(nameof(UploadStream))]
public async Task<IActionResult> UploadStream(string objectType, string objectKey, 
    string propertyName, IFormFile file) { ... }
```

| Method Parameter | Description | 
| ------- | ------- | 
| `objectType` | The business object type name. Use short or full format: `Employee` or `MainDemo.Module.BusinessObjects.Employee`. | 
| `objectKey` | The value that identifies an object/record by its primary key value. | 
| `propertyName` | The name of the property where to write BLOB data. | 
| `file` | The file content to upload. | 

Corresponding Web API Endpoint: `/api/MediaFile/UploadStream`

> [!tip]
> The code samples in this section are sourced from the _MainDemo.WebAPI.Tests\MediaFileTests.cs_ file installed as part of the XAF package. The default location of the demo application is _%PUBLIC%\Documents\DevExpress Demos <:xx.x:>\Components\XAF\MainDemo.NET.EFCore\CS_.

### Upload Data to a MediaDataObject

The code below uploads an image to the user's `Photo` property, which uses the `MediaDataObject` type.

```csharp
using var formDataContent = new MultipartFormDataContent();

var fileContent = new ByteArrayContent(Convert.FromBase64String(SamPhoto_String64));
fileContent.Headers.ContentType = new MediaTypeHeaderValue("text/plain");
formDataContent.Add(fileContent, "file", "SamPhoto.jpg");
// Fill parameters
formDataContent.Add(new StringContent(typeof(ApplicationUser).Name), "objectType");
formDataContent.Add(new StringContent(newUser.ID.ToString()), "objectKey");
formDataContent.Add(new StringContent(nameof(ApplicationUser.Photo)), "propertyName");

var request = new HttpRequestMessage(HttpMethod.Post, $"/api/MediaFile/UploadStream");
request.Content = formDataContent;
await WebApiClient.SendAsync(request);
```

### Upload Data to a FileData Object

The following code sample uploads a file to a `Resume` object of the `FileData` type.

```csharp
using var formDataContent = new MultipartFormDataContent();

var fileContent = new ByteArrayContent(Convert.FromBase64String(SamResume_String64));
fileContent.Headers.ContentType = new MediaTypeHeaderValue("text/plain");
formDataContent.Add(fileContent, "file", "SamResume.pdf");
// Fill parameters
formDataContent.Add(new StringContent(typeof(Resume).Name), "objectType");
formDataContent.Add(new StringContent(resume.ID.ToString()), "objectKey");
formDataContent.Add(new StringContent(nameof(Resume.File)), "propertyName");

var request = new HttpRequestMessage(HttpMethod.Post, $"/api/MediaFile/UploadStream");
request.Content = formDataContent;
await WebApiClient.SendAsync(request);
```

## Deep Update Operations

The XAF Backend Web API Service enables deep insert and update operations using POST, PATCH, and PUT methods. You can create or modify media data and its referenced objects in a single request.

> [!tip]
> The code samples in this section are sourced from the _MainDemo.WebAPI.Tests\MediaFile_DeepUpdate_Tests.cs_ file installed as part of the XAF package. The default location of the demo application is _%PUBLIC%\Documents\DevExpress Demos <:xx.x:>\Components\XAF\MainDemo.NET.EFCore\CS_.

### Deep Update MediaDataObject

The following code samples find an application user by the specified ID and updates their photo.

Note that in EF Core, when you write data to the `MediaResource` property, you must specify the `MediaDataKey`. The key is a unique random string that is the media data's identification tag. The `MediaDataKey` is used to create URLs and cache data. If you change `MediaResource` without `MediaDataKey`, a browser may display the wrong media data.

# [EF Core](#tab/tabid-ef-core)
```csharp
using var updateDepartmentResponse = await HttpClient.PatchAsync(
    $"/api/odata/ApplicationUser/{keys[0]}?$expand=Photo($expand=MediaResource)",
    new StringContent(
    $@"{
        "Photo": {
            "MediaDataKey": "{Guid.NewGuid().ToString("N")}",
            "MediaResource": {
                "MediaData": "{Utils.JohnPhoto_String64}"
            }
        }
    }", Encoding.UTF8, "application/json"));

updateDepartmentResponse.EnsureSuccessStatusCode();
var response = await updateDepartmentResponse.Content.ReadAsStringAsync();
```

# [XPO](#tab/tabid-xpo)
```csharp
using var updateDepartmentResponse = await HttpClient.PatchAsync(
    $"/api/odata/ApplicationUser/{keys[0]}?$expand=Photo",
    new StringContent(
    $@"{
        "Photo": {
            "MediaData": "{Utils.JohnPhoto_String64}"
        }
    }", Encoding.UTF8, "application/json"));

updateDepartmentResponse.EnsureSuccessStatusCode();
var response = await updateDepartmentResponse.Content.ReadAsStringAsync();
```
***

> [!spoiler][Display example result][Hide example result]
> ```JSON
{
    "@context":"http://localhost/api/odata/$metadata#ApplicationUser(Photo(MediaResource()))/$entity",
    "ID":"a33f42ca-cb35-4b47-4f18-08dd8f10e013",
    "UserName":"New User",
    "IsActive":true,
    "ChangePasswordOnFirstLogon":false,
    "AccessFailedCount":0,
    "LockoutEnd":"0001-01-01T00:00:00Z",
    "Photo":{
        "ID":"5e52c21a-d52a-4c21-782b-08dd8f10e015",
        "MediaDataKey":"b056c67159a44a20bb859d0df9877fcb",
        "MediaResource":{
            "ID":"5e52c21a-d52a-4c21-782b-08dd8f10e015",
            "MediaData":"{Utils.JohnPhoto_String64}"
        }
    }
}
>```

### Deep Update FileData Object

The following code sample creates a `Resume` object, specifies its content (the `File` property), and assigns it to an `Employee`:

# [EF Core](#tab/tabid-ef-core)
 
```csharp
byte[] bytes = Encoding.UTF8.GetBytes("FILE DATA");
string base64 = Convert.ToBase64String(bytes);

var request = new HttpRequestMessage(HttpMethod.Post, $"/api/odata/Resume");
request.Content = new StringContent($@"{
    "Employee": {
        "ID": "{_newEmployee.ID}"
    },
    "File": {
        "Content": "{base64}",
        "FileName": "DeepCreate_with_FileData_test.txt"
    }
}", Encoding.UTF8, "application/json");

await WebApiClient.SendAsync(request);
```
 
# [XPO](#tab/tabid-xpo)
 
```csharp
byte[] bytes = Encoding.UTF8.GetBytes("FILE DATA");
string base64 = Convert.ToBase64String(bytes);

var request = new HttpRequestMessage(HttpMethod.Post, $"/api/odata/Resume");
request.Content = new StringContent($@"{
    "Employee": {
        "Oid": "{_newEmployee.Oid}"
    },
    "File": {
        "Content": "{base64}",
        "FileName": "DeepCreate_with_FileData_test.txt"
    }
}", Encoding.UTF8, "application/json");

await WebApiClient.SendAsync(request);
```
 
***

## Media File Controller API

The `DownloadStream` and `UploadStream` methods described in this article are available in the `MediaFileController` MVC Controller. This controller is available to you regardless of how you added DevExpress Web API Service to your application. No additional option selection or customization is necessary.

### Media File Controller Customization

The `MediaFileController` class is marked with an [Authorize](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authorization.authorizeattribute) attribute. You can only use the controller with active [authorization](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/introduction). If you need to create an unprotected endpoint, derive your own controller from the ancestor class: `MediaFilesControllerBase`.

`MediaFileController` uses `DevExpress.ExpressApp.AspNetCore.Streaming.IStreamService` to obtain data. Use this service to modify controller implementation (obtain data in a custom manner).

### Add Unit Tests for Media File Controller

Follow the steps below to add unit tests to your application. This example adds tests for code that queries BLOB data (uses `MediaFileController`).

1. If your solution does not include a testing project, add a new **xUnit test project**.
2. Add a reference to the `{SolutionName}.Blazor.Server` project.
3. Add the `Microsoft.AspNetCore.Mvc.Testing` package reference.
4. Add the following test to the test project.

```csharp
using System.Net.Http.Headers;
using System.Text;
using MySolution.Module.BusinessObjects;
using Microsoft.AspNetCore.Mvc.Testing;
using Xunit;

namespace MySolution.WebAPI.Tests {
    public class MediaFileTests : IClassFixture<WebApplicationFactory<MySolution.Blazor.Server.Startup>> {
        HttpClient httpClient;
        public MediaFileTests(WebApplicationFactory<MySolution.Blazor.Server.Startup> webApplicationFactory) {
            httpClient = webApplicationFactory.CreateClient();
        }

        [Fact]
        public async System.Threading.Tasks.Task LoadApplicationUserPhotoTest() {
            string tokenString = await GetUserTokenAsync("Admin", "", "/api/Authentication/Authenticate");
            var authorizationToken = new AuthenticationHeaderValue("Bearer", tokenString);

            string userKey = //"objectKey";

            string url = $"/api/MediaFile/DownloadStream?objectType={typeof(ApplicationUser).Name}&objectKey={userKey}&propertyName={nameof(ApplicationUser.Photo)}";
            var httpRequest = new HttpRequestMessage(HttpMethod.Get, url);
            httpRequest.Headers.Authorization = authorizationToken;
            var response = await httpClient.SendAsync(httpRequest);
            var data = await response.Content.ReadAsStringAsync();
            Assert.True(data.Length > 200);
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
}
```