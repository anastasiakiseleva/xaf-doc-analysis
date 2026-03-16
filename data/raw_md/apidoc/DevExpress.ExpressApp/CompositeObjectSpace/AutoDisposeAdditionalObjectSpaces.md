---
uid: DevExpress.ExpressApp.CompositeObjectSpace.AutoDisposeAdditionalObjectSpaces
name: AutoDisposeAdditionalObjectSpaces
type: Property
summary: Specifies whether the current Object Space disposes of its inner Object Spaces from the @DevExpress.ExpressApp.CompositeObjectSpace.AdditionalObjectSpaces collection when it disposes itself.
syntax:
  content: public bool AutoDisposeAdditionalObjectSpaces { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: "**true**, if the current Object Space disposes of its inner Object Spaces from the @DevExpress.ExpressApp.CompositeObjectSpace.AdditionalObjectSpaces collection when it disposes itself; otherwise, **false**. The default value equals the @DevExpress.ExpressApp.CompositeObjectSpace.AutoDisposeAdditionalObjectSpacesByDefault static field's value."
seealso: []
---
Dispose of Object Spaces that you stopped using because undisposed Object Spaces may lead to memory leaks. Set this property to **true** to automatically dispose of all additional Object Spaces simultaneously with the parent Object Space. 

Refer to the following GitHub example to see how to use this property: [How to refresh Non-Persistent Objects and reload nested Persistent Objects](https://github.com/DevExpress-Examples/XAF_Non-Persistent-Objects-Reloading-Demo).
