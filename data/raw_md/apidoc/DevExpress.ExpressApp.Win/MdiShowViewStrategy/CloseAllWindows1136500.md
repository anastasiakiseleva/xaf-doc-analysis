---
uid: DevExpress.ExpressApp.Win.MdiShowViewStrategy.CloseAllWindows
name: CloseAllWindows()
type: Method
summary: Tries to close all the Windows from the [WinShowViewStrategyBase.Windows](xref:DevExpress.ExpressApp.Win.WinShowViewStrategyBase.Windows) collection.
syntax:
  content: public override bool CloseAllWindows()
  return:
    type: System.Boolean
    description: '**true** if the Windows have been closed successfully; otherwise, **false**.'
seealso: []
---
Overrides the [WinShowViewStrategyBase.CloseAllWindows](xref:DevExpress.ExpressApp.Win.WinShowViewStrategyBase.CloseAllWindows) method of the base class. If there are several open explorer windows (these windows contain navigation items and can display several List and Detail Views in tabs), this method saves the current layout of all open windows to the Application Model and closes them. If you don't want the windows layout to be saved to the Model, set the Options node's **EnableKeepTabbedMdiLayout** property to **false**.