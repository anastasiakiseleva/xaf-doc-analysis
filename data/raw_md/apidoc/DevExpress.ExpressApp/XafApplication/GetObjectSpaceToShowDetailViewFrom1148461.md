---
uid: DevExpress.ExpressApp.XafApplication.GetObjectSpaceToShowDetailViewFrom(DevExpress.ExpressApp.Frame,System.Type,DevExpress.ExpressApp.TargetWindow)
name: GetObjectSpaceToShowDetailViewFrom(Frame, Type, TargetWindow)
type: Method
summary: Returns an Object Space in which a [Detail View](xref:112611) should be created.
syntax:
  content: public virtual IObjectSpace GetObjectSpaceToShowDetailViewFrom(Frame sourceFrame, Type objectType, TargetWindow targetWindow)
  parameters:
  - id: sourceFrame
    type: DevExpress.ExpressApp.Frame
    description: A [](xref:DevExpress.ExpressApp.Frame) from which the **ShowView** method will be invoked.
  - id: objectType
    type: System.Type
    description: A [](xref:System.Type) object that is a type of object that will be supported by an Object Space.
  - id: targetWindow
    type: DevExpress.ExpressApp.TargetWindow
    description: ''
  return:
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) object representing the Object Space in which a Detail View should be created to be displayed via the **ShowView** method.
seealso: []
---
This method is used internally in **XAF**, and is not intended to be called from your code.