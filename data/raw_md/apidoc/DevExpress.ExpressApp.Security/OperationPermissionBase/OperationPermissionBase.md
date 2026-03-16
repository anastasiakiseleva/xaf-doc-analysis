---
uid: DevExpress.ExpressApp.Security.OperationPermissionBase
name: OperationPermissionBase
type: Class
summary: An abstact base class for Operation Permissions.
syntax:
  content: |-
    [DataContract]
    public abstract class OperationPermissionBase : IOperationPermission
seealso:
- linkId: DevExpress.ExpressApp.Security.OperationPermissionBase._members
  altText: OperationPermissionBase Members
---
The **OperationPermissionBase** class implements the [](xref:DevExpress.ExpressApp.Security.IOperationPermission) interface. You can inherit it instead of implementing the **IOperationPermission** interface "from scratch" when it is required to implement a custom Operation Permission.