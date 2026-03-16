---
uid: DevExpress.ExpressApp.Actions.PopupWindowShowAction.CustomizePopupWindowParams
name: CustomizePopupWindowParams
type: Event
summary: Occurs when generating a pop-up [Window](xref:112608) for a Pop-up Window Show Action.
syntax:
  content: public event CustomizePopupWindowParamsEventHandler CustomizePopupWindowParams
seealso: []
---
Handle this event to specify a [View](xref:112611) for a @DevExpress.ExpressApp.Actions.PopupWindowShowAction to show. For this purpose, use the handler's  [CustomizePopupWindowParamsEventArgs.View](xref:DevExpress.ExpressApp.Actions.CustomizePopupWindowParamsEventArgs.View) parameter. You can also use the [CustomizePopupWindowParamsEventArgs.IsSizeable](xref:DevExpress.ExpressApp.Actions.CustomizePopupWindowParamsEventArgs.IsSizeable) property, to specify the pop-up Window's ability to be sizable.

The following example creates a [List View](xref:112611#list-view) and displays it via a @DevExpress.ExpressApp.Actions.PopupWindowShowAction.

# [C#](#tab/tabid-csharp)

```csharp
using System;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
// ...
public class ShowListViewController : ViewController {
    public ShowListViewController() {
        PopupWindowShowAction showListViewAction = new PopupWindowShowAction(this, "ShowListView",
            PredefinedCategory.Edit);
        showListViewAction.CustomizePopupWindowParams += ShowListViewAction_CustomizePopupWindowParams;
    }
    private void ShowListViewAction_CustomizePopupWindowParams(object sender, CustomizePopupWindowParamsEventArgs e) {
        Type objectType = typeof(Person);
        e.View = Application.CreateListView(objectType, true);
    }
}
```
***