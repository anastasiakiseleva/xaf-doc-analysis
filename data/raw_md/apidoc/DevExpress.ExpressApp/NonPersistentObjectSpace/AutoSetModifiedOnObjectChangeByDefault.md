---
uid: DevExpress.ExpressApp.NonPersistentObjectSpace.AutoSetModifiedOnObjectChangeByDefault
name: AutoSetModifiedOnObjectChangeByDefault
type: Field
summary: Specifies whether non-persistent Object Spaces add objects to the @DevExpress.ExpressApp.NonPersistentObjectSpace.ModifiedObjects collection when these objects raise the @System.ComponentModel.INotifyPropertyChanged.PropertyChanged event. This field affects all non-persistent Object Spaces in your application if you do not specify the @DevExpress.ExpressApp.NonPersistentObjectSpace.AutoSetModifiedOnObjectChange property for a particular Object Space.
syntax:
  content: public static bool AutoSetModifiedOnObjectChangeByDefault
  return:
    type: System.Boolean
    description: '**true**, if non-persistent Object Spaces add objects to the @DevExpress.ExpressApp.NonPersistentObjectSpace.ModifiedObjects collection when these objects raise the @System.ComponentModel.INotifyPropertyChanged.PropertyChanged event; otherwise, **false**.'
seealso: []
---
Use this field to track modifications of [non-persistent objects](xref:116516) that implement the @System.ComponentModel.INotifyPropertyChanged interface.

Refer to the following GitHub example to see how to use this property: [How to implement CRUD operations for Non-Persistent Objects stored remotely](https://github.com/DevExpress-Examples/XAF-CRUD-for-Non-Persistent-Objects-Stored-Remotely).