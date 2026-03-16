---
uid: DevExpress.ExpressApp.View.QueryCanClose
name: QueryCanClose
type: Event
summary: Occurs when checking whether a View can be closed.
syntax:
  content: public event EventHandler<CancelEventArgs> QueryCanClose
seealso: []
---
The `QueryCanClose` event is raised from [View.CanClose](xref:DevExpress.ExpressApp.View.CanClose) and [View.Close](xref:DevExpress.ExpressApp.View.Close*) methods. To keep the View open, handle the event and set the `CancelEventArgs.Cancel` parameter to `true`. 

> [!NOTE]
> The `QueryCanClose` event is raised for [root views](xref:DevExpress.ExpressApp.View.IsRoot) only.  
> [!include[event to prohibit view closing in aspnet core blazor apps](~/templates/event to prohibit view closing in aspnet core blazor apps.md)]