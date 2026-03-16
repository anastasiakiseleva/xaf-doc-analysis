---
uid: DevExpress.ExpressApp.NonPersistentObjectSpace.AutoSetModifiedOnObjectChange
name: AutoSetModifiedOnObjectChange
type: Property
summary: Specifies whether the current non-persistent Object Space adds objects to the @DevExpress.ExpressApp.NonPersistentObjectSpace.ModifiedObjects collection when they raise the @System.ComponentModel.INotifyPropertyChanged.PropertyChanged event.
syntax:
  content: public bool AutoSetModifiedOnObjectChange { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: "**true**, if the current non-persistent Object Space adds objects to the @DevExpress.ExpressApp.NonPersistentObjectSpace.ModifiedObjects collection when they raise the @System.ComponentModel.INotifyPropertyChanged.PropertyChanged event; otherwise, **false**. The default value equals the @DevExpress.ExpressApp.NonPersistentObjectSpace.AutoSetModifiedOnObjectChangeByDefault static field's value."
seealso:
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/XAF-CRUD-for-Non-Persistent-Objects-Stored-Remotely
  altText: How to implement CRUD operations for Non-Persistent Objects stored remotely
---
Use this property to track modifications of [non-persistent objects](xref:116516) that implement the @System.ComponentModel.INotifyPropertyChanged interface.
