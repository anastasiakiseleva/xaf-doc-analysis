---
uid: DevExpress.ExpressApp.CompositeObjectSpace.AutoRefreshAdditionalObjectSpaces
name: AutoRefreshAdditionalObjectSpaces
type: Property
summary: Specifies whether the current Object Space refreshes its inner Object Spaces from the @DevExpress.ExpressApp.CompositeObjectSpace.AdditionalObjectSpaces collection when it refreshes itself.
syntax:
  content: public bool AutoRefreshAdditionalObjectSpaces { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: "**true**, if the current Object Space refreshes its inner Object Spaces from the @DevExpress.ExpressApp.CompositeObjectSpace.AdditionalObjectSpaces collection when it refreshes itself; otherwise, **false**. The default value equals the @DevExpress.ExpressApp.CompositeObjectSpace.AutoRefreshAdditionalObjectSpacesByDefault static field's value."
seealso: []
---
If a non-persistent object contains a reference to or a collection of persistent objects, you need to refresh their Object Space after refreshing the parent non-persistent Object Space. Set this property to **true** to do this automatically each time the non-persistent Object Space refreshes.

After refreshing, drop all references and collections of outdated persistent objects and create new instances in refreshed persistent Object Spaces. Also, you can drop the non-persistent object with persistent objects it references and create a new instance again in the [ObjectsGetting](xref:DevExpress.ExpressApp.NonPersistentObjectSpace.ObjectsGetting), [ObjectGetting](xref:DevExpress.ExpressApp.NonPersistentObjectSpace.ObjectGetting), and [ObjectByKeyGetting](xref:DevExpress.ExpressApp.NonPersistentObjectSpace.ObjectByKeyGetting) event handlers.

Refer to the following GitHub example to see how to use this property: [How to refresh Non-Persistent Objects and reload nested Persistent Objects](https://github.com/DevExpress-Examples/XAF_Non-Persistent-Objects-Reloading-Demo).
