---
uid: DevExpress.ExpressApp.Win.WinShowViewStrategyBase.Explorers
name: Explorers
type: Property
summary: Gets a list of the application's Explorer [Windows](xref:112608).
syntax:
  content: public List<WinWindow> Explorers { get; }
  parameters: []
  return:
    type: System.Collections.Generic.List{DevExpress.ExpressApp.Win.WinWindow}
    description: A **List\<**[](xref:DevExpress.ExpressApp.Win.WinWindow)**>** object representing a list of the application's Explorer Windows.
seealso:
- linkId: DevExpress.ExpressApp.Win.WinShowViewStrategyBase.Inspectors
- linkId: DevExpress.ExpressApp.Win.WinShowViewStrategyBase.Windows
- linkId: DevExpress.ExpressApp.Win.WinWindow.LastActiveExplorer
---
An XAF Windows Forms application provides two types of Windows - **Explorer** and **Inspector**.

* **Explorer Window** - contains navigation items and can display several List and Detail Views in tabs (when the MDI is used).
* **Inspector Window** - does not provide navigation items and displays a single View

Generally, you do not need to access this property.