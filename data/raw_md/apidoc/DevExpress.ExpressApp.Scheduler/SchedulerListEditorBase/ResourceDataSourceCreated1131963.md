---
uid: DevExpress.ExpressApp.Scheduler.SchedulerListEditorBase.ResourceDataSourceCreated
name: ResourceDataSourceCreated
type: Event
summary: Occurs after the resources data source has been instantiated by the [](xref:DevExpress.ExpressApp.Scheduler.SchedulerListEditorBase)'s descendant.
syntax:
  content: public event EventHandler<ResourceDataSourceCreatedEventArgs> ResourceDataSourceCreated
seealso:
- linkId: DevExpress.ExpressApp.Scheduler.SchedulerListEditorBase.ResourceDataSourceCreating
---
This event is raised in the protected [](xref:DevExpress.ExpressApp.Scheduler.SchedulerListEditorBase).**CreateResourcesDataSource** method. Handle this event to perform custom actions over the resources data source used by the **SchedulerListEditorBase**'s descendant. The handler's **DataSource** parameter provides access to an object collection that represents the resources data source.

To specify a custom resources data source to be used by the **SchedulerListEditorBase**'s descendant, handle the [SchedulerListEditorBase.ResourceDataSourceCreating](xref:DevExpress.ExpressApp.Scheduler.SchedulerListEditorBase.ResourceDataSourceCreating) event.

For information on resources, refer to the [Resources in a Schedule](xref:112813) topic.