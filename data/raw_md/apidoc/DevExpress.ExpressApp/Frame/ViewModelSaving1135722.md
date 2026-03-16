---
uid: DevExpress.ExpressApp.Frame.ViewModelSaving
name: ViewModelSaving
type: Event
summary: Occurs before synchronizing information on a [](xref:DevExpress.ExpressApp.Frame)'s [View](xref:112611).
syntax:
  content: public event EventHandler<CancelEventArgs> ViewModelSaving
seealso:
- linkId: DevExpress.ExpressApp.Frame.TemplateModelSaving
- linkId: DevExpress.ExpressApp.View.SaveModel
- linkId: DevExpress.ExpressApp.View.ModelSaving
---
The **ViewModelSaving** event is raised when attempting to write information on the current Frame's [Frame.View](xref:DevExpress.ExpressApp.Frame.View) to the [Application Model](xref:112580). If you need to prohibit writing, set the handler's **CancelEventArgs.Cancel** parameter to **true**. By default this parameter is set to **false**.

> [!NOTE]
> Synchronization is performed in Windows Forms applications when closing a Window.