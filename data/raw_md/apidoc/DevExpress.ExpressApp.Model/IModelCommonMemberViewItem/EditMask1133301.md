---
uid: DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.EditMask
name: EditMask
type: Property
summary: Specifies a mask expression for a [Property Editor](xref:113097).
syntax:
  content: |-
    [ModelBrowsable(typeof(MaskSettingsVisibilityCalculator))]
    string EditMask { get; set; }
  parameters: []
  return:
    type: System.String
    description: A mask expression for a [Property Editor](xref:113097).
seealso:
- linkId: DevExpress.ExpressApp.Win.SystemModule.IModelMaskSettings.MaskSettings
- linkId: DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.EditMaskType
---
> [!NOTE]
> Use the [MaskSettings](xref:DevExpress.ExpressApp.Win.SystemModule.IModelMaskSettings.MaskSettings) property instead of the **EditMask** property in **WinForms** application projects.

The default **EditMask** value is the [IModelRegisteredPropertyEditor.DefaultEditMask](xref:DevExpress.ExpressApp.Editors.IModelRegisteredPropertyEditor.DefaultEditMask) property value. 

You can set the **EditMask** property in the [Model Editor](xref:112582).

![EditMask in the Model Editor](~/images/edit-mask-model-editor.png)

See the following topic for more information on how to specify mask expressions: [PropertyEditor.EditMask](xref:DevExpress.ExpressApp.Editors.PropertyEditor.EditMask).

[!include[EditMaskNote](~/templates/editmasknote11188.md)]