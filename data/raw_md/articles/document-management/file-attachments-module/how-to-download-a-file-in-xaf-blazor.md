---
uid: "404760"
title: "How to: Download a File in XAF Blazor Applications"
owner: Irina Nikolaeva
---
# How to: Download a File in XAF Blazor Applications

This topic describes different ways to enable file download functionality in XAF ASP.NET Core Blazor applications. Examples in this topic use the [tutorial application](xref:402125) for demonstration purposes, but you can easily adapt these steps to suit your needs.

For information on how to **upload** files in XAF Blazor, refer to the following topic: [](xref:403360).

## Overview

XAF does not implement file download mechanisms and relies on [ASP.NET Core API](https://learn.microsoft.com/en-us/aspnet/core/blazor/file-downloads). The following sections contain examples that use this API in XAF Blazor applications: 

[Microsoft documentation](https://learn.microsoft.com/en-us/aspnet/core/blazor/file-downloads) describes two mechanisms to download files: 

1. Download a file from a stream (recommended for files smaller than 250 MB).

2. Download a file from a URL (recommended for files larger than 250 MB).

This topic demonstrates both of these approaches.

> [!NOTE]
> The sample below uses a void-returning async method for the `Execute` event handler. If you need to modify the suggested code, be aware that the caller of a void-returning async method cannot catch exceptions thrown by the method. Such unhandled exceptions may cause application failure. For more information about void-returning async methods, refer to the following Microsoft article: [Async return types (C#) - Void return type](https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/async-return-types#void-return-type).

## Download a File From a Stream

The example below uses JavaScript code to download a file. This code takes a link to a .NET stream ([](xref:Microsoft.JSInterop.DotNetStreamReference)) as a parameter. The application then calls this JavaScript code using the @Microsoft.JSInterop.IJSRuntime service.

To integrate this file download method into your application, follow the steps below:

1. Add the following JavaScript code to the `<body>` tag of your Blazor project's _YourSolutionName.Blazor.Server/Pages/_Host.cshtml_ file:

    ```HTML{8-20}
    <html>
        <body>
            @if(isIE) {
                <!-- ... -->
            }
            else {
                <!-- ... -->
                <script>
                window.downloadFileFromStream = async (fileName, contentStreamReference) => {
                    const arrayBuffer = await contentStreamReference.arrayBuffer();
                    const blob = new Blob([arrayBuffer]);
                    const url = URL.createObjectURL(blob);
                    const anchorElement = document.createElement('a');
                    anchorElement.href = url;
                    anchorElement.download = encodeURIComponent(fileName) ?? '';
                    anchorElement.click();
                    anchorElement.remove();
                    URL.revokeObjectURL(url);
                }
                </script>
            }
        </body>
    </html>
    ```

2. Add a new file (_DownloadFileController.cs_) to your Blazor project. This file should contain a View Controller that allows files to be downloaded.

    This controller adds a **Download a File** action to your application. When a user clicks the action, the application passes the `fileContent` value to the browser as a file.

    ```csharp
    using DevExpress.ExpressApp.Actions;
    using DevExpress.ExpressApp;
    using DevExpress.Persistent.Base;
    using Microsoft.JSInterop;
    using System.Text;

    namespace YourSolutionName.Blazor.Server.Controllers;

    public class DownloadFileController : ViewController {
        public DownloadFileController() {

            var downloadAction = new SimpleAction(this, "Download a File", PredefinedCategory.Save);

            downloadAction.Execute += async (s, e) => {

                IJSRuntime jsRuntime = Application.ServiceProvider.GetRequiredService<IJSRuntime>();
                var fileName = "Test.txt";

                // Replace this line with an actual stream, e.g. file stream File.OpenRead(filePath);
                var stream = new MemoryStream(Encoding.UTF8.GetBytes("YourData")); 
                using var streamRef = new DotNetStreamReference(stream: stream);
                await jsRuntime.InvokeVoidAsync("downloadFileFromStream", fileName, streamRef);
            };
        }
    }
    ```

3. Run the application and click **Download a File**. The specified file is downloaded to the browser.

    ![|DevExpress XAF: How to download a file](~/images/download-a-file-blazor.png)

## Download a File From a URL

To integrate this file download method into your application, follow the steps below:

1. Add the following JavaScript code to the `<body>` tag of your Blazor project's _YourSolutionName.Blazor.Server/Pages/_Host.cshtml_ file:

    ```HTML{8-16}
        <html>
        <body>
            @if(isIE) {
                <!-- ... -->
            }
            else {
                <!-- ... -->
                <script>
                window.triggerFileDownload = (fileName, url) => {
                    const anchorElement = document.createElement('a');
                    anchorElement.href = url;
                    anchorElement.download = encodeURIComponent(fileName) ?? '';
                    anchorElement.click();
                    anchorElement.remove();
                }
                </script>
             }
        </body>
    </html>
    ```

2. Create an endpoint (MVC controller) that provides access to the desired file. To do this, add a new file (_FileController.cs_) to the _API_ folder of your Blazor project. Note that this controller should contain the `Download` method.

    By default, ASP.NET Core Blazor Application projects do not include the _API_ folder. You may need to create it. 
    
    **File**: _YourSolutionName.Blazor.Server/API/FileController.cs_

    ```csharp
    using System.Text;
    using Microsoft.AspNetCore.Authorization;
    using Microsoft.AspNetCore.Mvc;

    namespace MySolution.Blazor.Server.API;

    [Route("api/[controller]")]
    [ApiController]
    [Authorize]
    public class FileController : ControllerBase {

        [HttpGet(nameof(Download))]
        public IActionResult Download(string fileName) {

            // Replace this line with an actual stream, e.g. file stream File.OpenRead(filePath);
            var stream = new MemoryStream(Encoding.UTF8.GetBytes("YourData"));
            return File(stream, "text/plain", fileName);
        }
    }
    ```

    > [!NOTE]
    > You must use the `Authorize` attribute in projects with the XAF Security System. For more information, refer to the following topic: [](xref:403858).
    >
    > In projects without the XAF Security System, remove this attribute from code.

3. If your project includes an authorization setting (`AddAuthorization` or `AddAuthorizationBuilder`), use the `CookieAuthenticationDefaults.AuthenticationScheme` setting to allow cookies in the project. The back-end can then use cookies to authorize download requests initiated by the Blazor application. For more endpoint-related notes, refer to the corresponding section below.

    To enable cookies, modify the `ConfigureServices` method in the _YourSolutionName.Blazor.Server/Startup.cs_ file as follows:

    ```csharp
    namespace YourSolutionName.Blazor.Server;

    public class Startup {
        // ...
        public void ConfigureServices(IServiceCollection services) {
            // ...
            services.AddAuthorizationBuilder()
                .SetDefaultPolicy(new AuthorizationPolicyBuilder(
                    JwtBearerDefaults.AuthenticationScheme, CookieAuthenticationDefaults.AuthenticationScheme)
                        .RequireAuthenticatedUser()
                        .RequireXafAuthentication()
                        .Build()); 
            });
    }
    ```

4. Add a new file (_DownloadFileController.cs_) with a View Controller to your Blazor project.

    This controller adds a **Download a File** action to your application. When a user clicks the action, the application passes the `fileContent` value to the browser as a file.

    ```csharp
    using DevExpress.ExpressApp.Actions;
    using DevExpress.ExpressApp;
    using DevExpress.Persistent.Base;
    using Microsoft.JSInterop;
    using Microsoft.AspNetCore.Components;

    namespace YourSolutionName.Blazor.Server.Controllers;

    public partial class DownloadFileController : ViewController {

        public DownloadFileController() {
            var downloadAction = new SimpleAction(this, "Download a File", PredefinedCategory.Save);

            downloadAction.Execute += async (s, e) => {
                IJSRuntime jsRuntime = Application.ServiceProvider.GetRequiredService<IJSRuntime>();
                NavigationManager navigationManager = Application.ServiceProvider.GetRequiredService<NavigationManager>();
                var fileName = "Test.txt";
                var fileURL = $"{navigationManager.BaseUri}api/File/Download?fileName={fileName}";
                await jsRuntime.InvokeVoidAsync("triggerFileDownload", fileName, fileURL);
            };
        }
    }
    ```

3. Run the application and click **Download a File**. The specified file is downloaded to the browser.

    ![|DevExpress XAF: How to download a file](~/images/download-a-file-blazor.png)

### Endpoint-Related Notes

* XAF Blazor already has an API endpoint that can return data from the File Attachment module's IFileData objects. If your task uses files attached to Business Objects, you can use the `{navigationManager.BaseUri}IFileUrlService/?objectType= MySolution.Module.BusinessObjects.Resume&objectKey=1dc9dfd3-7389-4e17-930c-c4018deb4acc&propertyName=File` URL pattern instead of implementing your own API controller.
* If you use an XAF Blazor project with Web API (Integrated Mode), you can also use the XAF Web API _MediaFile/DownloadStream_ endpoint that returns data from the File Attachment module's `IFileData` objects. This service has similar functionality to `IFileUrlService` mentioned before but offers more customization options. We recommend that you use this endpoint if you use Web API in your project. In this case, use the following URL pattern: `{navigationManager.BaseUri}api/MediaFile/DownloadStream?objectType=Employee&objectKey=0eb531f9-2195-49e4-60b1-08db8ba8ed44&propertyName=Photo`.

    For more information about this endpoint, refer to the following topic:  [](xref:404207).
