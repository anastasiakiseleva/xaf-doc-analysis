---
uid: DevExpress.ExpressApp.Scheduler.Win.SchedulerListEditor.ResourcesDataSource
name: ResourcesDataSource
type: Property
summary: Provides access to the object that stores resources.
syntax:
  content: public IList ResourcesDataSource { get; set; }
  parameters: []
  return:
    type: System.Collections.IList
    description: A [](xref:System.Collections.IList) object that stores resources.
seealso: []
---
This property is intended for internal use. If you need to perform custom actions over the resources data source, or specify a custom resources data source to be used, handle the [SchedulerListEditorBase.ResourceDataSourceCreating](xref:DevExpress.ExpressApp.Scheduler.SchedulerListEditorBase.ResourceDataSourceCreating) and [SchedulerListEditorBase.ResourceDataSourceCreated](xref:DevExpress.ExpressApp.Scheduler.SchedulerListEditorBase.ResourceDataSourceCreated) events.