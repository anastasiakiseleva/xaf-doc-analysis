---
uid: DevExpress.ExpressApp.DC.ITypeInfo.CreateMember(System.String,System.Type)
name: CreateMember(String, Type)
type: Method
summary: Dynamically adds a new member to the current type at run time.
syntax:
  content: IMemberInfo CreateMember(string memberName, Type memberType)
  parameters:
  - id: memberName
    type: System.String
    description: A string that holds the new member's name.
  - id: memberType
    type: System.Type
    description: A [](xref:System.Type) object that represents the type of the new member.
  return:
    type: DevExpress.ExpressApp.DC.IMemberInfo
    description: An [](xref:DevExpress.ExpressApp.DC.IMemberInfo) object that supplies metadata on the created member.
seealso: []
---
```csharp
ITypeInfo typeInfo1 = typesInfo.FindTypeInfo(typeof(PersistentObject1));

IMemberInfo memberInfo0 = typeInfo1.FindMember("NewIntField");
if (memberInfo0 == null) {
    typeInfo1.CreateMember("NewIntField", typeof(int));
}
// ...
typesInfo.RefreshInfo(typeof(PersistentObject1));
```

[!example[XAF - Customize an XPO Business Model at Runtime](https://github.com/DevExpress-Examples/xaf-customize-xpo-business-model-at-runtime)]