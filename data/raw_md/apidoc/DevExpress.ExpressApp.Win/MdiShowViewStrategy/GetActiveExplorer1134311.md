---
uid: DevExpress.ExpressApp.Win.MdiShowViewStrategy.GetActiveExplorer
name: GetActiveExplorer()
type: Method
summary: Returns the active Explorer [Window](xref:112608).
syntax:
  content: public WinWindow GetActiveExplorer()
  return:
    type: DevExpress.ExpressApp.Win.WinWindow
    description: A [](xref:DevExpress.ExpressApp.Win.WinWindow) object representing the active Explorer Window.
seealso: []
---
An XAF Windows Forms application provides two types of Windows - **Explorer** and **Inspector**.

* **Explorer Window** - contains navigation items and can display several List and Detail Views in tabs (when the MDI is  used).
* **Inspector Window** - does not provide navigation items and displays a single View

Generally, you do not need to use this method.