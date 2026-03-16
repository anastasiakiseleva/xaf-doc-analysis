---
uid: DevExpress.ExpressApp.SecuritySystem.IsGranted(DevExpress.ExpressApp.IObjectSpace,System.Type,System.String,System.Object,System.String)
name: IsGranted(IObjectSpace, Type, String, Object, String)
type: Method
summary: Checks whether or not the specified permission is granted to the current user.
syntax:
  content: public static bool IsGranted(IObjectSpace objectSpace, Type objectType, string operation, object targetObject, string memberName)
  parameters:
  - id: objectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) object which is the [Object Space](xref:113707) used to process the request.
  - id: objectType
    type: System.Type
    description: A target object type.
  - id: operation
    type: System.String
    description: A string which is the name of the requested operation. Operation names are declared as the [](xref:DevExpress.ExpressApp.Security.SecurityOperations) class' constants.
  - id: targetObject
    type: System.Object
    description: A target object.
  - id: memberName
    type: System.String
    description: A string which is the name of the target object's member.
  return:
    type: System.Boolean
    description: '**true**, if the specified permission is granted; otherwise, **false**.'
seealso:
- linkId: "404204"
---
You can also use the @DevExpress.ExpressApp.Security.IsGrantedExtensions class methods to check if the specified permission is granted to the current user.