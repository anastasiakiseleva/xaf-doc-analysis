---
uid: DevExpress.Persistent.Base.DataSourcePropertyAttribute.UsedProperties
name: UsedProperties
type: Property
summary: Gets names of properties that affect lookup list construction for the current data source property.
syntax:
  content: public string[] UsedProperties { get; }
  parameters: []
  return:
    type: System.String[]
    description: An array of `System.String` values that specify property names.
seealso: []
---

A lookup list for a property may depend on values of other properties. If that's the case, specify these properties in the `UsedProperties` parameter of the [](xref:DevExpress.Persistent.Base.DataSourcePropertyAttribute). This setting allows XAF to automatically refresh Lookup Property Editors in Blazor applications when values of related properties change. Otherwise, you would need to refresh lookup editors manually.

## Example

This code example demonstrates a data model in which a customer's order can be assigned a `Product`, an `Accessory`, and a Boolean `IncludeGlobalAccessories` value. The Lookup Property Editor for the `Accessory` property is populated with data from the `AvailableAccessories` property. That property returns a filtered list based on the `Product` property value (if a product is specified) and the `IncludeGlobalAccessories` value.

Since the `AvailableAccessories` property uses other properties in calculations, the `Accessory` lookup editor must be updated when a user changes these properties. To achieve this, add the names of the used properties to the `UsedProperties` collection parameter in the [`DataSourcePropertyAttribute`](xref:DevExpress.Persistent.Base.DataSourcePropertyAttribute) declaration.

[!include[data-source-attribute-used-properties-code](~/templates/data-source-attribute-usedproperties-code.md)]

The image below illustrates the result:

![Result](~/images/xaf-blazor-filter-lookup-property-editor-manual-data-sources-devexpress.png)