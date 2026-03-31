---
uid: DevExpress.ExpressApp.DC.IMemberInfo.AddAttribute(System.Attribute,System.Boolean)
name: AddAttribute(Attribute, Boolean)
type: Method
summary: Dynamically associates the specified attribute with the current member.
syntax:
  content: IMemberInfo AddAttribute(Attribute attribute, bool skipRefresh)
  parameters:
  - id: attribute
    type: System.Attribute
    description: An attribute to be associated with the current member.
  - id: skipRefresh
    type: System.Boolean
    description: '`true` to prevent the [Types Info Subsystem](xref:113669) from reloading @DevExpress.Xpo.Metadata.XPDictionary information immediately. In this case, you need to call the `XafMemberInfo.Refresh` method for each updated member.<br/> `false` to immediately refresh the type/member metadata. '
  return:
    type: DevExpress.ExpressApp.DC.IMemberInfo
    description: An object that allows you to further interact with member metadata information.
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