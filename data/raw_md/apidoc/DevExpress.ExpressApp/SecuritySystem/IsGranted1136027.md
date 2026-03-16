---
uid: DevExpress.ExpressApp.SecuritySystem.IsGranted(DevExpress.ExpressApp.Security.IPermissionRequest)
name: IsGranted(IPermissionRequest)
type: Method
summary: Checks whether or not the current user is allowed to execute the specified secured operation.
syntax:
  content: public static bool IsGranted(IPermissionRequest permissionRequest)
  parameters:
  - id: permissionRequest
    type: DevExpress.ExpressApp.Security.IPermissionRequest
    description: An **IPermissionRequest** object that specifies the secured operation.
  return:
    type: System.Boolean
    description: '**true**, if the user can execute the secured operation; otherwise - **false**.'
seealso:
- linkId: "404204"
---
[!include[<if the current user is allowed to execute the specified secured operation><@DevExpress.ExpressApp.Security.IPermissionRequest>](~/templates/IsGrantedExtensions_WithoutIPermissionRequest.md)]