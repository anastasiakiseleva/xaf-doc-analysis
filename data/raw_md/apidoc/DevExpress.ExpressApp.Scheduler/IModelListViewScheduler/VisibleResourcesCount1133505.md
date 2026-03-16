---
uid: DevExpress.ExpressApp.Scheduler.IModelListViewScheduler.VisibleResourcesCount
name: VisibleResourcesCount
type: Property
summary: Specifies the count of [resources](xref:112813) shown at one time on a scheduler.
syntax:
  content: |-
    [DefaultValue(5)]
    [ModelBrowsable(typeof(ModelListViewSchedulerVisibilityCalculator))]
    int VisibleResourcesCount { get; set; }
  parameters: []
  return:
    type: System.Int32
    description: An integer value that specifies the count of resources shown at one time on a scheduler.
seealso:
- linkId: "112812"
---
XAF uses property for the List Views that [](xref:DevExpress.ExpressApp.Scheduler.Win.SchedulerListEditor) displays.

> [!NOTE]
> `SchedulerListEditor` for ASP.NET Core Blazor does not use this property. To save and restore resources selected at runtime, it uses the `IModelListViewSchedulerBlazor.VisibleResourceIds` property (not available in the Model Editor).