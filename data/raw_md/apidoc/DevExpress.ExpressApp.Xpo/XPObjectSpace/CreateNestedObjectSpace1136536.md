---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpace.CreateNestedObjectSpace
name: CreateNestedObjectSpace()
type: Method
summary: Creates a nested Object Space.
syntax:
  content: public override IObjectSpace CreateNestedObjectSpace()
  return:
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) object that is a created nested Object Space.
seealso:
- linkId: DevExpress.Xpo.AggregatedAttribute
- linkId: DevExpress.Xpo.NestedUnitOfWork
---
Use this method to create a nested Object Space for the current Object Space. When committing the changes made within a nested Object Space, they are merged back into the parent Object Space. This allows treating several related operations as a single unified operation.

The code below demonstrates how you can use a nested Object Space to save a new **Task** object only if its **Contact** is saved.


# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.SystemModule;
using MainDemo.Module.BusinessObjects;
// ...

public class NewObjectController : ObjectViewController<ListView, DemoTask> {
    public NewObjectController() {
        TargetViewNesting = Nesting.Nested;
    }
    protected override void OnActivated() {
        NewObjectViewController controller = Frame.GetController<NewObjectViewController>();
        controller.ObjectCreating += Controller_ObjectCreating;
    }
    private void Controller_ObjectCreating(object sender, ObjectCreatingEventArgs e) {
        IObjectSpace objectSpace = View.ObjectSpace.CreateNestedObjectSpace();
        DemoTask task = objectSpace.CreateObject<DemoTask>();
        e.ObjectSpace = objectSpace;
        e.NewObject = task;
    }
}
```
***


By default, Nested Object Spaces are used for modal windows with detail views that represent aggregated objects (see [](xref:DevExpress.Xpo.AggregatedAttribute)). Aggregated objects are considered parts of their owner. When the owner is deleted, its aggregated objects are automatically deleted. Similarly, when the owner is saved, its aggregated objects are also saved. Using nested Object Spaces to represent aggregated object views allows the user to edit these objects in separate windows and choose whether to save or cancel changes (in memory) without immediately saving the owner object. For example:

* **Object Property Editor**
    
    This editor has an ellipsis button that opens a dialog representing the referenced object. This dialog contains a Detail View created in a nested Object Space.
    
    ![NestedObjectSpace](~/images/nestedobjectspace115616.png)
    
    This editor is suitable for Address type properties. For instance, each Person object has a unique Address. It is convenient to edit the Address object in a separate form, but commit changes together with the owner Person object. Using a nested Object Space in this scenario allows treating Person and Address object modifications as a single operation.
* **Modal Detail View**
    
    A Modal Detail View is usually opened for a new object created using the New action or an object selected in a nested List View that represents an Aggregated Collection. The nested Object Space is used to create this Detail View.
    
    ![OpenDetailViewFromAggregatedListView](~/images/opendetailviewfromaggregatedlistview132164.png)
    
    This is a typical and recommended implementation for a nested collection of objects that are unique for each owner. For instance, an aggregated collection of Phone Numbers owned by a Person.


Nested Object Spaces are implemented based on **Nested Units of Work** and inherit their behavior and specifics. Refer to the [Nested Units of Work](xref:DevExpress.Xpo.NestedUnitOfWork) documentation for details.