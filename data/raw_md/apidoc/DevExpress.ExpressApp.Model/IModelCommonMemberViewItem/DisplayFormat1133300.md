---
uid: DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.DisplayFormat
name: DisplayFormat
type: Property
summary: Specifies a display format pattern for a [Property Editor](xref:113097)'s value.
syntax:
  content: |-
    [ModelBrowsable(typeof(ListEditorsVisibilityCalculator))]
    string DisplayFormat { get; set; }
  parameters: []
  return:
    type: System.String
    description: A display format pattern for a Property Editor's value.
seealso: []
---
The default **DisplayFormat** value is the [IModelRegisteredPropertyEditor.DefaultDisplayFormat](xref:DevExpress.ExpressApp.Editors.IModelRegisteredPropertyEditor.DefaultDisplayFormat) property value.

Use the [Model Editor](xref:112582) to set the **DisplayFormat** property value as described in the following article: [](xref:402141).

See the following topic for more information on how to specify a display format pattern: [PropertyEditor.DisplayFormat](xref:DevExpress.ExpressApp.Editors.PropertyEditor.DisplayFormat).