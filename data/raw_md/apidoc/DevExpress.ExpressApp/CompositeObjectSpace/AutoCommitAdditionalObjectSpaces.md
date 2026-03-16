---
uid: DevExpress.ExpressApp.CompositeObjectSpace.AutoCommitAdditionalObjectSpaces
name: AutoCommitAdditionalObjectSpaces
type: Property
summary: Specifies whether the current Object Space's @DevExpress.ExpressApp.IObjectSpace.CommitChanges method forces [additional Object Spaces](xref:DevExpress.ExpressApp.CompositeObjectSpace.AdditionalObjectSpaces) to commit their changed objects. When this property is set to **true**, changes to objects that belong to additional Object Spaces mark the Object Space as [modified](xref:DevExpress.ExpressApp.IObjectSpace.IsModified).
syntax:
  content: public bool AutoCommitAdditionalObjectSpaces { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: "**true** if the current Object Space's @DevExpress.ExpressApp.IObjectSpace.CommitChanges method forces [additional Object Spaces](xref:DevExpress.ExpressApp.CompositeObjectSpace.AdditionalObjectSpaces) to commit their changed objects; otherwise, **false**."
seealso: []
---
Refer to the following GitHub example to see how to use this property: [How to refresh Non-Persistent Objects and reload nested Persistent Objects](https://github.com/DevExpress-Examples/XAF_Non-Persistent-Objects-Edit-Linked-Persistent-Objects-Demo).