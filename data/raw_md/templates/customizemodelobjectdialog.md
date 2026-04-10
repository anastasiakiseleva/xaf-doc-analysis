### Customize the Object Model Dialog

You can make a column invisible in List View and Detail View Object Model dialogs. Use [`HideInUI.ListViewCustomziationForm`](xref:DevExpress.Persistent.Base.HideInUI.ListViewCustomizationForm) and [`HideInUI.DetailViewCustomizationForm`](xref:DevExpress.Persistent.Base.HideInUI.DetailViewCustomizationForm) attributes respectively.

To specify property visibility in the **Object Model** dialog, override the `ObjectModelController`. For example, the following code snippet filters out all key properties:

```csharp{11,16}
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Components;
using DevExpress.ExpressApp.Blazor.SystemModule;
namespace YourApplicationName.Blazor.Server.Controllers;

public class CustomizeObjectDialogController : ViewController<DetailView> {
    ObjectModelController objectModelController;
    protected override void OnActivated() {
        base.OnActivated();
        objectModelController = Frame.GetController<ObjectModelController>();
        objectModelController.CustomizePropertyVisibility += ObjectModelController_CustomizePropertyVisibility;
    }

    private void ObjectModelController_CustomizePropertyVisibility(object sender, CustomizePropertyVisibilityEventArgs e) {
        if(e.MemberInfo.Owner.KeyMember == e.MemberInfo) {
            e.Visible = false;
        }
    }

    protected override void OnDeactivated() {
        base.OnDeactivated();
        if(objectModelController != null) {
            objectModelController.CustomizePropertyVisibility -= ObjectModelController_CustomizePropertyVisibility;
            objectModelController = null;
        }
    }
}
```