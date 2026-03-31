---
uid: "402078"
title: Audit the Current User or Host Identity (XPO)
---

# Audit the Current User or Host Identity (XPO)

If you build a business application that is intended for use by multiple users at the same time, you need to get information on who made a particular change. For this purpose, the `CurrentUserName` property of the application's [Security System](xref:113366) is passed to the Audit Trail system. If you do not use the XAF Security System, handle the [](xref:DevExpress.Persistent.BaseImpl.AuditTrail.Services.AuditTrailServiceBase.QueryCurrentUserName) event to specify the user name for audit records. In an XAF Windows Forms application, you can get the user name from the `WindowsIdentity` object. 

1. Create the `AuditTrailUserNameHandler` class that handles the `QueryCurrentUserName` event.

**File:** _MySolution.Win\AuditTrailUserNameHandler.cs_

# [C# (WinForms)](#tab/tabid-csharp-winforms)

```csharp
using System.Security.Principal;

namespace MySolution.Win;

public class AuditTrailUserNameHandler {
    public AuditTrailUserNameHandler(IAuditTrailService auditTrailService) {
        auditTrailService.QueryCurrentUserName += OnQueryCurrentUserName;
    }

    private void OnQueryCurrentUserName(object sender, QueryCurrentUserNameEventArgs e) {
        e.CurrentUserName = WindowsIdentity.GetCurrent().Name;
    }
}
```
***

2. Register the event handler in the DI container.

**File:** _MySolution.Win\ApplicationBuilder.cs_

# [C# (WinForms)](#tab/tabid-csharp-winforms)

```csharp{9}
using Microsoft.Extensions.DependencyInjection;

namespace MySolution.Win;

public class ApplicationBuilder : IDesignTimeApplicationFactory {

    public static WinApplication BuildApplication() {
        var builder = WinApplication.CreateBuilder();
        builder.Services.AddSingleton<AuditTrailUserNameHandler>();
        //...
    }
    //...
}
```
***

3. Ensure that the event handler resolves at the application's start.

**File:** _MySolution.Win\ApplicationBuilder.cs_

# [C# (WinForms)](#tab/tabid-csharp-winforms)

```csharp{10-13}
using Microsoft.Extensions.DependencyInjection;

namespace MySolution.Win;

public class ApplicationBuilder : IDesignTimeApplicationFactory {

    public static WinApplication BuildApplication() {
        var builder = WinApplication.CreateBuilder();
        // ...
        builder.AddBuildStep(application => {
        var serviceProvider = ((WinApplication)application).ServiceProvider;
        // Resolving the handler ensures the event is attached
        serviceProvider.GetRequiredService<AuditTrailUserNameHandler>();
        // ...
        })
    }
}
```
***