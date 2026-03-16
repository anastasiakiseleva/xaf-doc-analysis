---
uid: DevExpress.ExpressApp.CloneObject.CloneObjectViewController.CustomGetCloneActionTargetTypes
name: CustomGetCloneActionTargetTypes
type: Event
summary: Occurs before getting the target types list available via the [CloneObjectViewController.CloneObjectAction](xref:DevExpress.ExpressApp.CloneObject.CloneObjectViewController.CloneObjectAction).
syntax:
  content: public event EventHandler<CustomGetCloneActionTargetTypesEventArgs> CustomGetCloneActionTargetTypes
seealso: []
---
Handle the `CustomGetCloneActionTargetTypes` event to add custom target types via the handler's `TargetTypes` property. To prohibit adding the default target types, set the handler's `Handled` parameter to `true`.

The **CloneObject** [Action](xref:112622)'s [ChoiceActionBase.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.Items) collection includes the current object type and types inherited from the current object's base class. To get a list of these types in a `CustomGetCloneActionTargetTypes` handler, use the [CustomGetCloneActionTargetTypesEventArgs.GetDefaultTargetTypes](xref:DevExpress.ExpressApp.CloneObject.CustomGetCloneActionTargetTypesEventArgs.GetDefaultTargetTypes) method.

The following code prohibits adding descendant types of the current object type's base type to the Action's [ChoiceActionBase.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.Items) collection:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.CloneObject;
//...
public class MyCloneObjectController : CloneObjectViewController {
    // ...
    protected override void OnActivated() {
        this.CustomGetCloneActionTargetTypes += 
            MyCloneObjectController_CustomGetCloneActionTargetTypes;
        base.OnActivated();
    }
    private void MyCloneObjectController_CustomGetCloneActionTargetTypes(
        object sender, CustomGetCloneActionTargetTypesEventArgs e) {
        e.Handled = true;
        e.TargetTypes.Clear();
        e.TargetTypes.Add(
            Application.Model.BOModel[View.ObjectTypeInfo.Type.FullName],
            View.ObjectTypeInfo.Type);
    }
}
```
***

If you implement this Controller, the **CloneObject** Action will clone the currently selected object to the object of the same type, because only the Action's Item will be the current object type. Note, that you subscribe to the `CustomGetCloneActionTargetTypes` event before XAF calls the base `OnActivated` method. This is necessary because `CustomGetCloneActionTargetTypes` is raised from `OnActivated`. If you want to handle this event from a Controller that is not inherited from the [](xref:DevExpress.ExpressApp.CloneObject.CloneObjectViewController), subscribe in the `OnFrameAssigned` method.

To manually fill the Items of the **CloneObject** Action, access this Action in the Controller's `OnActivated` method. For more information, refer to the [CloneObjectViewController.CloneObjectAction](xref:DevExpress.ExpressApp.CloneObject.CloneObjectViewController.CloneObjectAction) topic.