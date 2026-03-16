---
uid: DevExpress.ExpressApp.Security.SecurityStrategy.IsGranted(DevExpress.ExpressApp.Security.IPermissionRequest)
name: IsGranted(IPermissionRequest)
type: Method
summary: Checks whether the specified operation is allowed.
syntax:
  content: public virtual bool IsGranted(IPermissionRequest permissionRequest)
  parameters:
  - id: permissionRequest
    type: DevExpress.ExpressApp.Security.IPermissionRequest
    description: An [](xref:DevExpress.ExpressApp.Security.IPermissionRequest) object that specifies the secured operation.
  return:
    type: System.Boolean
    description: '**true**, when the operation is allowed; otherwise, **false**.'
seealso: []
---
> [!Tip]
> [!include[<if the specified operation is allowed><@DevExpress.ExpressApp.Security.IPermissionRequest>](~/templates/IsGrantedExtensions_WithoutIPermissionRequest.md)]

The passed Permission Request should have an appropriate Permission Request Processor registered within the Security Strategy. To register a Permission Request, handle the [SecurityStrategy.CustomizeRequestProcessors](xref:DevExpress.ExpressApp.Security.SecurityStrategy.CustomizeRequestProcessors) event. Refer to the [How to: Implement Custom Security Objects (Users, Roles, Operation Permissions)](xref:113384) topic to see an example.