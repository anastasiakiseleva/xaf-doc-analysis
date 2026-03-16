---
uid: DevExpress.ExpressApp.SecuritySystem.IsGrantedNavigate(System.String,System.Type,System.Object,DevExpress.ExpressApp.IObjectSpace)
name: IsGrantedNavigate(String, Type, Object, IObjectSpace)
type: Method
summary: Checks whether or not the specified navigation permission is granted to the current user.
syntax:
  content: public static bool IsGrantedNavigate(string itemPath, Type objectType, object targetObject, IObjectSpace objectSpace)
  parameters:
  - id: itemPath
    type: System.String
    description: A string specifying the navigation item path. The delimiter is the slash character ("/").
  - id: objectType
    type: System.Type
    description: A target object type.
  - id: targetObject
    type: System.Object
    description: A target object.
  - id: objectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) object which is the [Object Space](xref:113707) used to process the request.
  return:
    type: System.Boolean
    description: '**true**, if the specified permission is granted; otherwise, **false**.'
seealso: []
---
The *objectType* and *targetObject* parameters should not be *null* when the [SecurityStrategy.SupportNavigationPermissionsForTypes](xref:DevExpress.ExpressApp.Security.SecurityStrategy.SupportNavigationPermissionsForTypes) property is set to **true** and you use navigation permissions determined in the [Type Permissions](xref:113366) tab. If this property is set to **false** or you use only navigation permissions in the **Navigation Permissions** tab, you can pass this parameter as *null*.