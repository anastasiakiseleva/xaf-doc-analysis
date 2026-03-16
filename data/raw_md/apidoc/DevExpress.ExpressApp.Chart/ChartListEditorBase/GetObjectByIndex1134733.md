---
uid: DevExpress.ExpressApp.Chart.ChartListEditorBase.GetObjectByIndex(System.Int32)
name: GetObjectByIndex(Int32)
type: Method
summary: Returns an object that represents the [](xref:DevExpress.ExpressApp.Chart.ChartListEditorBase)'s point with the specified index.
syntax:
  content: public object GetObjectByIndex(int index)
  parameters:
  - id: index
    type: System.Int32
    description: The index of an object that represents the Charting List Editor's point.
  return:
    type: System.Object
    description: The object that represents the Charting List Editor's point with the specified index.
seealso: []
---
This method is not intended to be called from your code. It is implemented as a part of the **IControlOrderProvider** interface. The [](xref:DevExpress.ExpressApp.Chart.ChartListEditorBase) implements this interface to support the [](xref:DevExpress.ExpressApp.SystemModule.RecordsNavigationController)'s [Actions](xref:112622) for the [Views](xref:112611) that use **ChartListEditorBase** descendants.