---
uid: DevExpress.ExpressApp.CloneObject.CloneObjectViewController.CustomShowClonedObject
name: CustomShowClonedObject
type: Event
summary: Occurs before XAF displays the Detail View of the cloned object.
syntax:
  content: public event EventHandler<CustomShowClonedObjectEventArgs> CustomShowClonedObject
seealso: []
---
XAF displays the Detail View of the cloned object after cloning. Handle this event to implement the custom code to be executed before or instead of displaying the Detail View. Set the handler's `Handled` parameter to `true` to prohibit displaying the Detail View.

[!include[customshowclonedobjectcode](~/templates/customshowclonedobjectcode.md)]