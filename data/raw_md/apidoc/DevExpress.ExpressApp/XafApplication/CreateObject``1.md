---
uid: DevExpress.ExpressApp.XafApplication.CreateObject``1(DevExpress.ExpressApp.IObjectSpace@)
name: CreateObject<T>(out IObjectSpace)
type: Method
summary: Creates an object of the type designated by the generic type parameter.
syntax:
  content: public T CreateObject<T>(out IObjectSpace objectSpace)
  parameters:
  - id: objectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: A variable that stores the [](xref:DevExpress.ExpressApp.IObjectSpace) used to create the intended object.
  typeParameters:
  - id: T
    description: ''
  return:
    type: '{T}'
    description: Object type.
seealso: []
---
The following code demonstrates how to implement a Simple Action that creates a new object of the specified type:

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
using dxTestSolution.Module.BusinessObjects;

public class CustomWinController : ViewController {
    public CustomWinController() {
        var myAction1 = new SimpleAction(this, "MyWinAction1", PredefinedCategory.Edit);
        myAction1.Execute += MyAction1_Execute;
    }

    private void MyAction1_Execute(object sender, SimpleActionExecuteEventArgs e) {
        var newContact = Application.CreateObject<Contact>(out IObjectSpace createdOS);
        newContact.FirstName = "contactName";
        createdOS.CommitChanges();
    }
}
```