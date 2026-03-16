---
uid: DevExpress.ExpressApp.Win.WinWindow.LastActiveExplorer
name: LastActiveExplorer
type: Property
summary: Provides access to the last active explorer [](xref:DevExpress.ExpressApp.Win.WinWindow)'s [WinWindow.Form](xref:DevExpress.ExpressApp.Win.WinWindow.Form).
syntax:
  content: public static Form LastActiveExplorer { get; set; }
  parameters: []
  return:
    type: System.Windows.Forms.Form
    description: A [](xref:System.Windows.Forms.Form) object that is the last active explorer Window.
seealso:
- linkId: DevExpress.ExpressApp.Win.WinShowViewStrategyBase.Explorers
---
Generally, this method should not be called from your code. It is intended to be used in Windows Forms Show View Strategies (see [](xref:DevExpress.ExpressApp.ShowViewStrategyBase)) only.

An XAF Windows Forms application provides two types of Windows - **Explorer** and **Inspector**.

* **Explorer Window** - contains navigation items and can display several List and Detail Views in tabs (when the MDI is used).
* **Inspector Window** - does not provide navigation items and displays a single View