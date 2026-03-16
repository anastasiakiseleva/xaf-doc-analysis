---
uid: DevExpress.ExpressApp.Blazor.SystemModule.IModelListViewTreeListBlazor.KeyFieldName
name: KeyFieldName
type: Property
summary: Specifies the field name that contains unique identifiers for Tree List nodes.
syntax:
  content: |-
    [DataSourceProperty("FieldNameSourceList", new string[]{})]
    [ModelBrowsable(typeof(IModelListViewTreeListBlazorVisibilityCalculator))]
    string KeyFieldName { get; set; }
  parameters: []
  return:
    type: System.String
    description: The key field’s name.
seealso: []
---
This property targets the [DxTreeList.KeyFieldName](xref:DevExpress.Blazor.DxTreeList.KeyFieldName) property. In XAF ASP.NET Core Blazor applications, this model property is necessary when you use a data source with [flat data](xref:112836#flat-data-structure) objects. For more information, refer to the following topic: [](xref:405312).