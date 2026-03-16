---
uid: DevExpress.ExpressApp.DC.ITypeInfo.DefaultMember
name: DefaultMember
type: Property
summary: Returns metadata on the current type's default member.
syntax:
  content: IMemberInfo DefaultMember { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.DC.IMemberInfo
    description: The metadata on the current type's default member.
seealso: []
---
XAF checks if a business class contains the following properties and sets **DefaultMember** to the first found property:

1. The property specified by the class's @System.ComponentModel.DefaultPropertyAttribute or @DevExpress.ExpressApp.DC.XafDefaultPropertyAttribute.
2. A property whose name matches or contains one of the **DevExpress.ExpressApp.DC.TypeInfo.DefaultPropertyNames** values (Name, Title, Subject, Caption, Description, Benennung, Nombre, Nome). These values are arranged in priority order. For example, if a business class has both **ObjectName** and **Description** properties, **DefaultMember** returns **ObjectName**.
3. The property specified by the class's @DevExpress.Persistent.Base.FriendlyKeyPropertyAttribute.
4. The property specified by the class's **KeyAttribute**.

The following behavior is specific to the default members:

* Lookup Property Editors display default member values.
* Default members take part in form caption generation.
* In List Views, reference property columns display values of a referenced object's default member. The [FullTextSearch Action](xref:112997) considers these values when it filters objects.
* List Views display the default member column first.
