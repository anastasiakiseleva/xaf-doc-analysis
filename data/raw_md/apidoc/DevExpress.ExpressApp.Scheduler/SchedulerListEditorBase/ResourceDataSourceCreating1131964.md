---
uid: DevExpress.ExpressApp.Scheduler.SchedulerListEditorBase.ResourceDataSourceCreating
name: ResourceDataSourceCreating
type: Event
summary: Occurs before the resources data source has been instantiated by the [](xref:DevExpress.ExpressApp.Scheduler.SchedulerListEditorBase)'s descendant.
syntax:
  content: public event EventHandler<ResourceDataSourceCreatingEventArgs> ResourceDataSourceCreating
seealso:
- linkId: DevExpress.ExpressApp.Scheduler.SchedulerListEditorBase.ResourceDataSourceCreated
---
This event is raised in the protected [](xref:DevExpress.ExpressApp.Scheduler.SchedulerListEditorBase).**CreateResourcesDataSource** method. Handle this event to specify a custom resources data source to be used by the **SchedulerListEditorBase**'s descendant. The handler's **ResourceType** parameter specifies the type of resource objects used by the Scheduler. Instantiate a collection of the required resources and pass it to the handler's **DataSource** parameter. Set the handler's **Handled** parameter to **true**, to prohibit the creation of the default resources collection.

To perform custom actions over the resources data source used by the **SchedulerListEditorBase**'s descendant, handle the [SchedulerListEditorBase.ResourceDataSourceCreated](xref:DevExpress.ExpressApp.Scheduler.SchedulerListEditorBase.ResourceDataSourceCreated).

For information on resources, refer to the [Resources in a Schedule](xref:112813) topic.