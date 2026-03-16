---
uid: DevExpress.ExpressApp.IObjectSpace.SetModified(System.Object,DevExpress.ExpressApp.DC.IMemberInfo)
name: SetModified(Object, IMemberInfo)
type: Method
summary: Sets the state of the specified object to be Modified and adds the passed object to the track list to be committed.
syntax:
  content: void SetModified(object obj, IMemberInfo memberInfo)
  parameters:
  - id: obj
    type: System.Object
    description: A persistent object whose state is the subject to be Modified.
  - id: memberInfo
    type: DevExpress.ExpressApp.DC.IMemberInfo
    description: An [](xref:DevExpress.ExpressApp.DC.IMemberInfo) object providing metadata on the property whose value has been changed.
seealso:
- linkId: DevExpress.ExpressApp.ListView.ObjectChanged
- linkId: "2077"
---
For object changes that cannot be tracked via notification mechanisms exposed by the data layer, use the **SetModified** method. This method adds the object passed as the _obj_ parameter to the list of objects to be committed

If you implement the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class' descendant, you don't have to override the **SetModified** method. This method is implemented in the **BaseObjectSpace** class. The [BaseObjectSpace.SetModified](xref:DevExpress.ExpressApp.BaseObjectSpace.SetModified*) method invokes a protected virtual **BaseObjectSpace.SetModified(Object obj, ObjectChangedEventArgs args)** method. So, you should override the virtual**CreateObjectCore** method. Use the _memberInfo_ parameter to specify the property that has been changed.

Note that you can raise the [IObjectSpace.ObjectChanged](xref:DevExpress.ExpressApp.IObjectSpace.ObjectChanged) event in your **BaseOBjectSpace.SetModified** method override. This event is handled internally, so that both a Detail View's Property Editor and a List View's [List Editor](xref:113189) will be refreshed if their object has changed.

The objects that are currently in the Modified state are available via the [IObjectSpace.ModifiedObjects](xref:DevExpress.ExpressApp.IObjectSpace.ModifiedObjects) property.