---
uid: DevExpress.ExpressApp.IObjectSpace.SetModified(System.Object)
name: SetModified(Object)
type: Method
summary: Sets the state of the specified object to _Modified_ and adds this object to the track list of changes that should be committed.
syntax:
  content: void SetModified(object obj)
  parameters:
  - id: obj
    type: System.Object
    description: A persistent object whose _IsModified_ state should be changed.
seealso:
- linkId: DevExpress.ExpressApp.ListView.ObjectChanged
- linkId: "2077"
---
If a data layer notification mechanism cannot track object changes, use the **SetModified** method. This method adds the object to the list of changes that should be committed.

In the @DevExpress.ExpressApp.BaseObjectSpace descendant, the [BaseObjectSpace.SetModified](xref:DevExpress.ExpressApp.BaseObjectSpace.SetModified*) method invokes the **BaseObjectSpace.SetModified(Object obj, ObjectChangedEventArgs args)** method. To change the object's _IsModified_ state, override the **CreateObjectCore(Type type)** method and return a new object of the type passed as the parameter. 

You can raise the [IObjectSpace.ObjectChanged](xref:DevExpress.ExpressApp.IObjectSpace.ObjectChanged) event in your **BaseObjectSpace.SetModified** method override. The **ObjectChanged** event handler updates a Detail View's Property Editor and a List View's [List Editor](xref:113189) when their objects are changed.

The [IObjectSpace.ModifiedObjects](xref:DevExpress.ExpressApp.IObjectSpace.ModifiedObjects) property contains objects in the _Modified_ state. 

[!include[](~/templates/setmodified_code_snippet.md)]