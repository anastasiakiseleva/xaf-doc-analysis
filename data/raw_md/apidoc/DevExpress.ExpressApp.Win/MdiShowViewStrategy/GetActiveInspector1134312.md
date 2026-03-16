---
uid: DevExpress.ExpressApp.Win.MdiShowViewStrategy.GetActiveInspector(DevExpress.ExpressApp.Win.WinWindow)
name: GetActiveInspector(WinWindow)
type: Method
summary: Returns the active Inspector [Window](xref:112608) of a particular Explorer Window.
syntax:
  content: public WinWindow GetActiveInspector(WinWindow explorer)
  parameters:
  - id: explorer
    type: DevExpress.ExpressApp.Win.WinWindow
    description: A [](xref:DevExpress.ExpressApp.Win.WinWindow) object representing the Explorer Window whose active Inspector Window must be returned.
  return:
    type: DevExpress.ExpressApp.Win.WinWindow
    description: A [](xref:DevExpress.ExpressApp.Win.WinWindow) object representing the active Inspector Window of the specified Explorer Window.
seealso: []
---
An XAF Windows Forms application provides two types of Windows - **Explorer** and **Inspector**.

* **Explorer Window** - contains navigation items and can display several List and Detail Views in tabs (when the MDI is  used).
* **Inspector Window** - does not provide navigation items and displays a single View

Generally, you do not need to use this method.