---
uid: DevExpress.ExpressApp.ListView.CurrentObject
name: CurrentObject
type: Property
summary: Specifies a List View's current object.
syntax:
  content: public override object CurrentObject { get; set; }
  parameters: []
  return:
    type: System.Object
    description: An **Object** representing the current List View's current object.
seealso:
- linkType: HRef
  linkId: DevExpress.ExpressApp.DetailView.CurrentObject
  altText: DetailView.CurrentObject
- linkType: HRef
  linkId: DevExpress.ExpressApp.View.CurrentObject
  altText: View.CurrentObject
- linkType: HRef
  linkId: DevExpress.ExpressApp.ListView.SelectedObjects
  altText: ListView.SelectedObjects
---
The example below demonstrates how to assign a **Contact**'s **FirstName** value to the **NickName** property via a @DevExpress.ExpressApp.Actions.SimpleAction only in [List Views](xref:112611#list-view).


# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
using MainDemo.Module.BusinessObjects;
// ...
public class SetNickNameController : ViewController<ListView> {
    public SetNickNameController() {
        SimpleAction setNickNameAction = new SimpleAction(this, "SetNickName", PredefinedCategory.Edit);
        setNickNameAction.Execute += SetNickNameAction_Execute;
    }
    private void SetNickNameAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
        Contact currentObject = View.CurrentObject as Contact;
        if(currentObject != null) {
            currentObject.NickName = currentObject.FirstName;
        }
    }
}
```
***

Use this property to access the focused object of the current List View's [ListView.Editor](xref:DevExpress.ExpressApp.ListView.Editor). If the focused object changes, the [View.CurrentObjectChanged](xref:DevExpress.ExpressApp.View.CurrentObjectChanged) event is raised.

When a List View is displayed in the **ListViewAndDetailView** mode ([IModelListView.MasterDetailMode](xref:DevExpress.ExpressApp.Model.IModelListView.MasterDetailMode)), the object specified by the **CurrentObject** property is displayed in the accompanying Detail View.

For additional information, refer to the [How to: Access Objects Selected in the Current View](xref:113324) help topic.