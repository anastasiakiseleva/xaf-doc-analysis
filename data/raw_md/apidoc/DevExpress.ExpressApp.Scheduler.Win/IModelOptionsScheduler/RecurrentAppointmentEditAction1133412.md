---
uid: DevExpress.ExpressApp.Scheduler.Win.IModelOptionsScheduler.RecurrentAppointmentEditAction
name: RecurrentAppointmentEditAction
type: Property
summary: Specifies the action that will be performed when double-clicking a [recurrent event](xref:113128).
syntax:
  content: |-
    [DefaultValue(RecurrentAppointmentAction.Ask)]
    RecurrentAppointmentAction RecurrentAppointmentEditAction { get; set; }
  parameters: []
  return:
    type: DevExpress.XtraScheduler.RecurrentAppointmentAction
    description: A **RecurrentAppointmentAction** enumeration value specifying the action that will be performed when double-clicking a [recurrent event](xref:113128).
seealso:
- linkId: "112811"
---
This property is considered in Windows Forms applications.

The following values are possible:

* **Ask** - in the invoked dialog, you can choose whether to open a Detail View with the current occurrence or the entire series.
* **Cancel** - nothing is invoked.
* **Occurrence** - a Detail View representing the current occurrence is invoked.
* **Series** - a Detail View representing the entire series is invoked.