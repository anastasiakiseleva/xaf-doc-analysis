---
uid: DevExpress.ExpressApp.BaseObjectSpace.SetModified(System.Object)
name: SetModified(Object)
type: Method
summary: Sets the state of the specified object to be Modified.
syntax:
  content: public void SetModified(object obj)
  parameters:
  - id: obj
    type: System.Object
    description: A persistent object whose state is the subject to be Modified.
seealso: []
---
Generally, the changes made to persistent object properties are tracked, to then be committed (see [BaseObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.BaseObjectSpace.CommitChanges)). For the object changes that cannot be tracked internally, use the **SetModified** method. This method calls a protected virtual **SetModified** method, which must be implemented in the **BaseObjectSpace** class' descendants.

The following code demonstrates how the MyViewController's Delete Action removes the selected objects in nested List Views:

# [C#](#tab/tabid-csharp)

```csharp
public partial class MyViewController : ViewController {
   //...
   private void MyViewController_AfterConstruction(object sender, EventArgs e) {
      this.deleteAction.TargetViewNesting = DevExpress.ExpressApp.Nesting.Nested;
      this.deleteAction.TargetViewType = DevExpress.ExpressApp.ViewType.ListView;
   }
   private void deleteAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
      foreach(object obj in View.SelectedObjects) {
         (View as ListView).CollectionSource.Remove(obj);
         (View as ListView).CollectionSource.ObjectSpace.SetModified(obj);
      }
   }
}
```
***

When executing the Delete Action demonstrated above, the selected objects will be marked as objects to be deleted and the nested List View's editor will be refreshed. Since nested List Views are created in the parent Detail View's Object Space, the deleted objects will actually be removed when executing the Detail View's Save or SaveAndClose Action.