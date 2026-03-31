---
uid: DevExpress.ExpressApp.DC.IBaseInfo.AddAttribute(System.Attribute)
name: AddAttribute(Attribute)
type: Method
summary: Dynamically associates the specified attribute with the current type or member.
syntax:
  content: IBaseInfo AddAttribute(Attribute attribute)
  parameters:
  - id: attribute
    type: System.Attribute
    description: An attribute to be associated with the current type or member.
  return:
    type: DevExpress.ExpressApp.DC.IBaseInfo
    description: An object that allows you to further interact with type/member metadata information.
seealso:
- linkId: 113583
- linkId: 113669
---
```csharp
public override void CustomizeTypesInfo(DevExpress.ExpressApp.DC.ITypesInfo typesInfo) {
    base.CustomizeTypesInfo(typesInfo);
    CalculatedPersistentAliasHelper.CustomizeTypesInfo(typesInfo);
    ITypeInfo pType = typesInfo.FindTypeInfo(typeof(PersistentObject1));
    pType.CreateMember("CustomDecimalField", typeof(decimal))
        .AddAttribute(new ModelDefaultAttribute("DisplayFormat", "n2"))
        .AddAttribute(new ModelDefaultAttribute("EditMask", "n2"));
    // ...
    typesInfo.RefreshInfo(typeof(PersistentObject1));
}
```