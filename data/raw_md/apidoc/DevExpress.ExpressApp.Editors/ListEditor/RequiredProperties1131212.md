---
uid: DevExpress.ExpressApp.Editors.ListEditor.RequiredProperties
name: RequiredProperties
type: Property
summary: Returns an array of descriptors for the properties considered bindable by the [List Editor](xref:113189)'s Collection Source.
syntax:
  content: public virtual string[] RequiredProperties { get; }
  parameters: []
  return:
    type: System.String[]
    description: An array of descriptors for the properties considered bindable by the List Editor's Collection Source.
seealso:
- linkId: "3113"
---
These properties are treated as displayable if a List View's data source is derived from the [](xref:DevExpress.Xpo.XPBaseCollection).
In addition, the properties whose names are stored in child nodes of the Application Model's [](xref:DevExpress.ExpressApp.Model.IModelColumns) node are treated as displayable, as well.

When deriving from the **ListEditor** class, you can return an empty collection. In this instance, only the properties specified in the Application Model will be treated as displayable.