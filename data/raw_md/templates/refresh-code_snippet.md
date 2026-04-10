The following code snippet adds a new `Contact` object to a [List View](xref:112611#list-view) and refreshes the Object Space to show the new object.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
using MainDemo.Module.BusinessObjects;
// ...
public class AddContactController : ObjectViewController<ListView, Contact> {
    public AddContactController() {
        ParametrizedAction addContactAction = new ParametrizedAction(
            this, "AddContact", PredefinedCategory.Edit, typeof(string));
        addContactAction.Execute += AddContactAction_Execute;
    }
    private void AddContactAction_Execute(object sender, ParametrizedActionExecuteEventArgs e) {
        using(IObjectSpace objectSpace = Application.CreateObjectSpace(typeof(Contact))) {
            Contact contact = objectSpace.CreateObject<Contact>();
            contact.FirstName = e.ParameterCurrentValue as string;
            objectSpace.CommitChanges();
        }
        View.ObjectSpace.Refresh();
    }
}
```
***