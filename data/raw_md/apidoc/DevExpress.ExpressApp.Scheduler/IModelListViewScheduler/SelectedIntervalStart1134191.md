---
uid: DevExpress.ExpressApp.Scheduler.IModelListViewScheduler.SelectedIntervalStart
name: SelectedIntervalStart
type: Property
summary: Specifies the starting point of the time interval selected in the scheduler's active view.
syntax:
  content: |-
    [ModelBrowsable(typeof(ModelListViewSchedulerVisibilityCalculator))]
    DateTime SelectedIntervalStart { get; set; }
  parameters: []
  return:
    type: System.DateTime
    description: A `DateTime` object that specifies the starting point of the time interval selected in the scheduler's active view.
seealso: []
---
XAF uses this property for the List Views that `DevExpress.ExpressApp.Scheduler.Blazor.Editors.SchedulerListEditor` and [](xref:DevExpress.ExpressApp.Scheduler.Win.SchedulerListEditor) display.