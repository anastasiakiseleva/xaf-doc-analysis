---
uid: DevExpress.ExpressApp.Blazor.SystemModule.IModelListViewTreeListBlazor.HasChildrenFieldName
name: HasChildrenFieldName
type: Property
summary: Specifies the field name that defines whether a node has children.
syntax:
  content: |-
    [DataSourceProperty("FieldNameSourceList", new string[]{})]
    [ModelBrowsable(typeof(IModelListViewTreeListBlazorVisibilityCalculator))]
    string HasChildrenFieldName { get; set; }
  parameters: []
  return:
    type: System.String
    description: The field name that defines whether a node has children.
seealso: []
---
This property targets the [DxTreeList.HasChildrenFieldName](xref:DevExpress.Blazor.DxTreeList.HasChildrenFieldName) property. In XAF ASP.NET Core Blazor applications, this model property is required when you use a data source with [flat data](xref:112836#flat-data-structure) objects in [Queryable Data Access Mode](xref:402925).