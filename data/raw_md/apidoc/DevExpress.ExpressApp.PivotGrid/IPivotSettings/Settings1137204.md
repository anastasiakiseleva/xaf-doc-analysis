---
uid: DevExpress.ExpressApp.PivotGrid.IPivotSettings.Settings
name: Settings
type: Property
summary: Provides access to the settings of the [pivot grid List Editor](xref:113303) used by a [List View](xref:112611), editable via the Pivot Grid Property Editor.
syntax:
  content: string Settings { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string representing the serialized pivot table settings.
seealso: []
---
This property stores pivot table settings configured via the Pivot Grid Property Editor. You can invoke this property editor from the [Model Editor](xref:112582), by clicking the ellipsis button (![EllipsisButton](~/images/ellipsisbutton116182.png)) of the Settings property.

![PivotGridPropertyEditor](~/images/pivotgridpropertyeditor116781.png)

In Windows Forms applications, end-users can also invoke the property editor via the [](xref:DevExpress.ExpressApp.PivotGrid.Win.PivotGridListEditor)'s context menu, if the [Application Model](xref:112580)'s [IPivotSettings.CustomizationEnabled](xref:DevExpress.ExpressApp.PivotGrid.IPivotSettings.CustomizationEnabled) property of the PivotSettings node is set to **true**.

To learn about the Pivot Grid Property Editor capabilities in detail, refer to the [Designer Dialog](xref:1825) help topic.