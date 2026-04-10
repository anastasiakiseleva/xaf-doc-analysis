The following code deactivates the sibling cloning functionality. Descendant types of the current object's ancestor do not appear in the Action's [ChoiceActionBase.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.Items) collection:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.CloneObject;
//...

namespace YourApplicationName.Module.Controllers;

public partial class MyCloneObjectController : ViewController {
    //...
    protected override void OnActivated() {
        base.OnActivated();
        CloneObjectViewController cloneObjectController =
            Frame.GetController<CloneObjectViewController>();
        if (cloneObjectController != null) {
            cloneObjectController.CloneObjectAction.Items.Clear();
            ChoiceActionItem myItem =
                new ChoiceActionItem(View.ObjectTypeInfo.Name, View.ObjectTypeInfo.Type);
            myItem.ImageName =
                Application.Model.BOModel.GetNode<IModelClass>(View.ObjectTypeInfo.FullName).ImageName;
            cloneObjectController.CloneObjectAction.Items.Add(myItem);
        }
    }
}
```
***

If you implement this Controller, the **CloneObject** Action clones the selected object to the object of the same type because the Action's Item will be the current object type. To manually fill the Items of the **CloneObjectAction**, handle the [CloneObjectViewController.CustomGetCloneActionTargetTypes](xref:DevExpress.ExpressApp.CloneObject.CloneObjectViewController.CustomGetCloneActionTargetTypes) event. For more information, refer to the event's description.