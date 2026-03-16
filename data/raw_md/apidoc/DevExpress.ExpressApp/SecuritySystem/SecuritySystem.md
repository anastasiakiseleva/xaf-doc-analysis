---
uid: DevExpress.ExpressApp.SecuritySystem
name: SecuritySystem
type: Class
summary: The static class that defines the XAF security system.
syntax:
  content: public static class SecuritySystem
seealso:
- linkId: DevExpress.ExpressApp.SecuritySystem._members
  altText: SecuritySystem Members
- linkId: "113366"
---
The **SecuritySystem** class provides the methods that implement the basic security system functionality. When the current end-user tries to access an object, the security system is asked whether there's permission to do it. It is assumed that end-users differ from one another by their type, which means that they have a different permission set. Based on that, the **SecuritySystem** allows the following:

* accessing the current user via the [SecuritySystem.CurrentUser](xref:DevExpress.ExpressApp.SecuritySystem.CurrentUser) property;
* determining the user type, name and logon parameters via  the [SecuritySystem.UserType](xref:DevExpress.ExpressApp.SecuritySystem.UserType), [SecuritySystem.CurrentUserName](xref:DevExpress.ExpressApp.SecuritySystem.CurrentUserName) and [SecuritySystem.LogonParameters](xref:DevExpress.ExpressApp.SecuritySystem.LogonParameters) properties;
* checking to see whether or not the user has permissions to access a particular object via the [SecuritySystem.IsGranted](xref:DevExpress.ExpressApp.SecuritySystem.IsGranted*) and [SecuritySystem.Demand](xref:DevExpress.ExpressApp.SecuritySystem.Demand*) methods (the **IsGranted** method returns a Boolean value, the **Demand** method raises an exception if access is denied).

> [!Tip]
> [!include[<whether or not the user has permissions to access a particular object><@DevExpress.ExpressApp.Security.IPermissionRequest>](~/templates/IsGrantedExtensions_WithoutIPermissionRequest.md)]

The **XAF** enables you to use different Security Strategies. The **SecuritySystem** actually delegates its functionality to the currently used Strategy. For instance, when you call the Security System's **Demand** method, the Security Strategy's **Demand** method is actually invoked. This allows you to implement business application features independent of the current Security Strategy, using only the Security System's methods and properties.
