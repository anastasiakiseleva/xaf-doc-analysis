---
uid: DevExpress.ExpressApp.PivotGrid.Win.PivotGridListEditor.BreakLinksToControls
name: BreakLinksToControls()
type: Method
summary: Removes references to the [](xref:DevExpress.ExpressApp.PivotGrid.Win.PivotGridListEditor)'s control and its event handlers.
syntax:
  content: public override void BreakLinksToControls()
seealso: []
---
The **BreakLinksToControls** method is used when disposing of the current [List Editor](xref:113189), or replacing it with another List Editor.

After disposing controls, raises the [PivotGridListEditor.PrintableChanged](xref:DevExpress.ExpressApp.PivotGrid.Win.PivotGridListEditor.PrintableChanged) event.

Generally, you do not need to use this method.