---
uid: "404176"
seealso:
- linkType: HRef
  linkId: https://community.devexpress.com/blogs/news/archive/2023/03/29/authorize-ef-core-crud-operations-and-download-reports-in-net-maui-with-odata-web-api.aspx
  altText: Authorize EF Core CRUD Operations and Download Reports in .NET MAUI with OData Web API
- linkType: HRef
  linkId: https://community.devexpress.com/blogs/news/archive/2023/05/01/authorize-ef-core-crud-operations-and-download-reports-in-blazor-webassembly-with-odata-web-api.aspx
  altText: Authorize EF Core CRUD Operations and Download Reports in Blazor WebAssembly with OData Web API
- linkType: HRef
  linkId: https://community.devexpress.com/blogs/news/archive/2023/10/17/javascript-consume-the-devexpress-backend-web-api-with-svelte-part-6-reports.aspx
  altText: JavaScript — Consume the DevExpress Backend Web API with Svelte (Part 6. Preview and Download Reports)
title: Obtain a Report from a Web API Controller Endpoint
---
# Obtain a Report from a Web API Controller Endpoint

This topic demonstrates how to obtain a report through HTTP requests to the [DevExpress Web API Service](xref:403394). 

The application must use the following technologies to enable such API requests: 

[DevExpress Reporting](xref:2162)  
:   Creates report definitions.
[XPO](xref:1998) | [EF Core](https://learn.microsoft.com/en-us/ef/)  
:   These ORM tools enable storage for report definitions and bound data.
[XAF Reports Module](xref:113591)  
:   Stores report definitions in a database with the help of specially designed classes: [ReportDataV2](xref:DevExpress.Persistent.BaseImpl.ReportDataV2) (XPO) / [ReportDataV2](xref:DevExpress.Persistent.BaseImpl.EF.ReportDataV2) (EF Core). 

HTTP request parameters allow you to filter or sort data before the API Controller generates the final report document.

>[!note]
 This option of our Web API Service ships as part of the [DevExpress Universal Subscription](https://www.devexpress.com/subscriptions/universal.xml).


## Report Controller Availability

The API described in this article only works if your project contains an MVC Controller that allows you to access reports -- `ReportController`. You can use the following methods to enable this controller in your applications:

### Enable the Module in the Template Kit

If you use the [Template Kit](xref:405447) to create your **Backend Web API** project, you can enable the **Reports** module the the **Additional Modules** section. For additional information, refer to the following topic: [Create a Standalone Web API Application](xref:403401).

### Add the Reports Module to a Standalone Web API or XAF Blazor Application

1. Install the **DevExpress.ExpressApp.ReportsV2.Blazor** NuGet package. 
2. Register the Reports module and required services in *Startup.cs*. Use the Web API builder or XAF Application builder:

    **File:** _MySolution.WebApi\Startup.cs_ (_MySolution.Blazor.Server\Startup.cs_)

    # [C# (Standalone WEB API Service)](#tab/tabid-csharp-standalone)

    ```csharp
    services.AddXafWebApi(builder => {
        //...
        builder.Modules
            .AddReports(options => {
                //...
            })
        //...
    }, Configuration);
    ```

    # [C# (XAF Application Builder)](#tab/tabid-csharp-builder)

    ```csharp
    services.AddXaf(Configuration, builder => {
        //...
        builder.Modules
            .AddReports(options => {
                //...
            })
        //...
    }
    ```
    ***

3. Add an API controller with endpoints to download reports to your existing Blazor application. An example of this controller can be found in our demo application that ships with the XAF installation (_%PUBLIC%\Documents\DevExpress Demos <:xx.x:>\Components\XAF\MainDemo.NET.EFCore\CS\MainDemo.Blazor.Server\API\Reports\ReportController.cs_ by default).

## Report Controller API

The `ReportController` class includes the following methods:

# [C#](#tab/tabid-csharp)
 
```csharp
[HttpGet("DownloadByKey({key})")]
public async Task<object> DownloadByKey(string key,
    [FromQuery] ExportTarget fileType = ExportTarget.Pdf,
    [FromQuery] string criteria = null) {
    //...
}

[HttpGet("DownloadByName({displayName})")]
public async Task<object> DownloadByName(string displayName,
    [FromQuery] ExportTarget fileType = ExportTarget.Pdf,
    [FromQuery] string criteria = null) {
    //...
}
```
***

### Basic Usage Example

This example demonstrates how to obtain a report as a PDF file. The code in this example sends a request to the `Report/DownloadByName` endpoint with the `displayName` parameter.

# [C#](#tab/tabid-csharp)
 
```csharp
HttpClient httpClient = new HttpClient();

// Set up client Uri.
httpClient.BaseAddress = new Uri("https://localhost:5001/");

// Argument for the DownloadByName method.
var displayName = "Employee List Report";

// Send request for a report PDF.
var response = await httpClient.GetAsync(
    $"/api/Report/DownloadByName({displayName})"
);

// Parse the result from HttpResponseMessage.
var report = await response.Content.ReadAsStringAsync();
```
***

### Configure the Request Locale

You can use the `HttpRequestMessage` API to configure the request locale:

# [C#](#tab/tabid-csharp)
 
```csharp
var customRequest = new HttpRequestMessage(HttpMethod.Get, 
    $"/api/Report/DownloadByName({displayName})");

customRequest.Headers.Add("Accept-Language", "en-US");

var response = await httpClient.SendAsync(customRequest);
```
***

For additional information, refer to the following article: [Accept-Language header in HttpRequestHeaders](https://learn.microsoft.com/en-us/dotnet/api/system.net.http.headers.httprequestheaders.acceptlanguage).

### Specify a Filter Condition

To specify a filter condition, use a query parameter named `criteria`. For example, the following URL instructs the report to only include records where "FirstName" equals "Aaron":

`/api/Report/DownloadByName(ReportName)?criteria=[FirstName] = 'Aaron'`

>[!note]
>`ReportController` filters data on the server side. 
>
>The report itself can apply additional filter conditions to the data source. The criteria set by the report's [FilterString](xref:DevExpress.XtraReports.UI.XtraReportBase.FilterString) property take effect on the client side, after the data is loaded.

### Specify Sort Order

You can use the `sortProperty` query parameter. For example, the following URL sorts records by `FirstName` in descending order:

`/api/Report/DownloadByName(ReportName)?sortProperty=[FirstName],Descending`

>[!note]
The sort order can be overriden by the report. A report band's [SortFields](xref:DevExpress.XtraReports.UI.DetailBand.SortFields) property takes priority if it conflicts with the specified sort order.


### Pass Report Parameters
If your report uses [Parameters](xref:4812), you can pass their values in the query. For example, the following URL sets parameters `FirstName` and `Position` to "Mary" and "Manager", respectively:

`/api/Report/DownloadByKey({key})?FirstName=Mary&Position=Manager`

### Tutorial Video: Create a Report Access Endpoint and Use It from a MAUI App

The video below shows how you can use our Web Service API in your applications. The instructions guide you through the following tasks:

- Create a DevExpress Report and configure security permissions for different users. 
- Establish a Web API Service endpoint to allow report document downloads. 
- Utilize HTTP requests to display downloaded PDF documents in a MAUI app.

> [!video https://www.youtube.com/embed/bn4iF5Gc9XY]

The full example solution is available on GitHub:

[!example[How to Create a Web API Service Backend for a .NET MAUI Application](https://github.com/DevExpress-Examples/XAF_Security_E4908/tree/22.2.4%2B/EFCore/MAUI)]

## Report Controller Customization

To use Web API Authentication, decorate the `ReportController` with [AuthorizeAttribute](xref:403413).

Note that the `ReportController` uses a report export service: `IReportExportService`. This service loads a report and prepares it to be exported to the specified format.

# [C#](#tab/tabid-csharp)
```csharp
using Microsoft.AspNetCore.Mvc;
using DevExpress.ExpressApp.ReportsV2;

public class ReportController : ControllerBase {
    private readonly IReportExportService service;
    // ...
}
```
***

You can modify the controller's methods as required and even use `IReportExportService` to create custom endpoints. 

The report export service includes helper methods that manage reports and their data sources. Note the `SetupReport` method that allows you to specify the following parameters before report export: a filter condition and an array of sort properties.

# [C#](#tab/tabid-csharp)
```csharp
void SetupReport(XtraReport report, string criteria = null, 
                 SortProperty[] sortProperties = null);
```
***

## Add Unit Tests for Report Controller

Follow the steps below to add unit tests for code that queries reports from the `ReportController`.

1. If your solution does not have a testing project, add a new **xUnit test project**.
2. Add a reference to the `{SolutionName}.Blazor.Server` project.
3. Add the `Microsoft.AspNetCore.Mvc.Testing` package reference.
4. Add the following test to the test project:

    # [C#](#tab/tabid-csharp)
     
    ```csharp
    using System.Net.Http.Headers;
    using System.Text;
    using DevExpress.Data.Filtering;
    using DevExpress.Xpo;
    using DevExpress.XtraPrinting;
    using MainDemo.Module.BusinessObjects;
    using Microsoft.AspNetCore.Mvc.Testing;
    using Xunit;
    public class ReportByNameUnitTests
        : IClassFixture<WebApplicationFactory<MainDemo.Blazor.Server.Startup>> {
        HttpClient httpClient;
        string ApiUrl = "/api/Report/DownloadByName";

        public ReportByNameUnitTests(WebApplicationFactory<MainDemo.Blazor.Server.Startup> webApplicationFactory) {
            httpClient = webApplicationFactory.CreateClient();
            httpClient.DefaultRequestHeaders.Add("Accept-Language", "de-DE");
        }

        // A simple test example (no authentication)
        [Fact]
        public async System.Threading.Tasks.Task LoadReport() {
            string url = CreateRequestUrl("Employee List Report");
            var response = await httpClient.GetAsync(url);
            string loadedReport = await response.Content.ReadAsStringAsync();
            // Validate the result
            // ...
        }

        // An advanced test example
        [Fact]
        public async System.Threading.Tasks.Task LoadReportWithCriteria() {
            string tokenString = await GetUserTokenAsync("Sam", "", "/api/Authentication/Authenticate");
            var authorizationToken = new AuthenticationHeaderValue("Bearer", tokenString);

            string criteria = CriteriaOperator.FromLambda<Employee>(x => x.FirstName == "Aaron" || x.LastName == "Benson").ToString();
            string url = CreateRequestUrl("Employee List Report", criteria, null, null, ExportTarget.Csv);

            var httpRequest = new HttpRequestMessage(HttpMethod.Get, url);
            httpRequest.Headers.Authorization = authorizationToken;
            var response = await httpClient.SendAsync(httpRequest);
            string loadedReport = await response.Content.ReadAsStringAsync();
            // Validate the result
            // ...
        }

        private string CreateRequestUrl(
            string reportName, string? criteria = null, string? reportParameters = null,
            SortProperty[]? sortProperties = null, ExportTarget exportType = ExportTarget.Pdf) {

            string url = $"{ApiUrl}({reportName})";
            var q = $"fileType={exportType}";

            if(!string.IsNullOrEmpty(criteria)) {
                q += $"&criteria={criteria}";
            }
            if(sortProperties != null && sortProperties.Length > 0) {
                foreach(var sortProperty in sortProperties) {
                    q += $"&sortProperty={$"{sortProperty.PropertyName},{sortProperty.Direction}"}";
                }
            }
            if(!string.IsNullOrEmpty(reportParameters)) {
                q += $"&{reportParameters}";
            }

            url += "?" + q;

            return url;
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
