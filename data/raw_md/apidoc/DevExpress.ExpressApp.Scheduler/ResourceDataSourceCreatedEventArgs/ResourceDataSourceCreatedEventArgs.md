---
uid: DevExpress.ExpressApp.Scheduler.ResourceDataSourceCreatedEventArgs
name: ResourceDataSourceCreatedEventArgs
type: Class
summary: Represents arguments passed to the [SchedulerListEditorBase.ResourceDataSourceCreated](xref:DevExpress.ExpressApp.Scheduler.SchedulerListEditorBase.ResourceDataSourceCreated) event.
syntax:
  content: 'public class ResourceDataSourceCreatedEventArgs : EventArgs'
seealso:
- linkId: DevExpress.ExpressApp.Scheduler.ResourceDataSourceCreatedEventArgs._members
  altText: ResourceDataSourceCreatedEventArgs Members
---
The **ResourceDataSourceCreated** event is raised in the protected [](xref:DevExpress.ExpressApp.Scheduler.SchedulerListEditorBase).**CreateResourcesDataSource** method. You can use the **ResourceDataSourceCreated** event to perform custom actions over the resources data source used by the **SchedulerListEditorBase**'s descendant. The handler's [ResourceDataSourceCreatedEventArgs.DataSource](xref:DevExpress.ExpressApp.Scheduler.ResourceDataSourceCreatedEventArgs.DataSource) parameter provides access to an object collection that represents the resources data source.

To specify a custom resources data source to be used by the **SchedulerListEditorBase**'s descendant, handle the [SchedulerListEditorBase.ResourceDataSourceCreating](xref:DevExpress.ExpressApp.Scheduler.SchedulerListEditorBase.ResourceDataSourceCreating) event.

For information on resources, refer to the [Resources in a Schedule](xref:112813) topic.