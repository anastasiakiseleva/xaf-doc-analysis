---
uid: DevExpress.ExpressApp.Security.IPermissionRequest
name: IPermissionRequest
type: Interface
summary: Declares members implemented by Permission Request classes.
syntax:
  content: public interface IPermissionRequest
seealso:
- linkId: DevExpress.ExpressApp.Security.IPermissionRequest._members
  altText: IPermissionRequest Members
---
The Security System uses Permission Requests to determine whether or not a permission is granted. Objects of the **IPermissionRequest** type can be passed to the [SecurityStrategy.IsGranted](xref:DevExpress.ExpressApp.Security.SecurityStrategy.IsGranted*) and [SecuritySystem.Demand](xref:DevExpress.ExpressApp.SecuritySystem.Demand*) methods when it is required to check a permission in code.

To add a custom Permission Request, declare a class that implements the **IPermissionRequest** interface, or inherit the [](xref:DevExpress.ExpressApp.Security.OperationPermissionRequestBase) class (see [How to: Implement Custom Security Objects (Users, Roles, Operation Permissions)](xref:113384)).

> [!Tip]
> [!include[<whether or not a permission is granted><@DevExpress.ExpressApp.Security.IPermissionRequest>](~/templates/IsGrantedExtensions_WithoutIPermissionRequest.md)]