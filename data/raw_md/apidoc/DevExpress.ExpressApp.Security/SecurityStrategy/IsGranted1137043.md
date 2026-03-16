---
uid: DevExpress.ExpressApp.Security.SecurityStrategy.IsGranted(System.Collections.Generic.IList{DevExpress.ExpressApp.Security.IPermissionRequest})
name: IsGranted(IList<IPermissionRequest>)
type: Method
summary: Checks whether the specified operations are allowed.
syntax:
  content: public virtual IList<bool> IsGranted(IList<IPermissionRequest> permissionRequests)
  parameters:
  - id: permissionRequests
    type: System.Collections.Generic.IList{DevExpress.ExpressApp.Security.IPermissionRequest}
    description: An **IList\<IPermissionRequest>** object that specifies the secured operations.
  return:
    type: System.Collections.Generic.IList{System.Boolean}
    description: '**true**, when the operations are allowed; otherwise, **false**.'
seealso: []
---
> [!Tip]
> [!include[<if the specified operations are allowed><@DevExpress.ExpressApp.Security.IPermissionRequest>](~/templates/IsGrantedExtensions_WithoutIPermissionRequest.md)]

The passed Permission Requests should have an appropriate Permission Request Processors registered within the Security Strategy. To register a Permission Request, handle the [SecurityStrategy.CustomizeRequestProcessors](xref:DevExpress.ExpressApp.Security.SecurityStrategy.CustomizeRequestProcessors) event.  Refer to the [How to: Implement Custom Security Objects (Users, Roles, Operation Permissions)](xref:113384) topic to see an example.