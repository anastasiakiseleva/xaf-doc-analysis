---
uid: DevExpress.ExpressApp.Model.NodeGenerators.ModelBOModelClassNodesGenerator.GetTypeId(System.Type)
name: GetTypeId(Type)
type: Method
summary: Returns an identifier of a given type.
syntax:
  content: public static string GetTypeId(Type type)
  parameters:
  - id: type
    type: System.Type
    description: A System.Type object.
  return:
    type: System.String
    description: A string identifier of a given type.
seealso: []
---
The **GetTypeId** method throws an **ArgumentException** if the passed type contains generic parameters (see [Type.ContainsGenericParameters](https://learn.microsoft.com/en-us/dotnet/api/system.type.containsgenericparameters#System_Type_ContainsGenericParameters)).
