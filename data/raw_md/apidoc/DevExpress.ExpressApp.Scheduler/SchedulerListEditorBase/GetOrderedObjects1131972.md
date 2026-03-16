---
uid: DevExpress.ExpressApp.Scheduler.SchedulerListEditorBase.GetOrderedObjects
name: GetOrderedObjects()
type: Method
summary: Returns an ordered list of objects that represent the **Scheduler**'s Events.
syntax:
  content: public IList GetOrderedObjects()
  return:
    type: System.Collections.IList
    description: An ordered list of objects that represent the **Scheduler**'s Events.
seealso: []
---
This method is not intended to be called from your code. It is implemented as a part of the **IControlOrderProvider** interface. The [](xref:DevExpress.ExpressApp.Scheduler.SchedulerListEditorBase) implements this interface to support the [](xref:DevExpress.ExpressApp.SystemModule.RecordsNavigationController)'s [Actions](xref:112622) for the [Views](xref:112611) that use **SchedulerListEditorBase** descendants.