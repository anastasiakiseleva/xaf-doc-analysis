---
uid: DevExpress.ExpressApp.Scheduler.IModelListViewScheduler.ResourceClass
name: ResourceClass
type: Property
summary: Specifies the type of the objects that will serve as a resource data source for the Scheduler List Editor.
syntax:
  content: |-
    [DataSourceProperty("ResourceClasses", new string[]{})]
    [ModelBrowsable(typeof(ModelListViewSchedulerVisibilityCalculator))]
    IModelClass ResourceClass { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Model.IModelClass
    description: An [](xref:DevExpress.ExpressApp.Model.IModelClass) object representing the Class node corresponding to the type of the objects that will serve as a resource data source for the Scheduler List Editor.
seealso:
- linkId: "112812"
---
This property is considered for the List Views displayed by the `DevExpress.ExpressApp.Scheduler.Blazor.Editors.SchedulerListEditor` and [](xref:DevExpress.ExpressApp.Scheduler.Win.SchedulerListEditor).

If you have several classes that implement the `IResource` interface, you can set any of them for this property.