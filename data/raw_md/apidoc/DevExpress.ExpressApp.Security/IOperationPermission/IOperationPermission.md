---
uid: DevExpress.ExpressApp.Security.IOperationPermission
name: IOperationPermission
type: Interface
summary: Declares members implemented by the Operation Permission classes.
syntax:
  content: public interface IOperationPermission
seealso:
- linkId: DevExpress.ExpressApp.Security.IOperationPermission._members
  altText: IOperationPermission Members
---
You can inherit the [](xref:DevExpress.ExpressApp.Security.OperationPermissionRequestBase) class instead of implementing this interface "from scratch". Return the list of **IOperationPermission** objects in the overridden **GetPermissions** method when implementing a custom **PermissionData** descendant. Refer to the [How to: Implement Custom Security Objects (Users, Roles, Operation Permissions)](xref:113384) topic to see an example.