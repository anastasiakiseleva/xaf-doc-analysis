---
uid: DevExpress.ExpressApp.View.CanClose
name: CanClose()
type: Method
summary: Determines whether a [](xref:DevExpress.ExpressApp.View) can be closed.
syntax:
  content: public bool CanClose()
  return:
    type: System.Boolean
    description: '**true** if the current View can be closed; otherwise, **false**.'
seealso:
- linkId: DevExpress.ExpressApp.View.Close*
- linkId: DevExpress.ExpressApp.View.Closed
- linkId: DevExpress.ExpressApp.Window.Close*
---
Use this method to check whether a View is allowed to be closed. If the current View is not root (it is created in another View's Object Space), this method returns **true**. Otherwise, it raises the [View.QueryCanClose](xref:DevExpress.ExpressApp.View.QueryCanClose) event and returns the opposite value of the handler's **CancelEventArgs.Cancel** parameter. Handle this event to prohibit closing a View under specific conditions.

This method is used internally, when closing a Window in a Windows Forms application and when replacing a View with another.