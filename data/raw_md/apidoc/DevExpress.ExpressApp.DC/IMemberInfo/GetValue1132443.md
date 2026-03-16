---
uid: DevExpress.ExpressApp.DC.IMemberInfo.GetValue(System.Object)
name: GetValue(Object)
type: Method
summary: Retrieves the member's value.
syntax:
  content: object GetValue(object obj)
  parameters:
  - id: obj
    type: System.Object
    description: The object whose property value will be returned.
  return:
    type: System.Object
    description: An object that is the member's value.
seealso: []
---
You can pass an object that is an actual member value, or an @DevExpress.ExpressApp.IObjectRecord object.

# [C#](#tab/tabid-csharp)

```csharp
ITypeInfo typeInfo = objectSpace.TypesInfo.FindTypeInfo(objectSpace.GetObjectType(objectRecord));
Object val = typeInfo.FindMember(propertyName).GetValue(objectRecord);
```
***