---
uid: DevExpress.ExpressApp.XafApplication.Security
name: Security
type: Property
summary: Provides access to the [Security Strategy](xref:113366) used in the application.
syntax:
  content: |-
    [Browsable(false)]
    public ISecurityStrategyBase Security { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Security.ISecurityStrategyBase
    description: An object that is the **ISecurityStrategyBase** Security Strategy.
seealso: []
---
To create a custom Security Strategy or Authentication Type, set the **Security** property in code:

# [C#](#tab/tabid-csharp)

```csharp
static class Program {
   // ... 
   public static void Main() {
      // ... 
      MySolutionWindowsFormsApplication application = new MySolutionWindowsFormsApplication();
      application.Security = new MySecurityStrategy<User, Role>(new MyAuthenticationStrategy<User, 
         AuthenticationStandardLogonParameters>())
      // ... 
      application.Setup();
      application.Start();
      // ... 
   }
}
```

# [VB.NET](#tab/tabid-vb)

```vb
Friend Class Program
   ' ... 
   Public Shared Sub Main()
      ' ... 
      Dim _application As MySolutionWindowsFormsApplication = _
      New MySolutionWindowsFormsApplication()
      _application.Security = New MySecurityStrategy(Of User, Role)( _
      New MyAuthenticationStrategy(Of User, AuthenticationStandardLogonParameters)())
      ' ... 
      _application.Setup()
      _application.Start()
      ' ... 
   End Sub 
End Class
```

***

For details on the Security System supplied by XAF, refer to the [Security System Overview](xref:113366) topic.