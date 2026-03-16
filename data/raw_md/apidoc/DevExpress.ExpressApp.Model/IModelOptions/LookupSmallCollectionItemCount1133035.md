---
uid: DevExpress.ExpressApp.Model.IModelOptions.LookupSmallCollectionItemCount
name: LookupSmallCollectionItemCount
type: Property
summary: Used by reference properties that are displayed by a Look-up Property Editor in [](xref:DevExpress.Persistent.Base.LookupEditorMode.Auto) mode. For more information, see [IModelCommonMemberViewItem.LookupEditorMode](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.LookupEditorMode). If the element count in the Look-up Property Editor's data source collection is greater than this property value, XAF does not load them and enables the Search feature.
syntax:
  content: |-
    [DefaultValue(25)]
    int LookupSmallCollectionItemCount { get; set; }
  parameters: []
  return:
    type: System.Int32
    description: An integer value that specifies the minimum object count required to enable the Search functionality.
seealso: []
---
You can change this property value in the [Model Editor](xref:112582).

![|LookupSmallCollectionItemCount](~/images/lookupsmallcollectionitemcount119000.png)

> [!NOTE]
>  In an XAF ASP.NET Core Blazor application, this setting is ignored, and XAF does not enable Search automatically. For details on how to enable this feature, refer to the following topic: [](xref:112925).