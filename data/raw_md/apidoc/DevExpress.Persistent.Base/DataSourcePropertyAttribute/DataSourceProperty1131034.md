---
uid: DevExpress.Persistent.Base.DataSourcePropertyAttribute.DataSourceProperty
name: DataSourceProperty
type: Property
summary: Returns a name of a business class collection property, serving as a source for the Lookup Property Editor of the target Object type business class property.
syntax:
  content: public string DataSourceProperty { get; }
  parameters: []
  return:
    type: System.String
    description: A string value representing the name of the source collection property for the target Object type property.
seealso: []
---
You can change the property name, which is specified in code, via the **BOModel** | **_\<Class\>_** | **OwnMembers** | **_\<Member\>_** node's [IModelMember.DataSourceProperty](xref:DevExpress.ExpressApp.Model.IModelMember.DataSourceProperty) property in the [Model Editor](xref:112830).