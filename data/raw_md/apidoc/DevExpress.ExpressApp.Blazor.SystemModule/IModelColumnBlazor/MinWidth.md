---
uid: DevExpress.ExpressApp.Blazor.SystemModule.IModelColumnBlazor.MinWidth
name: MinWidth
type: Property
summary: Specifies the minimum width of a column, in pixels.
syntax:
  content: |-
    [DefaultValue(50)]
    int MinWidth { get; set; }
  parameters: []
  return:
    type: System.Int32
    description: The minimum width of a column, in pixels.
seealso: []
---


Use the `MinWidth` property to set the minimum width of a grid column, in pixels. This value initializes the [DxGridColumn.MinWidth](xref:DevExpress.Blazor.DxGridColumn.MinWidth) property in the ASP.NET Core Blazor Grid Control that serves as the List View editor.

You can change the default value of this property in the [Model Editor](xref:112582). Note that if you set the property to `0`, the column collapses if the grid cannot display all its columns.

For additional information on how the grid layout is rendered in different scenarios, see the following topic: [](xref:403586).