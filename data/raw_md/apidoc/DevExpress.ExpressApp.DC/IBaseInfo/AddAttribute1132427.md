---
uid: DevExpress.ExpressApp.DC.IBaseInfo.AddAttribute(System.Attribute)
name: AddAttribute(Attribute)
type: Method
summary: Dynamically associates an attribute to the current type at run time.
syntax:
  content: IBaseInfo AddAttribute(Attribute attribute)
  parameters:
  - id: attribute
    type: System.Attribute
    description: A descendant of the **System.Attribute** class that represents the attribute which will be associated with the current type at run time.
  return:
    type: DevExpress.ExpressApp.DC.IBaseInfo
    description: ''
seealso: []
---
```csharp
ITypeInfo typeInfo1 = typesInfo.FindTypeInfo(typeof(PersistentObject1));
typeInfo1.AddAttribute(new DevExpress.Persistent.Base.DefaultClassOptionsAttribute());
// ...
typesInfo.RefreshInfo(typeof(PersistentObject1));
```

[!example[XAF - Customize an XPO Business Model at Runtime](https://github.com/DevExpress-Examples/xaf-customize-xpo-business-model-at-runtime)]