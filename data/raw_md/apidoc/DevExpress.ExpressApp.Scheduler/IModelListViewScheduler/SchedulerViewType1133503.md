---
uid: DevExpress.ExpressApp.Scheduler.IModelListViewScheduler.SchedulerViewType
name: SchedulerViewType
type: Property
summary: Specifies the view type used by the Scheduler List Editor.
syntax:
  content: |-
    [ModelBrowsable(typeof(ModelListViewSchedulerVisibilityCalculator))]
    SchedulerViewType SchedulerViewType { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Scheduler.SchedulerViewType
    description: A `SchedulerViewType` enumeration value that specifies the view type used by the Scheduler List Editor.
seealso:
- linkId: "112812"
---
This property is considered for the List Views displayed by the `DevExpress.ExpressApp.Scheduler.Blazor.Editors.SchedulerListEditor` and [](xref:DevExpress.ExpressApp.Scheduler.Win.SchedulerListEditor).

The following values are available:

* `Day` - lets users schedule and view appointments by day.
* `Month` - lets users schedule and view appointments across several weeks.
* `Timeline` - displays appointments as horizontal bars along the timescales and provides users with a scheduling overview.
* `Week` - lets users schedule and view appointments by week.
* `WorkWeek` - displays appointments for the working days in a particular week.
