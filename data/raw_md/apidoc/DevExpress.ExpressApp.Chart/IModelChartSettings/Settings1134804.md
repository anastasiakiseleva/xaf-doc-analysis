---
uid: DevExpress.ExpressApp.Chart.IModelChartSettings.Settings
name: Settings
type: Property
summary: Provides access to the settings of the [charting List Editor](xref:113302) used by a [List View](xref:112611), editable using the Chart Designer.
syntax:
  content: string Settings { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string representing the serialized chart settings.
seealso:
- linkId: "113314"
---
This property stores charting settings configured using the Chart Designer. You can invoke this wizard from the [Model Editor](xref:112582), by clicking the ellipsis button (![EllipsisButton](~/images/ellipsisbutton116182.png)) of the Settings property.

![ModelEditor_SpecialEditors_ChartWizard](~/images/modeleditor_specialeditors_chartwizard116849.png)

In WinForms applications, end-users can also invoke the designer using the [](xref:DevExpress.ExpressApp.Chart.Win.ChartListEditor)'s context menu, if the [Application Model](xref:112580)'s [ICustomizationEnabledProvider.CustomizationEnabled](xref:DevExpress.ExpressApp.Chart.ICustomizationEnabledProvider.CustomizationEnabled) property of the ChartSettings node is set to **true**.

To learn about the Chart Designer capabilities in detail, refer to the [Chart Designer](xref:114070) help topic.