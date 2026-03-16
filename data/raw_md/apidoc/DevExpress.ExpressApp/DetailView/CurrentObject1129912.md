---
uid: DevExpress.ExpressApp.DetailView.CurrentObject
name: CurrentObject
type: Property
summary: Specifies an object displayed by the Detail View.
syntax:
  content: public override object CurrentObject { get; set; }
  parameters: []
  return:
    type: System.Object
    description: An **Object** displayed by the Detail View.
seealso:
- linkType: HRef
  linkId: DevExpress.ExpressApp.ListView.CurrentObject
  altText: ListView.CurrentObject
- linkType: HRef
  linkId: DevExpress.ExpressApp.DetailView.SelectedObjects
  altText: DetailView.SelectedObjects
---
The example below demonstrates how to assign a **Contact**'s **FirstName** value to the **NickName** property via a @DevExpress.ExpressApp.Actions.SimpleAction only in [Detail Views](xref:112611#detail-view).

# [C#](#tab/tabid-csharp)
```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
using MainDemo.Module.BusinessObjects;
// ...
public class SetNickNameController : ViewController<DetailView> {
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

By default, this property is set to the object that was passed in the Detail View constructor. You can change it. This will raise the [View.SelectionChanged](xref:DevExpress.ExpressApp.View.SelectionChanged), [View.CaptionChanged](xref:DevExpress.ExpressApp.View.CaptionChanged) and [View.CurrentObjectChanged](xref:DevExpress.ExpressApp.View.CurrentObjectChanged) events one after another.

For additional information, refer to the [How to: Access Objects Selected in the Current View](xref:113324) help topic.