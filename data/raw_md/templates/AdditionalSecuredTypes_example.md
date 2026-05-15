The Security System allows you to configure [Type Permissions](xref:404633#type-permissions) for persistent types only. Non-persistent objects are not secured and users can access them. If you want to protect a non-persistent object type, add this type to the static [SecurityStrategy.AdditionalSecuredTypes](xref:DevExpress.ExpressApp.Security.SecurityStrategy.AdditionalSecuredTypes) collection and configure a **Type permission** for this type. 

The following examples show how to add the non-persistent `MyClass` type to the `AdditionalSecuredTypes` collection.

**WinForms**

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Security;
// ...
public partial class MainDemoWinApplication : WinApplication {
    static MainDemoWinApplication() {
        SecurityStrategy.AdditionalSecuredTypes.Add(typeof(MyClass));
    }
    // ...
}
```

# [VB.NET](#tab/tabid-vb)

```vb
Imports DevExpress.ExpressApp.Security
' ...
Partial Public Class MainDemoWinApplication
    Inherits WinApplication
    Shared Sub New()
        SecurityStrategy.AdditionalSecuredTypes.Add(GetType([MyClass]))
    End Sub
    ' ...
End Class
```
***

**ASP.NET Core Blazor**

# [C#](#tab/tabid-csharp1)

```csharp
using DevExpress.ExpressApp.Security;
// ...
public partial class MainDemoBlazorApplication : BlazorApplication {
    static MainDemoBlazorApplication() {
        SecurityStrategy.AdditionalSecuredTypes.Add(typeof(MyClass));
    }
    // ...
}
```

***