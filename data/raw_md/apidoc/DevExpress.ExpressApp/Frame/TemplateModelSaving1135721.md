---
uid: DevExpress.ExpressApp.Frame.TemplateModelSaving
name: TemplateModelSaving
type: Event
summary: Occurs before synchronizing information on a [](xref:DevExpress.ExpressApp.Frame)'s [Template](xref:112609).
syntax:
  content: public event EventHandler<CancelEventArgs> TemplateModelSaving
seealso:
- linkId: DevExpress.ExpressApp.Frame.ViewModelSaving
- linkId: DevExpress.ExpressApp.View.SaveModel
- linkId: DevExpress.ExpressApp.View.ModelSaving
---
The **TemplateModelSaving** event is raised when attempting to write information on the current Frame's [Frame.Template](xref:DevExpress.ExpressApp.Frame.Template) to the [Application Model](xref:112580). If you need to prohibit writing, set the **CancelEventArgs.Cancel** parameter to **true**.

> [!NOTE]
> Synchronization is performed in Windows Forms applications when closing a Window.