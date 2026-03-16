---
uid: DevExpress.Persistent.Base.DataSourcePropertyAttribute.#ctor(System.String,DevExpress.Persistent.Base.DataSourcePropertyIsNullMode,System.String[])
name: DataSourcePropertyAttribute(String, DataSourcePropertyIsNullMode, String[])
type: Constructor
summary: Initializes a new instance of the [](xref:DevExpress.Persistent.Base.DataSourcePropertyAttribute) class with the specified [DataSourcePropertyAttribute.DataSourceProperty](xref:DevExpress.Persistent.Base.DataSourcePropertyAttribute.DataSourceProperty), [DataSourcePropertyAttribute.DataSourcePropertyIsNullMode](xref:DevExpress.Persistent.Base.DataSourcePropertyAttribute.DataSourcePropertyIsNullMode), and [DataSourcePropertyAttribute.UsedProperties](xref:DevExpress.Persistent.Base.DataSourcePropertyAttribute.UsedProperties) properties.
syntax:
  content: public DataSourcePropertyAttribute(string dataSourceProperty, DataSourcePropertyIsNullMode mode, params string[] usedProperties)
  parameters:
  - id: dataSourceProperty
    type: System.String
    description: A string value that specifies the name of a collection property used as the data source for a List View displayed in a Lookup Property Editor or invoked by the [LinkUnlinkController.LinkAction](xref:DevExpress.ExpressApp.SystemModule.LinkUnlinkController.LinkAction) Action in a popup window.
  - id: mode
    type: DevExpress.Persistent.Base.DataSourcePropertyIsNullMode
    description: A **DataSourcePropertyIsNullMode** enumeration value that specifies the display mode for the target property's Lookup List View if the [DataSourcePropertyAttribute.DataSourceProperty](xref:DevExpress.Persistent.Base.DataSourcePropertyAttribute.DataSourceProperty) is not specified.
  - id: usedProperties
    type: System.String[]
    description: An array of `System.String` values that specify properties whose values are used to calculate the data source property's return value.
seealso: []
---
