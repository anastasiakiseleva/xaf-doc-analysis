---
uid: DevExpress.ExpressApp.View
name: View
type: Class
summary: The base class for [Views](xref:112611).
syntax:
  content: 'public abstract class View : ISelectionContext, IDisposable'
seealso:
- linkId: DevExpress.ExpressApp.View._members
  altText: View Members
- linkId: "112607"
- linkId: "112611"
---
The [](xref:DevExpress.ExpressApp.View) class serves as the base for classes that are responsible for data representation and editing. Normally, you do not need to use this class directly. Instead, you will need to use its descendants - [](xref:DevExpress.ExpressApp.DashboardView), [](xref:DevExpress.ExpressApp.DetailView) and [](xref:DevExpress.ExpressApp.ListView). These are the actual classes used to display and edit objects in a UI.

You can access a [](xref:DevExpress.ExpressApp.View) via the [Frame.View](xref:DevExpress.ExpressApp.Frame.View) or [ViewController.View](xref:DevExpress.ExpressApp.ViewController.View) property.