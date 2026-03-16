---
uid: "404398"
title: Connect a Non-XAF Application to a Middle Tier Security Server (EF Core)
seealso:
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/connect-winforms-grid-to-backend-using-middletier-server
  altText: 'GitHub example: Connect the DevExpress WinForms Data Grid to a Backend using a Middle Tier Server (EF Core without OData)'
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/XAF_Security_E4908/tree/25.1.4+/EFCore/WinForms
  altText: 'GitHub example: Role-based Access Control, Permission Management, and OData / Web / REST API Services for Entity Framework and XPO ORM'
- linkId: 404389
- linkId: 404390
- linkId: 404391
- linkId: 403394
- linkId: 404691#ways-to-protect-database-connection-strings-in-desktop-web-or-mobile-clients
  altText: Ways to protect database connection strings in desktop, web, or mobile clients 
- linkId: 405145
---
# Connect a Non-XAF Application to a Middle Tier Security Server (EF Core)

The following steps outline how to connect a non-XAF .NET application to a database through the EF Core-based Middle Tier Security application.

> [!NOTE]
> The technique described in this topic was not tested with .NET MAUI and Blazor WebAssembly clients. With these platforms, we recommend that you use our [Web API Service](xref:403394) on the backend as demonstrated in the following examples on GitHub:
> - [How to Create a Web API Service Backend for a .NET MAUI Application](https://github.com/DevExpress-Examples/XAF_Security_E4908/tree/22.2.4%2B/EFCore/MAUI?utm_source=DevExpress&utm_medium=Website&utm_campaign=XAF&utm_content=XAF_Security_NonXAF_MAUI_EFCore)
> - [How to Create a Web API Service Backend for a Blazor WebAssembly Application](https://github.com/DevExpress-Examples/XAF_Security_E4908/tree/22.2.4%2B/EFCore/ASP.NetCore/Blazor.WebAssembly?utm_source=DevExpress&utm_medium=NonXAFSecurityLanding&utm_campaign=XAF&utm_content=XAF_Security_NonXAF_Blazor_WebAssembly)

1. Install the following NuGet package: [DevExpress.ExpressApp.EFCore](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.EFCore).

2. Create a Middle Tier client:

    ```csharp
    // The following code sample sets the Middle Tier server URL to the default value for debug mode
    // This setting may be different in your application
    // You can check this setting in the following Middle Tier project's file: Properties/launchSettings.json
    var middleTierClient = new MiddleTierClientBuilder<MainDemoDbContext>()
        .UseServer(" https://localhost:44319/ ")
        .UsePasswordAuthentication("John", "")
        .Build();
    ```

3. After the client successfully connects to the Middle Tier server and passes authentication, you can access security permissions for the current user.

    ```csharp
    var objectSpace = middleTierClient.CreateObjectSpace();
    bool isReadGranted = middleTierClient.Security.CanRead<Employee>(objectSpace);
    bool isWriteGranted = middleTierClient.Security.CanWrite<Employee>(objectSpace, nameof(Employee.Address1));
    ```

4. You can use the Middle Tier Security as a database provider to access data through an EF Core `DbContext` or Object Space:

    ```csharp
    // Use DbContext to access data:
    var dbContext = middleTierClient.CreateDbContext();
    var users = dbContext.Employees.ToList();

    // Use Object Space to access data:
    var objectSpace = middleTierClient.CreateObjectSpace();
    var users = objectSpace.GetObjectsQuery<Employee>().ToList();
    ```


5. You need to dispose the Middle Tier client when it is no longer needed:

    ```csharp
    middleTierClient.Dispose();
    ```

> [!tip]
> You can use [DevExpress Template Kit for Visual Studio](https://marketplace.visualstudio.com/items?itemName=DevExpress.devexpress-template-kit-for-visual-studio) to create WinForms and WPF applications that implement the described approach.

[`MiddleTierClientBuilder`]: xref:DevExpress.ExpressApp.ApplicationBuilder.MiddleTierClientBuilder`1
[`UseServer`]: xref:DevExpress.ExpressApp.ApplicationBuilder.MiddleTierClientBuilder`1.UseServer(System.String)
[`Build`]: xref:DevExpress.ExpressApp.ApplicationBuilder.MiddleTierClientBuilder`1.Build
[`UsePasswordAuthentication`]: xref:DevExpress.ExpressApp.ApplicationBuilder.MiddleTierClientBuilder`1.UsePasswordAuthentication*
[`CreateDbContext`]: xref:DevExpress.ExpressApp.ApplicationBuilder.IMiddleTierClient`1.CreateDbContext
[`CreateObjectSpace`]: xref:DevExpress.ExpressApp.ApplicationBuilder.IMiddleTierClient`1.CreateObjectSpace
[`Security`]: xref:DevExpress.ExpressApp.ApplicationBuilder.IMiddleTierClient`1.Security
