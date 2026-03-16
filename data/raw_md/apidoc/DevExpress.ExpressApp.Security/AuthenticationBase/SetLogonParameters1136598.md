---
uid: DevExpress.ExpressApp.Security.AuthenticationBase.SetLogonParameters(System.Object)
name: SetLogonParameters(Object)
type: Method
summary: Initializes the Logon Parameters.
syntax:
  content: public virtual void SetLogonParameters(object logonParameters)
  parameters:
  - id: logonParameters
    type: System.Object
    description: The Logon Parameters object.
seealso: []
---
In the [](xref:DevExpress.ExpressApp.Security.AuthenticationBase) class, the **SetLogonParameters** method does nothing. In the [client-server security configuration](xref:113439) with custom logon parameters, it is required to override this method in the following manner:

# [C#](#tab/tabid-csharp)

```csharp
public override void SetLogonParameters(object logonParameters) {
     this.logonParameters = (CustomLogonParameters)logonParameters;
}
```
***
Here, **logonParameters** is a private value holder of the [AuthenticationBase.LogonParameters](xref:DevExpress.ExpressApp.Security.AuthenticationBase.LogonParameters) property, and **CustomLogonParameters** is a type of your custom Logon Parameters object.