---
uid: "113330"
seealso: []
title: Node Property Editors
owner: Ekaterina Kiseleva
---
# Node Property Editors

In the [Model Editor](xref:112582), the string property values displayed in the [Property Grid](xref:113329) can be edited with a simple string editor. However, the values of certain complex properties are difficult to edit manually. In these cases, an ellipsis button (![EllipsisButton](~/images/ellipsisbutton116182.png)) is displayed to the right of the property. Clicking this button invokes an _enhanced editor_, displayed in a popup window. This topic lists the enhanced property editors available in the **Model Editor**.

## Image Picker
The **Image Picker** is available for properties that refer to images and specify image names (for example, [IModelClass.ImageName](xref:DevExpress.ExpressApp.Model.IModelClass.ImageName) and [IModelAction.ImageMode](xref:DevExpress.ExpressApp.Model.IModelAction.ImageMode)). If you do not know the exact image name, click the ellipsis button (![EllipsisButton](~/images/ellipsisbutton116182.png)) displayed to the right of an image name and browse the available images within the **Image Picker** dialog.

![ModelEditor_SpecialEditors_Image](~/images/modeleditor_specialeditors_image116846.png)

> [!NOTE]
> The Image Picker lists images available in current [image sources](xref:112792). You cannot add custom images within this dialog. To add your own image, follow the technique described in the following help topic: [](xref:404209).

## Expression Editor
The **Expression Editor** is available for properties that specify [expressions](xref:4928) (e.g., [IModelMember.Expression](xref:DevExpress.ExpressApp.Model.IModelMember.Expression)). If you do not wish to type an expression manually, click the ellipsis button (![EllipsisButton](~/images/ellipsisbutton116182.png)) displayed to the right of an expression value and use the invoked [Expression Editor](xref:6212) dialog to select functions, operators and operands.

![Editor_Expression](~/images/editor_expression117367.png)

## Filter Builder
The **Filter Builder** is available for properties that specify [criteria](xref:4928) (for example, [IModelListView.Criteria](xref:DevExpress.ExpressApp.Model.IModelListView.Criteria), [IModelListViewFilterItem.Criteria](xref:DevExpress.ExpressApp.SystemModule.IModelListViewFilterItem.Criteria) and [IRuleBaseProperties.TargetCriteria](xref:DevExpress.Persistent.Validation.IRuleBaseProperties.TargetCriteria)). You can invoke the **Filter Builder** dialog to visually design the required criterion by clicking the ellipsis button (![EllipsisButton](~/images/ellipsisbutton116182.png)) displayed to the right of a criterion.

![ModelEditor_SpecialEditors_Criteria](~/images/modeleditor_specialeditors_criteria116847.png)

## Mask Editor
The **Mask Editor** is available for properties that specify [Edit Masks](xref:583) (for example, [IModelCommonMemberViewItem.EditMask](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.EditMask)). If you do not wish to type a mask manually, click the ellipsis button (![EllipsisButton](~/images/ellipsisbutton116182.png)) displayed to the right of a mask value. The dialog provides multiple predefined masks. It is also possible to create custom masks. The dialog's **Test Input** box allows you to test the selected mask.

![ModelEditor_SpecialEditors_EditMask](~/images/modeleditor_specialeditors_editmask116848.png)

## Chart Designer
The **Chart Designer** is intended to specify settings of the charting List Editor ([IModelChartSettings.Settings](xref:DevExpress.ExpressApp.Chart.IModelChartSettings.Settings)). To invoke the designer, click the ellipsis button (![EllipsisButton](~/images/ellipsisbutton116182.png)) displayed to the right of a settings string. To see an example of how to use this designer, refer to the [How to: Display a List View as a Chart](xref:113314) tutorial. To learn about the Chart Designer capabilities in detail, refer to the [Chart Designer](xref:114070) topic.

> [!NOTE]
> The **Chart Designer** is available only for XAF Windows Forms applications.

![ModelEditor_SpecialEditors_ChartWizard](~/images/modeleditor_specialeditors_chartwizard116849.png)

## PivotGrid Designer
The **PivotGrid Designer** is intended to specify settings of the Pivot Grid List Editor ([IPivotSettings.Settings](xref:DevExpress.ExpressApp.PivotGrid.IPivotSettings.Settings)). To invoke the wizard, click the ellipsis button (![EllipsisButton](~/images/ellipsisbutton116182.png)) displayed to the right of a settings string. To learn about PivotGrid Designer capabilities in detail, refer to the [PivotGrid Designer](xref:1825) help topic.

![ModelEditor_SpecialEditors_PivotSettingsEditor](~/images/modeleditor_specialeditors_pivotsettingseditor116850.png)