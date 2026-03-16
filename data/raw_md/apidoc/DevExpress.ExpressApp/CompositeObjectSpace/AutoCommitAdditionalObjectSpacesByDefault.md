---
uid: DevExpress.ExpressApp.CompositeObjectSpace.AutoCommitAdditionalObjectSpacesByDefault
name: AutoCommitAdditionalObjectSpacesByDefault
type: Field
summary: Specifies whether an Object Space's @DevExpress.ExpressApp.IObjectSpace.CommitChanges method forces [additional Object Spaces](xref:DevExpress.ExpressApp.CompositeObjectSpace.AdditionalObjectSpaces) to commit their changed objects. When this property is set to **true**, changes to objects that belong to additional Object Spaces mark the Object Space as [modified](xref:DevExpress.ExpressApp.IObjectSpace.IsModified). This field affects all Object Spaces in your application if you do not specify the @DevExpress.ExpressApp.CompositeObjectSpace.AutoCommitAdditionalObjectSpaces property for a particular Object Space.
syntax:
  content: public static bool AutoCommitAdditionalObjectSpacesByDefault
  return:
    type: System.Boolean
    description: "**true**, if an Object Space's @DevExpress.ExpressApp.IObjectSpace.CommitChanges method forces [additional Object Spaces](xref:DevExpress.ExpressApp.CompositeObjectSpace.AdditionalObjectSpaces) to commit their changed persistent objects; otherwise, **false**."
seealso:
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/XAF_Non-Persistent-Objects-Edit-Linked-Persistent-Objects-Demo
  altText: How to edit a collection of Persistent Objects linked to a Non-Persistent Object
---
