---
uid: "403982"
seealso:
- linkType: HRef
  linkId: https://community.devexpress.com/blogs/news/archive/2023/04/17/consume-the-devexpress-backend-web-api-from-javascript-with-svelte-part-2-model-info.aspx?utm_source=DevExpress&utm_medium=Blog&utm_id=XAF&utm_term=part4&utm_content=oliver-apr2022
  altText: Consume the DevExpress Backend Web API from JavaScript with Svelte (Part 2. Manage Localization and UI Settings)
title: 'Obtain Localization Strings from a Web API Controller Endpoint'
---
# Obtain Localization Strings from a Web API Controller Endpoint

This topic demonstrates how to obtain localized UI strings through HTTP requests to a [Web API](xref:403394) service. You can use the localized UI strings in your custom application that uses the XAF Web API as a backend. 

Refer to the following article for instructions on how to localize UI strings for an XAF application: [](xref:113298).

>[!note]
 This option of our Web API Service ships as part of the [DevExpress Universal Subscription](https://www.devexpress.com/subscriptions/universal.xml).

## Localization Controller

### Localization Controller API

Use the localization controller API to obtain translations for the following strings:

- Class captions

  **Web API Endpoint**: `Localization/ClassCaption?classFullName=...`

  **Method called in the controller**: [CaptionHelper.GetClassCaption](xref:DevExpress.ExpressApp.Utils.CaptionHelper.GetClassCaption(System.String))
- Member captions
  
   **Web API Endpoint**: `Localization/MemberCaption?typeFullName=...&memberName=...`

   **Method called in the controller**: [CaptionHelper.GetMemberCaption(Type, String)](xref:DevExpress.ExpressApp.Utils.CaptionHelper.GetMemberCaption(System.Type,System.String))
   
   The `typeFullName` string parameter is equal to `typeof(objectType).FullName`.
- Action captions

  **Web API Endpoint**: `Localization/ActionCaption?actionName=...` 

  **Method called in the controller**: [CaptionHelper.GetActionCaption](xref:DevExpress.ExpressApp.Utils.CaptionHelper.GetActionCaption(System.String))
- Custom strings

  **Web API Endpoint**: `Localization/LocalizedText?groupPath=...&itemName=...` 

  **Method called in the controller**: [CaptionHelper.GetLocalizedText](xref:DevExpress.ExpressApp.Utils.CaptionHelper.GetLocalizedText(System.String,System.String))
  
You can control the language for localization through the `Accept-Language` request header. This header accepts language identifiers such as `en`, `de`, `ja`, and others. For additional details, refer to [Globalization and localization in ASP.NET Core](http://docs.microsoft.com/en-us/aspnet/core/fundamentals/localization).

> [!NOTE]
> 
> The localization controller does not require authorization. You need to take the following data access specifics into account:
> - You can access the localization controller without JWT tokens that are required for Web API endpoints. 
> - The localization controller provides access to a shared model layer, without considering user changes. 
> - You cannot use the localization controller to access secure data. 
>
> Without authorization, the controller has significantly better performance, which means it can process many more requests per second than other Web API endpoints.


### Example

This example demonstrates how to obtain a localized string. The code in this example sends a request to the `Localization/LocalizedText` endpoint with the `groupPath` and `itemName` parameters.

# [C#](#tab/tabid-csharp1)
 
```csharp
// This code requests a German version of 
// the `Messages:CannotUploadFile` caption.

HttpClient httpClient = new HttpClient();

// Set up client locale and Uri.
httpClient.BaseAddress = new Uri("https://localhost:5001/");
httpClient.DefaultRequestHeaders.Add("Accept-Language", "de");

// Arguments for the LocalizedText method.
var groupPath = "Messages";
var itemName = "CannotUploadFile";

// Send request for a localized string.
var response = await httpClient.GetAsync($"api/Localization/LocalizedText?groupPath={groupPath}&itemName={itemName}");

// Parse the result from HttpResponseMessage.
var localizedString = await response.Content.ReadAsStringAsync();
```
***

You can configure the request locale directly on an `HttpRequestMessage` as follows. For more details, read [Accept-Language header in HttpRequestHeaders](https://learn.microsoft.com/en-us/dotnet/api/system.net.http.headers.httprequestheaders.acceptlanguage).

# [C#](#tab/tabid-csharp1)
 
```csharp
var customRequest = new HttpRequestMessage(HttpMethod.Get, $"api/Localization/LocalizedText?groupPath={groupPath}&itemName={itemName}");

customRequest.Headers.Add("Accept-Language", "en");

var response = await httpClient.SendAsync(customRequest);
```
***


## Add Unit Tests for Localization Controller

1. If your solution does not have a testing project, add a new **xUnit test project**.
2. Add a reference to `{SolutionName}.Blazor.Server` project.
3. Add the `Microsoft.AspNetCore.Mvc.Testing` package reference.
4. Add the following test to the xUnit project:

    # [C#](#tab/tabid-csharp1)
     
    ```csharp
    using System.Net.Http;
    using System.Threading.Tasks;
    using Microsoft.AspNetCore.Mvc.Testing;
    using Xunit;
    public class LocalizationUnitTests
        : IClassFixture<WebApplicationFactory<MySolution.Blazor.Server.Startup>> {
        HttpClient httpClient;
        public LocalizationUnitTests(WebApplicationFactory<MySolution.Blazor.Server.Startup> webApplicationFactory) {
            httpClient = webApplicationFactory.CreateClient();
            httpClient.DefaultRequestHeaders.Add("Accept-Language", "de");
        }
        // A simple test example.
        [Fact]
        public async Task SampleLocalizationTest() {
            var groupPath = "Messages";
            var itemName = "CannotUploadFile";
            var response = await httpClient.GetAsync($"api/Localization/LocalizedText?groupPath={groupPath}&itemName={itemName}");
            var localizedString = await response.Content.ReadAsStringAsync();
            Assert.NotEmpty(localizedString);
        }
        // An advanced test example.
        [Theory]
        [InlineData("en", "Messages", "CannotUploadFile")]
        [InlineData("de", "Messages", "CannotUploadFile")]
        public async Task TestLocalizedText(string locale, string groupPath, string itemName) {
            var customRequest = new HttpRequestMessage(HttpMethod.Get, $"api/Localization/LocalizedText?groupPath={groupPath}&itemName={itemName}");
            customRequest.Headers.Add("Accept-Language", locale);
            var response = await httpClient.SendAsync(customRequest);
            var localizedString = await response.Content.ReadAsStringAsync();
            Assert.NotEmpty(localizedString);
        }
    }
    ```
    ***
