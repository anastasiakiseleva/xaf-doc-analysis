---
uid: DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.BackColor
name: BackColor
type: Property
summary: Specifies the background color of UI elements affected by the conditional appearance rule generated from this attribute instance.
syntax:
  content: public string BackColor { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string specifying the background color of UI elements affected by the conditional appearance rule.  A value should be recognizable by the [System.Drawing.ColorConverter](https://learn.microsoft.com/en-us/dotnet/api/system.drawing.colorconverter) class.
seealso:
- linkId: "113286"
---
The following UI elements can change their background color:

* Data cells in a [](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor) and [](xref:DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor)
* Nodes in a [](xref:DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditor)
* Property Editors that are inherited from the [](xref:DevExpress.ExpressApp.Win.Editors.DXPropertyEditor) and [](xref:DevExpress.ExpressApp.Blazor.Editors.BlazorPropertyEditorBase) types
* [](xref:DevExpress.ExpressApp.Editors.StaticText)

> [!NOTE]
> We do not recommend to apply the same background color for all business class properties. This setting changes the background color of selected rows in the [](xref:DevExpress.XtraGrid.GridControl), so the selection is invisible when you select rows with the modified background color.
>
> The font color depends on the current skin. Ensure that the specified background color does not make the text unreadable in certain skins. For more information about skins, refer to the following topic: [IModelApplicationOptionsSkin.Skin](xref:DevExpress.ExpressApp.Win.SystemModule.IModelApplicationOptionsSkin.Skin).

[!include[ConditionalAppearance_ObjectColoredInListView](~/templates/conditionalappearance_objectcoloredinlistview11916.md)]

[!include[<`Appearance` attribute>](~/templates/main-demo-tip.md)]