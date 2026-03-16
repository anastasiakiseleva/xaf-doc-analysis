---
uid: DevExpress.ExpressApp.Blazor.SystemModule.IModelListViewTreeListBlazor.ParentKeyFieldName
name: ParentKeyFieldName
type: Property
summary: Specifies the field that links a node to its parent.
syntax:
  content: |-
    [DataSourceProperty("FieldNameSourceList", new string[]{})]
    [ModelBrowsable(typeof(IModelListViewTreeListBlazorVisibilityCalculator))]
    string ParentKeyFieldName { get; set; }
  parameters: []
  return:
    type: System.String
    description: The name of the data field that stores parent node keys.
seealso: []
---
This property targets the [DxTreeList.ParentKeyFieldName](xref:DevExpress.Blazor.DxTreeList.ParentKeyFieldName) property. In XAF ASP.NET Core Blazor applications, this model property is necessary when you use a data source with [flat data](xref:112836#flat-data-structure) objects. For more information, refer to the following topic: [](xref:405312).