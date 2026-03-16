---
uid: DevExpress.ExpressApp.Security.ClientServer.WebApi.WebApiDataServerHelper.AddKnownType(System.Type)
name: AddKnownType(Type)
type: Method
summary: Adds the specified [custom permission request](xref:113384) or custom logon parameter type to the ASP.NET Core Web API service known types list.
syntax:
  content: public static void AddKnownType(Type type)
  parameters:
  - id: type
    type: System.Type
    description: A type that this method adds to the ASP.NET Core Web API service known types list.
seealso: []
---
In applications with [Middle Tier Security](xref:113439), call this method on the server and client sides to register your custom permission requests and custom logon parameters. You do not need to use this method when you use standard logon parameters and do not have custom permission requests. Do not use this method to register [business classes](xref:113664).

The **AddKnownType** method throws an **InvalidOperationException** if the [WebApiDataServerHelper.GetKnownTypes](xref:DevExpress.ExpressApp.Security.ClientServer.WebApi.WebApiDataServerHelper.GetKnownTypes) method was already called internally. If you receive this exception, call this method earlier, before the data server and/or client application are initialized.
