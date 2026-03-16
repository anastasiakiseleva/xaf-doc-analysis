---
uid: DevExpress.ExpressApp.Model.NodeGenerators.ModelBOModelClassNodesGenerator.TryGetTypeId(System.Type,System.String@)
name: TryGetTypeId(Type, out String)
type: Method
summary: Tries to get an identifier of a given type.
syntax:
  content: public static bool TryGetTypeId(Type type, out string typeId)
  parameters:
  - id: type
    type: System.Type
    description: A System.Type object.
  - id: typeId
    type: System.String
    description: A string identifier of a given type.
  return:
    type: System.Boolean
    description: On success, returns **true**; otherwise, **false**.
seealso: []
---
The **TryGetTypeId** method returns **false** and sets the _typeId_ parameter to null if the passed type contains generic parameters (see [Type.ContainsGenericParameters](https://learn.microsoft.com/en-us/dotnet/api/system.type.containsgenericparameters#System_Type_ContainsGenericParameters)).
