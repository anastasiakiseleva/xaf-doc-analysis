---
uid: DevExpress.ExpressApp.Actions.PopupWindowShowActionExecuteEventArgs
name: PopupWindowShowActionExecuteEventArgs
type: Class
summary: Represents arguments passed to a Pop-up Window Show Action's [PopupWindowShowAction.Execute](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction.Execute) event.
syntax:
  content: 'public class PopupWindowShowActionExecuteEventArgs : SimpleActionExecuteEventArgs'
seealso:
- linkId: DevExpress.ExpressApp.Actions.PopupWindowShowActionExecuteEventArgs._members
  altText: PopupWindowShowActionExecuteEventArgs Members
---
The [](xref:DevExpress.ExpressApp.Actions.PopupWindowShowActionExecuteEventArgs) class declares properties specific to the [PopupWindowShowAction.Execute](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction.Execute) event. This event is designed to execute custom code when clicking the accept button on a Pop-up Window Show Action's pop-up [Window](xref:112608). You can handle this event to execute custom code and specify whether to close the pop-up window.

This class is inherited from the [](xref:DevExpress.ExpressApp.Actions.SimpleActionExecuteEventArgs) class. Use the inherited [SimpleActionExecuteEventArgs.CurrentObject](xref:DevExpress.ExpressApp.Actions.SimpleActionExecuteEventArgs.CurrentObject) and [SimpleActionExecuteEventArgs.SelectedObjects](xref:DevExpress.ExpressApp.Actions.SimpleActionExecuteEventArgs.SelectedObjects) properties to access the current and selected objects of the pop-up window's parent [View](xref:112611). Use the [PopupWindowShowActionExecuteEventArgs.PopupWindowViewCurrentObject](xref:DevExpress.ExpressApp.Actions.PopupWindowShowActionExecuteEventArgs.PopupWindowViewCurrentObject) and [PopupWindowShowActionExecuteEventArgs.PopupWindowViewSelectedObjects](xref:DevExpress.ExpressApp.Actions.PopupWindowShowActionExecuteEventArgs.PopupWindowViewSelectedObjects) properties to access the current and selected objects of the View displayed within the pop-up Window. To access the popup Window itself, use the [PopupWindowShowActionExecuteEventArgs.PopupWindow](xref:DevExpress.ExpressApp.Actions.PopupWindowShowActionExecuteEventArgs.PopupWindow) property.