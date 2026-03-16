---
uid: DevExpress.ExpressApp.Actions.PopupWindowShowAction
name: PopupWindowShowAction
type: Class
summary: Represents a Pop-up Window Show Action.
syntax:
  content: 'public class PopupWindowShowAction : ActionBase'
seealso:
- linkId: DevExpress.ExpressApp.Actions.PopupWindowShowAction._members
  altText: PopupWindowShowAction Members
- linkId: "117231"
---
The **PopupWindowShowAction** class inherits the basic functionality of [Actions](xref:112622) from the [](xref:DevExpress.ExpressApp.Actions.ActionBase) class. Pop-up Window Show Actions are used to invoke a pop-up [Window](xref:112608) with a specified [View](xref:112611) and execute custom code when an end-user clicks the accept or cancel button. To specify the View to be displayed, handle the [PopupWindowShowAction.CustomizePopupWindowParams](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction.CustomizePopupWindowParams) event and set the required View to the handler's [CustomizePopupWindowParamsEventArgs.View](xref:DevExpress.ExpressApp.Actions.CustomizePopupWindowParamsEventArgs.View) parameter. An example of using this approach is shown below.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.Editors;
using DevExpress.Persistent.Base;
// ...
public class ShowPopupViewController : ObjectViewController<ObjectView, Contact> {
    public ShowPopupViewController() {
        var popupAction = new PopupWindowShowAction(this, "ShowPopup", PredefinedCategory.View);
        popupAction.SelectionDependencyType = SelectionDependencyType.RequireSingleObject;
        popupAction.CustomizePopupWindowParams += PopupAction_CustomizePopupWindowParams;
    }
    private void PopupAction_CustomizePopupWindowParams(object sender, CustomizePopupWindowParamsEventArgs e) {
        IObjectSpace objectSpace = e.Application.CreateObjectSpace(typeof(Contact));
        Contact currentObject = objectSpace.GetObject(ViewCurrentObject);
        DetailView detailView = e.Application.CreateDetailView(objectSpace, currentObject);
        detailView.ViewEditMode = ViewEditMode.Edit;
        e.View = detailView;
        e.Maximized = true;
    }
}

```
***

In the code above, the new [](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction) object is created to invoke a pop-up window for the particular **View** when the [PopupWindowShowAction.CustomizePopupWindowParams](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction.CustomizePopupWindowParams) event raises. The [CustomizePopupWindowParamsEventArgs.Maximized](xref:DevExpress.ExpressApp.Actions.CustomizePopupWindowParamsEventArgs.Maximized) property is set to **true**, thus the pop-up window will expand to occupy the whole space.

To process end-user clicks on the accept and cancel buttons, handle the [PopupWindowShowAction.Execute](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction.Execute) and [PopupWindowShowAction.Cancel](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction.Cancel) events, respectively. Built-in [Action Containers](xref:112610) display Pop-up Window Show Actions via a button.

To add a Pop-up Window Show Action to a [Controller](xref:112621), drag and drop the **PopupWindowShowAction** item from the **XAF Actions** section on the **Toolbox** to the required Controller's **Designer** area (see [](xref:402158)).  You can also use the [](xref:DevExpress.Persistent.Base.ActionAttribute) to convert a business class' method to an Action that displays a [non-persistent object](xref:116516) in a popup (see [How to: Create an Action Using the Action Attribute](xref:112619)).

[!include[coderush-templates-actions-controllers](~/templates/coderush-templates-actions-controllers.md)]

Unlike other Action types, the [](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction) does not raise the [ActionBase.ProcessCreatedView](xref:DevExpress.ExpressApp.Actions.ActionBase.ProcessCreatedView) event. This is because such an Action creates a View before the **Executed** event is raised.