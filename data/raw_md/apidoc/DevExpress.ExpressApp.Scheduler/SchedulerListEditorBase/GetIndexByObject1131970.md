---
uid: DevExpress.ExpressApp.Scheduler.SchedulerListEditorBase.GetIndexByObject(System.Object)
name: GetIndexByObject(Object)
type: Method
summary: Returns the index of an object that represents the **Scheduler**'s Event.
syntax:
  content: public int GetIndexByObject(object obj)
  parameters:
  - id: obj
    type: System.Object
    description: An object that represents the **Scheduler**'s Event.
  return:
    type: System.Int32
    description: An index of an object that represents the **Scheduler**'s Event.
seealso: []
---
This method is not intended to be called from your code. It is implemented as a part of the **IControlOrderProvider** interface. The [](xref:DevExpress.ExpressApp.Scheduler.SchedulerListEditorBase) implements this interface to support the [](xref:DevExpress.ExpressApp.SystemModule.RecordsNavigationController)'s [Actions](xref:112622) for the [Views](xref:112611) that use **SchedulerListEditorBase** descendants.