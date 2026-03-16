---
uid: DevExpress.ExpressApp.PivotGrid.Win.PivotGridListEditor.PivotGridControl
name: PivotGridControl
type: Property
summary: Provides access to the [](xref:DevExpress.ExpressApp.PivotGrid.Win.PivotGridListEditor)'s pivot grid control.
syntax:
  content: public PivotGridControl PivotGridControl { get; }
  parameters: []
  return:
    type: DevExpress.XtraPivotGrid.PivotGridControl
    description: A [](xref:DevExpress.XtraPivotGrid.PivotGridControl) object representing the current List Editor's pivot grid control.
seealso: []
---
Pivot grid [List Editors](xref:113189) display data in the form of a pivot table that can be accompanied by a chart. So, these List Editors actually use two controls in a UI - one control represents the pivot table and another control represents the chart. The **PivotGridControl** property provides access to the control representing the List Editor's pivot table.

You can use this property to customize the List Editor's control. Generally, the recommended place to do this is a custom [Controller](xref:112621)'s [ViewController.ViewControlsCreated](xref:DevExpress.ExpressApp.ViewController.ViewControlsCreated) event handler. The [](xref:402154) article illustrates this approach.

If you need to execute a custom action after a List Editor's control has been created, handle the [ListEditor.ControlsCreated](xref:DevExpress.ExpressApp.Editors.ListEditor.ControlsCreated) event.