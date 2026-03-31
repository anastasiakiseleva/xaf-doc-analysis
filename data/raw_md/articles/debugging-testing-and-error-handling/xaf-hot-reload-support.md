---
uid: "404703"
title: Hot Reload Support (ASP.NET Core Blazor)
seealso:
- linkId: 113653
- linkId: 403452
---
# Hot Reload Support (ASP.NET Core Blazor)

XAF ASP.NET Core Blazor applications support [Hot Reload](https://learn.microsoft.com/en-us/aspnet/core/test/hot-reload), a feature of Visual Studio debugger. It allows you to see changes in the UI without restarting your application when you modify markup or logic in your custom Razor components or modify the methods of your View Controllers and Actions, such as `Execute` event handlers.

## Limitations

Hot Reload is not supported when you change the entire application structure or `XafApplication` requires setup or restart. Review the following list for examples of such changes:
* Changes in _Startup.cs_, _Module.cs_, _BlazorApplication.cs_.
* Changes in XAFML, JSON, and other configuration or resource files.
* Creation, deletion, and modification of ORM business classes and XAF controllers.

For more information, refer to Microsoft documentation: [Unsupported changes to code](https://learn.microsoft.com/en-us/visualstudio/debugger/supported-code-changes-csharp#unsupported-changes-to-code).